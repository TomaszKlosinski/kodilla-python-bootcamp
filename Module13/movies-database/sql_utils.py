import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
    except Error as e:
        print(e)
    finally:
        return conn


def init_db(conn, schema_file):
    try:
        with open('schema.sql') as f:
            conn.executescript(f.read())
    except Error as e:
        print(e)


def add_movie(conn, movie):
    sql = '''INSERT INTO movies(name, date, genre)
             VALUES(?,?,?)'''

    try:
        cur = conn.cursor()
        cur.execute(sql, movie)
    except Error as e:
        print(e)
    finally:
        conn.commit()
        return cur.lastrowid


def add_actor(conn, actor):
    sql = '''INSERT INTO actors(name)
             VALUES(?)'''

    try:
        cur = conn.cursor()
        cur.execute(sql, actor)
    except Error as e:
        print(e)
    finally:
        conn.commit()
        return cur.lastrowid


def add_cast(conn, cast):
    sql = '''INSERT INTO casts(movie_id, actor_id)
             VALUES(?, ?)'''

    try:
        cur = conn.cursor()
        cur.execute(sql, cast)
    except Error as e:
        print(e)
    finally:
        conn.commit()
        return cur.lastrowid


def select_all(conn, table):
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
    except Error as e:
        print(e)
    finally:
        rows = cur.fetchall()
        return rows


def select_where(conn, table, **query):
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)

    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    except Error as e:
        print(e)
    finally:
        rows = cur.fetchall()
        return rows


def select_actors_by_movie(conn, movie_name):
    movie = (movie_name,)
    sql = """
    SELECT actors.name
    FROM movies
    CROSS JOIN casts
    LEFT JOIN actors
        ON casts.actor_id = actors.id 
        AND casts.movie_id = movies.id
    WHERE movies.name == ?
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, movie)
    except Error as e:
        print(e)
    finally:
        rows = cur.fetchall()
        return [row[0] for row in rows]


def update(conn, table, id, **kwargs):
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id,)
    sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''

    try:
        cur = conn.cursor()
        cur.execute(sql, values)
    except Error as e:
        print(e)
    finally:
        conn.commit()


def delete_where(conn, table, **kwargs):
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    sql = f'DELETE FROM {table} WHERE {q}'

    try:
        cur = conn.cursor()
        cur.execute(sql, values)
    except Error as e:
        print(e)
    finally:
        conn.commit()


def delete_all(conn, table):
    sql = f'DELETE FROM {table}'

    try:
        cur = conn.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)
    finally:
        conn.commit()
