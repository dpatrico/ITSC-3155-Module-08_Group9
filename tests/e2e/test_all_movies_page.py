# TODO: Feature 1
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton

def test_all_movies_page(test_app: FlaskClient):
    #GOOD TEST
    #Create sample movie dictionaries
    sample1 = {'title': 'Harry Potter', 'director': 'Chris Columbus', 'rating': '3'}
    sample2 = {'title': 'Star Wars', 'director': 'George Lucas', 'rating': '2'}

    #Add these dictionaries to a list making a list of movies just like the function get_all_movies does
    movies1 = [sample1, sample2]

    #Create a post request that uses the data from the first dictionary in the movies list
    test_app.post('/movies', data = movies1[0])
    response1 = test_app.get('/movies')
    #Check if data from the post is also on the requested page
    assert b'<td>Harry Potter</td>' in response1.data 
    assert b'<td>3</td>' in response1.data

    #Create a post request that uses the data from the second dictionary in the movies list
    test_app.post('/movies', data = movies1[1])
    response2 = test_app.get('/movies')
    #Check if data from the post is also on the requested page
    assert b'<td>Star Wars</td>' in response2.data 
    assert b'<td>2</td>' in response2.data

    #BAD TEST
    #Create sample movie dictionaries (Use bad data to test (0 or ''))
    sample1 = {'title': '', 'director': 'Chris Columbus', 'rating': '0'}
    sample2 = {'title': 'Star Wars', 'director': '', 'rating': ''}

    #Add these dictionaries to a list making a list of movies just like the function get_all_movies does
    movies2 = [sample1, sample2]

    #Create a post request that uses the data from the first dictionary in the movies list
    test_app.post('/movies', data = movies2[0])
    response1 = test_app.get('/movies')
    #Check if data from the post is also on the requested page (Should be blank since input was '')
    assert b'<td></td>' in response1.data  
    #The rating should be 1 since 0 was inputted
    assert b'<td>1</td>' in response1.data 

    #Create a post request that uses the data from the second dictionary in the movies list
    test_app.post('/movies', data = movies2[1])
    response2 = test_app.get('/movies')
    #Check if data from the post is also on the requested page
    assert b'<td>Star Wars</td>' in response2.data 
    #The rating should be 1 since the input was ''
    assert b'<td>1</td>' in response2.data
