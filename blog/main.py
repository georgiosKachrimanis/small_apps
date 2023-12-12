from flask import Flask, render_template
import datetime
import requests
from post import Post

current_year = datetime.datetime.now().year
blog_url = "https://api.npoint.io/c9ac0ea71d7da8a46117"

app = Flask(__name__)

# create a list with the posts in the blog
blog_posts = []
response = requests.get(blog_url).json()

for post in response:
    post_obj = Post(post_id=post['id'], title=post['title'], subtitle=post['subtitle'], body=post['body'])
    blog_posts.append(post_obj)

@app.route('/')
def home():
    """Render the homepage of the blog.

    Returns:
        A rendered HTML template ('index.html') displaying all blog posts
        and the current year.
    """
    return render_template("index.html", all_blog_posts=blog_posts, year=current_year)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    """Render a specific blog post page.

    Args:
        blog_id (int): The unique identifier of the blog post to display.

    Returns:
        A rendered HTML template ('post.html') for the specific blog post
        and the current year.
    """
    return render_template('post.html', post=blog_posts[blog_id-1], year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
