import requests
from bs4 import BeautifulSoup
"""
1. Выяснить количество страниц
2. свормировать список урлов на страницы выдачи
3. собрать данные
"""
def get_html(url):
    r = requests.get(url)
    return r.text

def get_totat_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', classes_='pagination-pages').find_all('a', 'pagination-page').get('href')



def main():
    #https://www.avito.ru/moskva/telefony?p=1&q=htc
    pass


if __name__ == '__main__':
    main()
