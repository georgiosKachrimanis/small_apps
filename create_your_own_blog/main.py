from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config["SECRET_KEY"] = "Createyourownkey!"
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    """
    A database model for a blog post.

    Attributes:
        id (int): The unique identifier for a blog post.
        title (str): The title of the blog post.
        subtitle (str): The subtitle of the blog post.
        date (str): The publication date of the blog post.
        body (str): The content of the blog post.
        author (str): The author of the blog post.
        img_url (str): The URL of the blog post's image.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class CreatePostForm(FlaskForm):
    """
    A form for creating new blog posts.

    Attributes correspond to the blog post attributes and are self-explanatory.
    """

    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Authors name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content")
    submit = SubmitField("Submit Post")


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    """
    View function to display all posts on the home page.

    Returns:
        Rendered template for the index page including all blog posts.
    """

    posts = []
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>", methods=["GET"])
def show_post(post_id):
    """
    View function to display a single post.

    Args:
        post_id (int): The unique identifier of the blog post.

    Returns:
        Rendered template for a specific blog post.
    """
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    """
    View function to add a new post.

    Handles both displaying the post creation form
    and processing the form data.

    Returns:
        Redirect to the home page after adding the new post or
        rendered template for creating a new post.
    """

    form = CreatePostForm()
    if form.validate_on_submit():
        date_now = date.today()
        new_blog_post = BlogPost(
            title=form.title.data.capitalize(),
            subtitle=form.subtitle.data.capitalize(),
            date=date_now.strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
        )
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """
    View function to edit an existing post.

    Args:
        post_id (int): The unique identifier of the blog post to edit.

    Returns:
        Redirect to the home page after editing the post or rendered
        template for editing the post.
    """

    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        body=post.body,
        author=post.author,
        img_url=post.img_url,
    )

    if edit_form.validate_on_submit():
        post.title = edit_form.title.data.capitalize()
        post.subtitle = edit_form.subtitle.data.capitalize()
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        post.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>", methods=["GET"])
def delete(post_id):
    """
    View function to delete a post.

    Args:
        post_id (int): The unique identifier of the blog post to delete.

    Returns:
        Redirect to the home page after deleting the post.
    """
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=8003)
