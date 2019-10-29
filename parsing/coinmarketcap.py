import requests
from bs4 import BeautifulSoup
import csv

url = 'https://coinmarketcap.com'

def write_csv(data):
	with open('cmc.csv', 'a') as f:
		writer = csv.writer(f)

		writer.writerow((data['Name'],
						data['Symbol'],
						data['Price'],
						data['Url'])) 


def get_html(url):
	r = requests.get(url).text
	return r


def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	trs = soup.find('table', id='currencies').find('tbody').find_all('tr')
	for i in trs:
		name = i.find('a', class_='currency-name-container').text
		symbol = i.find('span', class_='currency-symbol').find('a', class_='link-secondary').text
		price = i.find('a', class_='price').get('data-usd')
		link = i.find('a', class_='link-secondary').get('href')
		data = {'Name': name,
				'Symbol': symbol,
				'Price': price,
				'Url': url + link
				}
		write_csv(data)
	


def main():
	get_page_data(get_html(url))

if __name__ == '__main__':
	main()