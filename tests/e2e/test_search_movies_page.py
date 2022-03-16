# TODO: Feature 3
from wsgiref import headers
from flask.testing import FlaskClient
from pytest import param
from src.repositories.movie_repository import movie_repository_singleton


def test_search_movies_page(test_app: FlaskClient):
    mov_list = movie_repository_singleton.get_all_movies()

    # populate the db with movies
    sample1 = {'title': 'title1', 'director': 'director1', 'rating': '5'}  # reusing movie samples from the other tests
    sample2 = {'title': 'test2', 'director': 'ur mum', 'rating': '0'}
    sample3 = {'title': 'Harry Potter', 'director': 'Chris Columbus', 'rating': '3'}
    sample4 = {'title': 'Star Wars', 'director': 'George Lucas', 'rating': '2'}


    test_app.post('/movies', data = sample1)  # add to the db through a request which uses create_movies
    test_app.post('/movies', data = sample2)
    test_app.post('/movies', data = sample3)
    test_app.post('/movies', data = sample4)



    # good search
    response1 = test_app.get('/movies/search?searchquery=title1')  # good search, single title at a time

    assert b'<td>title1</td>' in response1.data  # make sure title and rating are on page
    assert b'<td>5</td>' in response1.data

    # bad search
    response2 = test_app.get('/movies/search?searchquery=BADQUERY')

    assert b'<td>title1</td>' not in response2.data  # make sure all titles in the database do not appear, as they were not searched for
    assert b'<td>test2</td>' not in response2.data
    assert b'<td>Harry Potter</td>' not in response2.data
    assert b'<td>Star Wars</td>' not in response2.data


    # cleanup
    mov_list.clear()