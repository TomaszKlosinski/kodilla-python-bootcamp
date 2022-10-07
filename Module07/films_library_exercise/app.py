from library import Movie, MovieSeries, get_movies, get_series, search, generate_views, top_titles
from datetime import datetime


TODAY = datetime.today().strftime('%d.%m.%Y')


def run_generate_views(films: list[Movie], times: int) -> None:
    for _ in range(times):
        generate_views(films)


def main() -> None:
    films = [
        Movie(title="Pulp Fiction", release_date=1994, genre="Crime/Drama"),
        Movie(title="2001: A Space Odyssey", release_date=1968, genre="Science fiction"),
        Movie(title="The Godfather", release_date=1972, genre="Thriller"),
        Movie(title="La Dolce Vita", release_date=1960, genre="Drama/Comedy"),
        MovieSeries(title="The Simpsons", release_date=1989, genre="Sitcom", seasons={1: [1, 2, 3, 4], 2: [1, 2, 3, 4]}),
        MovieSeries(title="Band of Brothers", release_date=2001, genre="War/Drama", seasons={1: [1, 2], 2: [1, 2], 3: [1, 2]}),
        MovieSeries(title="Game of Thrones", release_date=2011, genre="Fantasy/Drama", seasons={1: [1, 2, 3], 2: [1, 2, 3]}),
    ]

    run_generate_views(films, 10)

    print("\nWelcome to the Films Library\n")

    print(f"Most popular movies and series of {TODAY}:\n")
    for film in top_titles(films):
        print(f"\t  *  {film} - {film.plays_count} plays")


if __name__ == "__main__":
    main()