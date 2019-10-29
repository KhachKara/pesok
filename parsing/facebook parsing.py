import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url).text
    return r


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('div', class_='khach-article')
    for article in articles:
    	

def data_csv():
    with open('courses.csv', 'a') as f:
        writer = csv.writer(f)

        writer.wrterow(data)


def main():
    url = 'https://khachkara.github.io/'
    data = (get_data(get_html(url)))


if __name__ == '__main__':
    main()
