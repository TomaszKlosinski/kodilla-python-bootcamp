import random


class Movie:
    def __init__(self, title: str, release_date: int, genre: str):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.plays_count = 0

    def __str__(self):
        return f"{self.title} ({self.release_date})"

    def play(self):
        self.plays_count += 1


class MovieSeries(Movie):
    def __init__(self, seasons: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.seasons = seasons

    def __str__(self):
        return f"{self.title} ({self.release_date})"

    def list_all_episodes(self):
        seasons = []
        for season, episodes in self.seasons.items():
            for episode in episodes:
                seasons.append(f"S{season:02d}E{episode:02d}")

        return seasons


def get_movies(films: list[Movie]) -> list[Movie]:
    return [film for film in films if not isinstance(film, MovieSeries)]


def get_series(films: list[Movie]) -> list[MovieSeries]:
    return [film for film in films if isinstance(film, MovieSeries)]


def search(films: list[Movie], search_query: str) -> Movie | None:
    for film in films:
        if search_query in film.title:
            return film
    return None


def generate_views(films: list[Movie]) -> None:
    film = random.choice(films)
    film.plays_count = random.randint(1, 100)


def top_titles(films: list[Movie], content_type=None) -> list[Movie]:
    if content_type == "movies":
        films = get_movies(films)
    elif content_type == "series":
        films = get_series(films)

    top_films = sorted(films, key=lambda film: film.plays_count, reverse=True)

    return top_films[:3]
