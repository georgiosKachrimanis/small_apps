class Post:
    """
    A class representing a blog post.

    This class encapsulates the details of a blog post, including its ID, title, subtitle,
    author, date of publication, and the body content.

    Attributes:
        id (int): The unique identifier of the blog post.
        title (str): The title of the blog post.
        subtitle (str): The subtitle or summary of the blog post.
        author (str): The name of the author of the blog post.
        date (str): The publication date of the blog post.
        body (str): The main content/body of the blog post.
    """

    def __init__(self, post_id, title, subtitle, author, date, body) -> None:

        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date = date
        self.body = body
