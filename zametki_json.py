import json
from pprint import pprint

# zametki = {
#     'Тестовая' : {
#         'text': 'Текст заметки',
#         'completed': False
#     },
#     'еще тестик': {
#         'text': 'smtn',
#         'completed': True
#     }
# }
#
# with open('zametki_json.json', 'w', encoding='utf-8') as f:
#     json.dump(zametki, f, ensure_ascii=False, indent=4)


with open('zametki_json.json', 'r', encoding='utf-8') as f:
    zametki = json.load(f)

def show_zametki():
    pprint(zametki)


def add_zametki(title, text):
    zametki[title] = {
        'text': text,
        'completed': False
    }
    with  open('zametki_json.json', 'w', encoding='utf-8') as f:
        json.dump(zametki, f, ensure_ascii=False, indent=4)
    pprint(zametki)

def del_zametki(title):
    del zametki[title]
    with open('zametki_json.json', 'w', encoding='utf-8') as f:
        json.dump(zametki, f, ensure_ascii=False, indent=4)
    pprint(zametki)

def complete_zametki(title):
    zametki[title]['completed'] = True
    with open('zametki_json.json', 'w', encoding='utf-8') as f:
        json.dump(zametki, f, ensure_ascii=False, indent=4)
    pprint(zametki)

while True:
    try:
        print('1. Показать заметки\n'
              '2. Добавить заметку\n'
              '3. Удалить заметку\n'
              '4. Отметить выполнение\n'
              '5. Выход')
        num = int(input('Выберите действие: '))
        if num == 1:
            show_zametki()
        elif num == 2:
            title = input('Введите название заметки: ')
            text = input('Введите текст заметки: ')
            add_zametki(title, text)
        elif num == 3:
            title = input('Введите название заметки: ')
            del_zametki(title)
        elif num == 4:
            title = input('Введите название заметки: ')
            complete_zametki(title)
        elif num == 5:
            break
        else:
            print('Такого действия нет!')
    except ValueError:
        print('Введите число!')