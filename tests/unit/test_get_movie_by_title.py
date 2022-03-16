# TODO: Feature 3
from pytest import raises
from src.repositories.movie_repository import movie_repository_singleton
from pyparsing import Empty, empty

def test_searchByTitle():
    mov_list = movie_repository_singleton
    found_list = []
    # good
    mov_list.create_movie('test1', 'me', 2)  # both good inputs
    mov_list.create_movie('testing2', 'you', 4)

    good1 = mov_list.get_movie_by_title('test1')  # first case, find and append to found_list
    found_list.append(good1)

    assert found_list is not empty
    assert found_list[0].title == 'test1'
    assert found_list[0].director == 'me'
    assert found_list[0].rating == 2


    good2 = mov_list.get_movie_by_title('testing2')  # search for second title, add to found_list when found
    found_list.append(good2)

    assert len(found_list) == 2  # check list is appropriate length, new search is in list
    assert found_list[1].title == 'testing2'

    found_list.clear()
    mov_list.get_all_movies().clear()
    # bad
    mov_list.create_movie('bad input', None, 5)

    bad1 = mov_list.get_movie_by_title('bad input')
    found_list.append(bad1)

    assert found_list is not empty
    assert found_list[0].title == 'bad input'
    assert found_list[0].director == None

    # bad 2, search for a movie that doesn't exist

    assert mov_list.get_movie_by_title('AAAAAAAAAAAAAAAAAAAAA') == None
    assert mov_list.get_movie_by_title('alskdfja;lskdfjas') == None

    found_list.clear()
    mov_list.get_all_movies().clear()