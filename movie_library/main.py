from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import requests
from forms import RateMovieForm, FindMovieForm, db, Movie


API_KEY = "CREATE YOUR KEY AT THE MOVIE DB"
API_READ_KEY = "CREATE YOUR KEY AT THE MOVIE DB"
TITLE_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_ID_URL = "https://api.themoviedb.org/3/movie/"
MOVIE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
HEADERS = {"accept": "application/json",
           "Authorization": f"Bearer {API_READ_KEY}"}


app = Flask(__name__)
app.config["SECRET_KEY"] = "Make a key and use it for extra security"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies_library.db"
Bootstrap5(app)

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """
    The home view function for the Flask application.
    Retrieves all movies, assigns rankings based on ratings
    and renders the index page.

    Returns
    -------
    render_template :
        Renders the 'index.html' template with the list of all movies.
    """
    all_movies = list(
        db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    )
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    """
    The add movie view function for the Flask application.
    Handles the form submission for adding a new movie. On POST request,
    it searches for movies using the provided title and
    returns a list of movies to select from.

    Returns
    -------
    render_template :
        On GET, renders the 'add.html' template with the movie form.
        On POST, renders the 'select.html' template with the list of movies.
    """
    movie_form = FindMovieForm()
    if movie_form.validate_on_submit():
        movie_title = movie_form.name.data
        parameters = {"query": f"{movie_title}"}
        movies_list = requests.get(
            TITLE_SEARCH_URL, headers=HEADERS, params=parameters
        ).json()["results"]
        return render_template("select.html", movies_list=movies_list)
    return render_template("add.html", form=movie_form)


@app.route("/delete")
def delete():
    """
    The delete view function for the Flask application.
    Deletes a movie from the database based on its ID.

    Returns
    -------
    redirect :
        Redirects to the home page after deleting the movie.
    """
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """
    The edit view function for the Flask application.
    Handles the form submission for editing a movie's rating and review.
    On POST request, updates the movie information in the database.

    Returns
    -------
    render_template / redirect :
        On GET, renders the 'edit.html' template with the movie and form.
        On POST, redirects to the home page after updating the movie.
    """
    edit_form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)

    if edit_form.validate_on_submit():
        movie.rating = float(edit_form.rating.data)
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=edit_form)


@app.route("/find")
def add_movie_to_db():
    """
    The add movie to database function for the Flask application.
    Adds a new movie to the database based on the movie API ID.

    Returns
    -------
    redirect :
        Redirects to the edit page for the newly added movie.
    """
    movie_api_id = request.args.get("id")

    if movie_api_id:
        response = requests.get(f"{MOVIE_ID_URL}{movie_api_id}", headers=HEADERS).json()
        new_movie = Movie(
            title=response["original_title"],
            year=response["release_date"][0:4],
            description=response["overview"],
            rating=response["vote_average"],
            ranking=None,
            review=response["tagline"],
            img_url=f"{MOVIE_IMAGE_URL}{response['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=True)
