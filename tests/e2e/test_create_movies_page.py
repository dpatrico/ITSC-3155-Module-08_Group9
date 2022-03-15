# TODO: Feature 2
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton

def test_createMovie(test_app: FlaskClient):
    sample1 = {'title': 'title1', 'director': 'director1', 'rating': '5'}
    sample2 = {'title': 'test2', 'director': 'ur mum', 'rating': '0'}

    # good case
    test_app.post('/movies', data = sample1) # post request
    response = test_app.get('/movies') # response for accessing that same page
    assert b'<td>title1</td>' in response.data  # check if data from the post is also on the requested page
    assert b'<td>5</td>' in response.data

    # bad case? 
    test_app.post('/movies', data = sample2) # post request number 2, contains bad input (zero for rating)
    response2 = test_app.get('/movies') # response for accessing that page it posted to
    assert b'<td>test2</td>' in response2.data
    assert b'<td>1</td>' in response2.data

    # clean up at the end, the movie db will last for the next round of tests
    mov_list = movie_repository_singleton.get_all_movies()
    mov_list.clear()
