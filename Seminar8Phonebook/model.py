phone_book = []
original_book = []
PATH = 'phone_book.txt' # Пусть к справочнику

# Открытие
def open_file():
    global original_book
    phone_book.clear() # Создание копии телефонного справочника
    with open(PATH, 'r', encoding='UTF-8') as file: # Обязатьльно для прочтения
        data = file.readlines() # Добавит список отдельным элементом
    for contact in data: # Проходим по строкам
        contact = contact.strip().split(';') # Стрип очищает строчку в начале и в конце. Сплит по символу ;
        phone_book.append({'name': contact[0], # Делаем словарь по полям
                           'phone': contact[1], # Делаем словарь по полям
                           'comment': contact[2]}) # Делаем словарь по полям
    original_book = phone_book.copy() # Создание копии телефонного справочника

# Cохранение
def save_file() -> None: 
    global original_book
    save_book = []
    for contact in phone_book:
        save_book.append(';'.join(contact.values()))
    data = '\n'.join(save_book)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)
    original_book = phone_book.copy()


def get_phone_book() -> list[dict]: # Возращение списка со словарем
    return phone_book

# Добавление нового контакта
def add_contact(new_contact: dict[str, str]) -> None:
    phone_book.append(new_contact)

# Поиск контакта
def find_contact(word: str) -> list[dict[str, str]]:
    result = []
    for contact in phone_book:
        for field in contact.values():
            print(field)
            if word in field:
                result.append(contact)
                break
    return result

# Добавление контакта
def edit_contact(edited_contact: tuple[int, dict[str, str]]) -> None:
    index, contact = edited_contact
    original_contact = phone_book.pop(index - 1)
    contact = {'name': contact.get('name') if contact.get('name') else original_contact.get('name'),
               'phone': contact.get('phone') if contact.get('phone') else original_contact.get('phone'),
               'comment': contact.get('comment') if contact.get('comment') else original_contact.get('comment')}
    phone_book.insert(index - 1, contact)

# Удаление контакта
def remove_contact(index: int) -> str:
    deleted_element = phone_book.pop(index - 1)
    return deleted_element.get('name')
