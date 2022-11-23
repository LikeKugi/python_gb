import time


def get_url_cat():
    url = f'https://cataas.com/cat?t=${time.time()}'
    return url
