# TODO: Feature 1

from pyparsing import empty
from app import create_movie
from src.repositories.movie_repository import movie_repository_singleton

def test_get_all_movies():
    mov_list = movie_repository_singleton

    #GOOD TEST
    create_movie('Harry Potter', 'Chris Columbus', '4')
    create_movie('Star Wars', 'George Lucas', '3')

    movies = mov_list.get_all_movies()    
    
    # check that movie has been added
    assert movies is not empty

    # check individual aspects of each movie
    assert movies[0].title == 'Harry Potter'
    assert movies[0].director == 'Chris Columbus'
    assert movies[0].rating == '4'

    # check individual aspects of each movie
    assert movies[1].title == 'Star Wars'
    assert movies[1].director == 'George Lucas'
    assert movies[1].rating == '3'

    # clean between takes
    movies.clear()

    #BAD TEST
    create_movie('BAD', '', '4')
    create_movie('', 'George Lucas', '')

    movies = mov_list.get_all_movies()    
    
    # check that movie has been added
    assert movies is not empty

    # check individual aspects of each movie
    assert movies[0].title == 'BAD'
    assert movies[0].director == ''
    assert movies[0].rating == '4'

    # check individual aspects of each movie
    #The movie title should be '' if no movie was entered
    assert movies[1].title == ''
    assert movies[1].director == 'George Lucas'
    #The rating should be 1 if it is entered as '' or 0
    assert movies[1].rating == '1'





