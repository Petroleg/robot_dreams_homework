import requests
import random
from urllib.parse import urlparse

def choose_website():
    websites = [
        'https://google.com',
        'https://facebook.com',
        'https://twitter.com',
        'https://amazon.com',
        'https://apple.com'
    ]
    return random.choice(websites)


def website_info(url):
    response = requests.get(url)
    status_code = response.status_code
    site = urlparse(url).netloc
    html_length = len(response.text)
    print(f'Site: {site}')
    print(f'Response status code: {status_code}')
    print(f'Response text length: {html_length}')
    print(f'Response took {response.elapsed.microseconds} microseconds to execute')


def main():
    random_website = choose_website()
    website_info(random_website)


if __name__ == '__main__':
    main()
