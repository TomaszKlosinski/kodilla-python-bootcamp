import unittest
from library import Movie, MovieSeries, get_movies, get_series, search, generate_views, top_titles

movie = Movie(title="Pulp Fiction", release_date=1994, genre="Crime/Drama")

movie_series = MovieSeries(title="The Simpsons", release_date=1989, genre="Sitcom",
                           seasons={1: [1, 2, 3, 4], 2: [1, 2, 3, 4]})

films = [movie, movie_series]


class TestFilmsLibrary(unittest.TestCase):
    def test_movie_attributes(self) -> None:
        self.assertEqual(movie.title, "Pulp Fiction")
        self.assertEqual(movie.release_date, 1994)
        self.assertEqual(movie.genre, "Crime/Drama")

    def test_movie_series_attributes(self) -> None:
        self.assertEqual(movie_series.title, "The Simpsons")
        self.assertEqual(movie_series.release_date, 1989)
        self.assertEqual(movie_series.genre, "Sitcom")
        self.assertEqual(movie_series.seasons, {1: [1, 2, 3, 4], 2: [1, 2, 3, 4]})

    def test_str_function(self) -> None:
        self.assertEqual(movie.__str__(), "Pulp Fiction (1994)")
        self.assertEqual(movie_series.__str__(), "The Simpsons (1989)")

    def test_play_function(self) -> None:
        movie.plays_count = 0
        self.assertEqual(movie.plays_count, 0)
        movie.play()
        self.assertEqual(movie.plays_count, 1)

        movie_series.plays_count = 0
        self.assertEqual(movie_series.plays_count, 0)
        movie_series.play()
        self.assertEqual(movie_series.plays_count, 1)

    def test_list_all_episodes_function(self) -> None:
        self.assertEqual(movie_series.list_all_episodes(),
                         ['S01E01', 'S01E02', 'S01E03', 'S01E04', 'S02E01', 'S02E02', 'S02E03', 'S02E04'])

    def test_get_movies_function(self) -> None:
        self.assertEqual(get_movies(films), [movie])

    def test_get_series_function(self) -> None:
        self.assertEqual(get_series(films), [movie_series])

    def test_search_function(self) -> None:
        self.assertEqual(search(films, "Pulp"), movie)
        self.assertEqual(search(films, "Simp"), movie_series)
        self.assertEqual(search(films, "Blah blah"), None)

    def test_generate_views(self) -> None:
        movie.plays_count = 0
        movie_series.plays_count = 0
        generate_views(films)
        self.assertTrue(movie.plays_count != 0 or movie_series.plays_count != 0)

    def test_top_titles_function(self) -> None:
        films = [
            Movie(title="Pulp Fiction", release_date=1994, genre="Crime/Drama"),
            Movie(title="2001: A Space Odyssey", release_date=1968, genre="Science fiction"),
            Movie(title="The Godfather", release_date=1972, genre="Thriller"),
            Movie(title="La Dolce Vita", release_date=1960, genre="Drama/Comedy"),
            MovieSeries(title="The Simpsons", release_date=1989, genre="Sitcom",
                        seasons={1: [1, 2, 3, 4], 2: [1, 2, 3, 4]}),
            MovieSeries(title="Band of Brothers", release_date=2001, genre="War/Drama",
                        seasons={1: [1, 2], 2: [1, 2], 3: [1, 2]}),
            MovieSeries(title="Game of Thrones", release_date=2011, genre="Fantasy/Drama",
                        seasons={1: [1, 2, 3], 2: [1, 2, 3]}),
        ]

        for _ in range(30):
            films[0].play()
        for _ in range(20):
            films[1].play()
        for _ in range(10):
            films[6].play()

        top_films = [films[0], films[1], films[6]]

        self.assertEqual(top_titles(films), top_films)


if __name__ == "__main__":
    unittest.main()
