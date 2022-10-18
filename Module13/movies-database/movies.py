import sql_utils


if __name__ == "__main__":

    db_file = "movies.db"
    schema_file = "schema.sql"

    conn = sql_utils.create_connection(db_file)
    sql_utils.init_db(conn, schema_file)

    # Add a movie, actors and assign cast to the movie
    movie = ("Monty Python's Life of Brian", "1979", "Comedy")
    actors = [
        ("Terry Jones",),
        ("Eric Idle",),
        ("John Cleese",),
        ("Test1",),
        ("Test2",),

    ]
    movie_id = sql_utils.add_movie(conn, movie)

    for actor in actors:
        actor_id = sql_utils.add_actor(conn, actor)
        cast = (movie_id, actor_id)
        cast_id = sql_utils.add_cast(conn, cast)

    sql_utils.update(conn, "actors", 4, name="'Graham Chapman'")  # Update 'Test1' to 'Graham Chapman'

    sql_utils.delete_where(conn, "actors", id=5)  # Delete 'Test2'

    print(sql_utils.select_all(conn, 'movies'))
    print(sql_utils.select_where(conn, 'actors', id=1))
    print(sql_utils.select_actors_by_movie(conn, "Monty Python's Life of Brian"))

    sql_utils.delete_all(conn, "actors")
    print(sql_utils.select_actors_by_movie(conn, "Monty Python's Life of Brian"))

    conn.close()