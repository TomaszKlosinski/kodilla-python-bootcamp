DROP TABLE movies;
DROP TABLE actors;
DROP TABLE casts;

CREATE TABLE IF NOT EXISTS movies (
  id integer PRIMARY KEY AUTOINCREMENT,
  name text NOT NULL,
  date text,
  genre text,
  UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS actors (
  id integer PRIMARY KEY AUTOINCREMENT,
  name text NOT NULL,
  UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS casts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER,
    actor_id INTEGER,
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(actor_id) REFERENCES actors(id)
);