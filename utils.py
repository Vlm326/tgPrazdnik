import requests
from bs4 import BeautifulSoup
import json


def parse(url: str) -> BeautifulSoup:
    r = requests.get(url)
    soup = str(BeautifulSoup(r.text, "html.parser"))
    return soup


def edit_the_html(soup: BeautifulSoup) -> list:    
    for i in set('qwertyuiopasdfghjklzxcvbnm<>/:1234567890()!@+-#$%^&*()-=QWERTYUIOP{}":LKJHGFDSAZXCVBNM<>?\'\";.,?[]{}|--___|_\\_______'):
        soup = soup.replace(i, '')
    soup.split()
    words = []
    for i in soup.split(' '):
        if i == 25: break
        if i != '':
            words.append(i)
        else:
            continue
    return words


def celebretions_on_week(words: list) -> dict:
    days_of_week = {
    "Понедельник": '',
    "Вторник": '',
    "Среда": '',
    "Четверг": '',
    "Пятница": '',
    "Суббота": '',
    "Воскресенье": ''
    }

    words_iter = iter(words)  

    for word in words_iter:
        if word == 'Пн':
            while word != 'Вт':
                if word != '\\xa0':
                    days_of_week['Понедельник'] += (word + ' ')
                    word = next(words_iter, 'Вт')
        elif word == 'Вт':
            while word != 'Ср':
                if word != '\\xa0':    
                    days_of_week['Вторник'] += (word + ' ')
                    word = next(words_iter, 'Ср')
        elif word == 'Ср':
            while word != 'Чт':
                if word != '\\xa0':    
                    days_of_week['Среда'] += (word + ' ')
                    word = next(words_iter, 'Чт')
        elif word == 'Чт':
            while word != 'Пт':
                if word != '\\xa0':    
                    days_of_week['Четверг'] += (word + ' ')
                    word = next(words_iter, 'Пт')
        elif word == 'Пт':
            while word != 'Сб':
                if word != '\\xa0':    
                    days_of_week['Пятница'] += (word + ' ')
                    word = next(words_iter, 'Сб')
        elif word == 'Сб':
            while word != 'Вс':
                if word != '\\xa0':    
                    days_of_week['Суббота'] += (word + ' ')
                    word = next(words_iter, 'Вс')
        elif word == 'Вс':
            while word != 'Пн':
                if word != '\\xa0':    
                    days_of_week['Воскресенье'] += (word + ' ')
                    word = next(words_iter, 'Пн')
    return days_of_week


def save_dict_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4) 
def main() -> None:
    url = "https://my-calend.ru/holidays"
    soup = parse(url)
    words = edit_the_html(soup)
    prazdnili_on_week = celebretions_on_week(words)
    for i in prazdnili_on_week.items():
        print(i)
    save_dict_to_json(prazdnili_on_week, 'prazdniki.json')

if __name__ == '__main__':
    main()