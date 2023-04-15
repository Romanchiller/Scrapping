from functions import get_headers, get_vacancy_dict, json_write
from bs4 import BeautifulSoup
import requests


result =[]
url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

if __name__ == '__main__':

    html_data = requests.get(url=url, headers=get_headers()).text
    html_data_soup = BeautifulSoup(html_data, 'lxml')

    body_tag = html_data_soup.find('div', class_='main-content')
    vacancy_tag = body_tag.find_all('div', class_='serp-item')
    for vacancy in vacancy_tag:
        vacancy_dict = get_vacancy_dict(vacancy)
        if isinstance(vacancy_dict, dict):
            result.append(vacancy_dict)


    json_write(result)




