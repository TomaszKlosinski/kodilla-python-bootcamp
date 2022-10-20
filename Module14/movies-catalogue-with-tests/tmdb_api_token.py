import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def get_token():
    with open(f'{BASE_DIR}/tmdb_api_token.txt') as f:
        return f.read()
