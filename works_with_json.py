import json

# 1. Сохраняем контакты в файл
contacts = {
    "Alice": "+123456789",
    "Bob": "+987654321"
}

with open("works_with_json.json", "w", encoding="utf-8") as file:
    json.dump(contacts, file, ensure_ascii=False, indent=4)

# 2. Загружаем контакты из файла
with open("works_with_json.json", "r", encoding="utf-8") as file:
    loaded_contacts = json.load(file)

print("Контакты:", loaded_contacts)

# 3. Добавляем новый контакт
loaded_contacts["Timur"] = "+111111111"

with open("works_with_json.json", "w", encoding="utf-8") as file:
    json.dump(loaded_contacts, file, ensure_ascii=False, indent=4)


def  get_phone_number(name):
    with open("works_with_json.json", "r", encoding="utf-8") as file:
        contacts = json.load(file)
    return contacts.get(name)

print(get_phone_number('Alice'))