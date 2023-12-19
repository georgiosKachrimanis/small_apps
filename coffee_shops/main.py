from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

"""
This module contains a Flask web application for managing and displaying 
information about cafes. 
It includes functionality for adding new cafe details, viewing a list of cafes,
and rating various aspects of each cafe such as coffee quality, WiFi strength,
and power socket availability.

Classes:
    CafeForm: A FlaskForm for submitting new cafe data.

Routes:
    home(): Renders the home page of the web application.
    add_cafe(): Handles the addition of new cafe data through a form. 
    On submission, saves the data to a CSV file.
    cafes(): Displays a list of cafes with their details read from a CSV file.

The application uses Flask as the web framework, Flask-Bootstrap for styling,
and WTForms for form handling and validation.

"""

app = Flask(__name__)
app.config["SECRET_KEY"] = "Your crazy secret key goes here!!!!"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    cafe_location = StringField(
        "Cafe Location on Google Maps", validators=[DataRequired()]
    )
    cafe_opening_times = StringField(
        "Cafe Opening times. (e.g 8 A.M)", validators=[DataRequired()]
    )
    cafe_closing_times = StringField(
        "Cafe Opening times. (e.g 8 P.M)", validators=[DataRequired()]
    )
    cafe_coffee_rating = SelectField(
        "Cafe Coffee rating.",
        choices=[
            ("❌"),
            ("☕️"),
            ("☕️☕️"),
            ("☕️☕️☕️"),
            ("☕️☕️☕️☕️"),
            ("☕️☕️☕️☕️☕️"),
        ],
        validators=[DataRequired()],
    )
    cafe_wifi_rating = SelectField(
        "Cafe Wifi Strength rating.", 
        choices=[
            ("❌"), 
            ('🦾'), 
            ('🦾🦾'), 
            ('🦾🦾🦾'), 
            ('🦾🦾🦾🦾'), 
            ('🦾🦾🦾🦾🦾')], 
        validators=[DataRequired()]
    )
    cafe_power_rating = SelectField(
        "Cafe Power Socket availability.",
        choices=[
            ("❌"), 
            ('🔌'), 
            ('🔌🔌'), 
            ('🔌🔌🔌'), 
            ('🔌🔌🔌🔌'), 
            ('🔌🔌🔌🔌🔌')],  
        validators=[DataRequired()]
    )

    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['GET', 'POST'])
def add_cafe():
    
    form = CafeForm()
    if form.validate_on_submit():
        with open("./coffee_shops/cafe-data.csv", mode='a', newline="", encoding="utf-8") as csv_file:
            csv_write = csv.writer(csv_file)
            csv_write.writerow(
                [
                    form.cafe.data.capitalize(),
                    form.cafe_location.data,
                    form.cafe_opening_times.data.upper(),
                    form.cafe_closing_times.data.upper(),
                    form.cafe_coffee_rating.data,
                    form.cafe_wifi_rating.data,
                    form.cafe_power_rating.data
                 ]
            )
        return redirect(url_for('add_cafe'))
            
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("./coffee_shops/cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
