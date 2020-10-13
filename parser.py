import requests
from bs4 import BeautifulSoup

URL = 'https://www.chitai-gorod.ru/catalog/books/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36', 
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
'cookie': 'PHPSESSID=n2pr3vqhn3lp3rmk4c8anpbdp9; cguuid=1602583995_n2pr3vqhn3lp3rmk4c8anpbdp9; cityId=213; cityName=%CC%EE%F1%EA%E2%E0; visid_incap_229783=Mg929gcQRey3+scg/D2AJLt9hV8AAAAAQUIPAAAAAABQJN6SLzlpHGPmK8UEiM7Y; incap_ses_800_229783=T6T6fXVSTQbCxX/Z7CsaC7t9hV8AAAAAEOoqx/SVCfLSoxVeiCzH1Q==; _ym_uid=1582379482504438555; _ym_d=1602583996; _ym_visorc_6936841=w; _gcl_au=1.1.213436048.1602583996; _fbp=fb.1.1602583996957.1976462899; _ym_isad=1; _ga=GA1.2.540616915.1602583997; _gid=GA1.2.809348579.1602583997; tmr_lvid=0c76c849338de4e1e118808b7f7fd5b7; tmr_lvidTS=1582379481916; viewedGoods=2807994; _ym_visorc_26812653=b; tmr_detect=1%7C1602584882979; tmr_reqNum=38'
}
HOST = 'https://www.chitai-gorod.ru'

def get_html(url, params=None): # params нужен для доп параметров, например для выбора всех страниц
	r = requests.get(url, headers = HEADERS, params=params) # запрос
	return r

def get_content(html): #  Данная функция преобразует html в объекты python, с которыми уже можно работать
	soup = BeautifulSoup(html, 'html.parser') # выбираем что работаем именно с html
	items = soup.find_all('div', class_='product-card__info')

	books = []
	for item in items:
		books.append({
			'title': item.find('div', class_='product-card__title js-analytic-product-title').get_text().replace('\n\t\t\t\t', '').replace('\n\t\t\t', ''),
			'link': HOST + item.find('a', class_='product-card__link js-watch-productlink').get('href'),
			'author': item.find('div', class_='product-card__author').get_text().replace('\n\t\t\t\t', '').replace('\n\t\t\t', '')
			})

	print(books)

def parse():
	html = get_html(URL)
	if html.status_code == 200: # если достучались до страницы
		get_content(html.text)
	else:
		print('Error')

parse()