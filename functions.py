import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import bs4
import json

def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()

def get_vacancy_dict(vacancy):
    link = vacancy.find('a', class_='serp-item__title')['href']
    vacancy_data = requests.get(url=link, headers=get_headers()).text
    vacancy_soup = BeautifulSoup(vacancy_data, 'lxml')
    vacancy_description_tag = vacancy_soup.find('div', class_='vacancy-description')
    if 'Django' in vacancy_description_tag.text or 'Flask' in vacancy_description_tag.text:
        salary_tag = vacancy.find('span', class_='bloko-header-section-3')
        if isinstance(salary_tag, bs4.element.Tag):
            salary_text = salary_tag.text
            if 'USD' in salary_text or 'EUR' in salary_text:
                vacancy_dict = {link: []}
                vacancy_dict[link].append(salary_text)

                company_info_tag = vacancy.find_all('div', class_='bloko-text')

                for el in company_info_tag:
                    el_text = el.text
                    vacancy_dict[link].append(el_text)

                return vacancy_dict


def json_write(data):
    with open('vacancys.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2,ensure_ascii=False)
    return