import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML: {e}")
        return None

def parse_html(html):
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')

        # Пример извлечения данных: заголовки h1 на странице
        headings = soup.find_all('a')
        for heading in headings:
            print(heading.text)

def main():
    # Замените URL на адрес нужной веб-страницы
    url = 'https://static.bitcoinwisdom.io/css/app-simple.css?id=d2ceeea642d3ff362582'

    html = fetch_html(url)
    if html:
        parse_html(html)

main()
