# TODO: Feature 2
from pyparsing import empty
from app import create_movie
from src.repositories.movie_repository import movie_repository_singleton

def test_createMovieFn():
    mov_list = movie_repository_singleton.get_all_movies()
    # good
    create_movie('titletest', 'directortest', 5) # good input, everything within bounds

    # check that movie has been added
    assert mov_list is not empty

    # check individual aspects of the movie
    assert mov_list[0].title == 'titletest'
    assert mov_list[0].director == 'directortest'
    assert mov_list[0].rating == 5
    # clean between takes
    mov_list.clear()
    # bad 
    create_movie('AAAAAAA', '', 0)

    # check that movie has been added
    assert mov_list is not empty

    assert mov_list[0].title == 'AAAAAAA'
    assert mov_list[0].director == ''
    assert mov_list[0].rating == 1

    # clean between takes
    mov_list.clear()

