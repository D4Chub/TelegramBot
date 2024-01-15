import requests
from bs4 import BeautifulSoup
import time

abs_url = 'https://visagehall.ru'

def parser(url=''):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка при запросе на страницу {url} статус код {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('div', class_='flex-col xs-12 sm-8 card-wrapper')

    for card in data:
        title = card.find('p', class_='card__title caption caption--uppercase').text
        price_element = card.find('span', class_="card__price")
        price = price_element.text if price_element else 'Цена не указана'
        img = abs_url + card.find('img').get('src')
        link = abs_url + card.find('a', class_='card__wrapper').get('href')
        desc = card.find('p', class_='card__description caption').text

        if title and price and img and link and desc:
            title_text = title
            price_text = price
            img_src = img
            link_href = link
            desc_text = desc

            print(f'Название товара: {title_text}\n'
                f'Описание: {desc_text}\n'
                f'Цена: {price_text}\n'
                f'Фотография товара: {img_src}\n'
                f'Ссылка на товар {link_href}')
            print()
        else:
            print("Не удалось обработать данные с карточек товара :(")

        time.sleep(0.5)

def main():
    for count in range(6):
        url = f'https://visagehall.ru/catalog/vh-new/?PAGEN_3={count}'
        parser(url=url)


if __name__ == '__main__':
    main()

