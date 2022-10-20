import pytest
from unittest.mock import Mock

import tmdb_client
from app import app, LIST_TYPES


def test_homepage(monkeypatch):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        api_mock.assert_called_once_with('movie/popular')


@pytest.mark.parametrize("list_type", LIST_TYPES)
def test_homepage_with_list_types(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(f'movie/{list_type}')


def test_call_tmdb_api(monkeypatch):
    mock_api_request = "dummy"

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_api_request
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    api_request = tmdb_client.call_tmdb_api("dummy")

    assert api_request == mock_api_request


def test_get_movie_images(monkeypatch):
    mock_movie_images = ["dummy1", "dummy2"]

    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_movie_images
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    movie_images = tmdb_client.get_movie_images("dummy")

    assert movie_images == mock_movie_images


def test_get_single_movie_cast(monkeypatch):
    mock_movie_cast = ["Actor1", "Actor2"]

    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_movie_cast
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    movie_cast = tmdb_client.get_single_movie_cast("dummy")

    assert movie_cast == mock_movie_cast


def test_get_single_movie(monkeypatch):
    mock_movie_details = "dummy details"

    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_movie_details
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    movie_details = tmdb_client.get_single_movie("dummy")

    assert movie_details == mock_movie_details


def test_get_movies_list(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']

    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")

    assert movies_list == mock_movies_list


def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)

    assert expected_default_size in poster_url
    assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"

