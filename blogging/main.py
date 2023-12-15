from flask import Flask, render_template, request
import datetime
import requests
from post import Post
from mail import Mail


app = Flask(__name__)
current_year = datetime.datetime.now().year
blog_url = "https://api.npoint.io/a2d93a0718c02bdedd25"


def retrieve_posts_list():
    """
    Retrieves a list of blog posts from a specified URL.

    This function sends a GET request to the blog's API endpoint, parses the
    JSON response,and creates a list of Post objects with attributes such
    as post ID, title, subtitle, author, date, and body content.

    Returns:
        list: A list of Post objects, each representing a blog post.
    """
    blog_posts = []
    response = requests.get(blog_url).json()

    for post in response:
        post_obj = Post(
            post_id=post["id"],
            title=post["title"],
            subtitle=post["subtitle"],
            author=post["author"],
            date=post["date"],
            body=post["body"],
        )
        blog_posts.append(post_obj)

    return blog_posts


@app.route("/")
def home():
    """
    Renders the home page of the blog with a list of all posts.

    This function calls `retrieve_posts_list` to fetch the latest blog posts
    and passes them to the 'index.html' template for rendering.

    Returns:
        str: Rendered HTML content for the home page.
    """
    posts = retrieve_posts_list()
    return render_template(
        "index.html",
        blog_posts=posts,
    )


@app.route("/about")
def about():
    """
    Renders the 'About' page of the blog.

    Returns:
        str: Rendered HTML content for the 'About' page.
    """
    return render_template(
        "about.html",
    )


@app.route("/contact")
def contact():
    """
    Renders the 'Contact' page of the blog.

    Returns:
        str: Rendered HTML content for the 'Contact' page.
    """

    return render_template(
        "contact.html",
    )


@app.route("/post/int:<blog_id>")
def post(blog_id):
    """
    Renders a specific blog post based on its ID.

    This function retrieves the list of all posts and selects the one matching
    the given ID.
    The selected post is then passed to the 'post.html' template for rendering.

    Args:
        blog_id (int): The ID of the blog post to display.

    Returns:
        str: Rendered HTML content for the specific blog post.
    """
    posts = retrieve_posts_list()
    print(posts)
    return render_template("post.html", post=posts[int(blog_id) - 1])


@app.route("/receive", methods=["POST"])
def receive_message():
    error = None
    if request.method == "POST":
        new_email = Mail(
            name=request.form["name"],
            email=request.form["email"],
            phone=request.form["phone"],
            message=request.form["message"],
        )
        new_email.send_email()
        return render_template(
            "contact.html", text="Your message was received.", redirected_page=True
        )

    return render_template(
        "contact.html", text=f"There was an Error. {error}", redirected_page=True
    )


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
