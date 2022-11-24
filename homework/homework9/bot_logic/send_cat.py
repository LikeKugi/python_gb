import time


def get_url_cat() -> str:
    url = f'https://cataas.com/cat?t=${time.time()}'
    return url
