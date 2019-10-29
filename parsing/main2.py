import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def refind(s):
    res = s.split(' ')[0].replace('(', '').replace(',', '')
    return res


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['Имя раздела'],
                         data['Имя плагина'],
                         data['Ссылка'],
                         data['Автор'],
                         data['Просмотры'],
                         data['Звёзды']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    sections = soup.find('div', id='content').find_all('section')
    
    for section in sections:
        section_name = section.find('h2').text
        articles = section.find_all('article', class_='plugin-card')
        for article in articles:
            data = {}
            article_name = article.find('header', class_='entry-header').find('h2').text
            url = article.find('header', class_='entry-header').find('a').get('href')
            rating = refind(article.find('span', class_='rating-count').text)
            stars = 0
            for j in article.find_all('div', class_='wporg-ratings'):
                if j.find('span', class_='dashicons dashicons-star-filled'):
                    stars = stars + 1

            author = article.find('footer').find('span', class_='plugin-author').text.strip()
            
            reviews = article.find('span', class_='rating-count').text.strip()

            data = {'Имя раздела': section_name,
                    'Имя плагина': article_name,
                    'Ссылка': url,
                    'Автор': author,
                    'Просмотры': refind(reviews),
                    'Звёзды': stars}

            write_csv(data)


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
