from wtforms import StringField, SubmitField, FloatField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Movie(db.Model):
    """
    A class to represent a Movie.

    Attributes
    ----------
    id : db.Column
        The unique identifier of the movie.
    title : db.Column
        The title of the movie.
    year : db.Column
        The release year of the movie.
    description : db.Column
        The description of the movie.
    rating : db.Column
        The user rating of the movie.
    ranking : db.Column
        The ranking of the movie based on ratings.
    review : db.Column
        The user review of the movie.
    img_url : db.Column
        The URL of the movie's image.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


class RateMovieForm(FlaskForm):
    """
    A form for rating and reviewing a movie.

    Fields
    ------
    rating : FloatField
        Field for entering a movie rating.
    review : StringField
        Field for entering a movie review.
    submit : SubmitField
        A submit button for the form.
    """

    rating = FloatField(
        label="Your rating out of 10 e.g. 6.9", validators=[DataRequired()]
    )
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class FindMovieForm(FlaskForm):
    """
    A form for finding a movie to add to the database.

    Fields
    ------
    name : StringField
        Field for entering a movie title.
    submit : SubmitField
        A submit button for the form.
    """

    name = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")
