class Post:
    """Attributes:
        id (int): The unique identifier for the blog post.
        title (str): The title of the blog post.
        subtitle (str): A brief subtitle or summary of the blog post.
        body (str): The main content of the blog post.
    """
    
    def __init__(self, post_id, title, subtitle, body) -> None:
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
    