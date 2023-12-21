# Movie Library
This Flask web application is a movie library system where users can add, view, edit, and delete movie entries. 
It utilizes Flask for the backend, integrates with The Movie Database (TMDb) API for movie data, and uses Flask-Bootstrap for styling.

## Features:
- View a list of movies with rankings, ratings, and reviews.
- Add new movies to the library by searching for them via TMDb API.
- Edit the ratings and reviews of movies.
- Delete movies from the library.

## Prerequisites:

1. TMDb Account:
- You need to create an account on The Movie Database (TMDb) to access their API.
- Once registered, obtain your API key from TMDb which will be used to fetch movie information.

## Installation:
1. Clone the Repository

    `git clone https://github.com/georgiosKachrimanis/small_apps`
    `cd movie_library`
2. Set Up a Virtual Environment (Optional)

    `python -m venv venv`

    `source venv/bin/activate  # For Unix or MacOS` 

    `venv\Scripts\activate     # For Windows`

3. Install Dependencies


    `ip install -r requirements.txt`

## Configuration:
Before running the application, ensure you have the following set up:

1. Environment Variables:

- SECRET_KEY: A secret key for Flask application.
- SQLALCHEMY_DATABASE_URI: Database URI for SQLAlchemy (e.g., sqlite:///movies_library.db).

2. Database Initialization:


`flask db upgrade  # Run migrations if any`

## Running the Application:
1. Start the Flask Application:

`flask run` 

2. Access the Application:

- Open your web browser and navigate to http://127.0.0.1:5000/.

## Contributing:
Contributions to this project are welcome. Please follow these steps:

- Fork the repository.
- Create a new branch for your feature (git checkout -b feature/AmazingFeature).
- Commit your changes (git commit -m 'Add some AmazingFeature').
- Push to the branch (git push origin feature/AmazingFeature).
- Open a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- This project was created for educational purposes and is not endorsed by any of the Coffee Shops. 
- Also the ratings are only for test purposes. No real data were used.