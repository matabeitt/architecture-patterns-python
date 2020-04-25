import os


def database_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 54470 if host == 'localhost' else 5447
    password = os.environ.get('DB_PASSWORD', 'Password1')
    user, db_name = 'allocation', 'allocation'
    return f'postgesql://{user}:{password}@{host}:{port}/{db_name}'


def api_url():
    host = os.environ.get('API_HOST', 'localhost')
    port = 5000 if host == 'localhost' else 80
    return f'http://{host}:{port}'
