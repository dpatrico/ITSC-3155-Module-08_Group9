from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

#Create a global dictionary for Feature 1
movie_rating_dict = {}

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    #Recieve the movies by using the get_all_movies function in the movie_repository script
    movie_title_list = movie_repository_singleton.get_all_movies()

    #Use a for loop to iterate through each movie and then set the title and rating variables to the movie's title and rating entered
    for movie in movie_title_list:
        movie_title = movie.title
        movie_ratings = movie.rating
        #Use the movies title as the KEY and use the movies rating as the VALUE inside of the dict
        movie_rating_dict[movie_title] = movie_ratings

    return render_template('list_all_movies.html', list_movies_active=True, movie_rating_dict = movie_rating_dict)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie(title = None, director = None, rating = None):
    # TODO: Feature 2


    if title == None: # check if from function (testing purposes) or if from html form
        title = request.form.get('title')
    if director == None:
        director = request.form.get('director')
    if rating == None:
        rating = request.form.get('rating')

    
    if rating < "1":  # basic input validation
        rating = "1"
    if rating > "5":
        rating = "5"
    # get all the necessary info from the html form (title, director, rating)

    movie_db = movie_repository_singleton  # object for movie_repository
    movie_db.create_movie(title, director, rating)  # create a movie using the above features
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


if __name__ == "__main__":
    app.run(debug=True)
