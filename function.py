def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split('|'), end='')


def add_data() -> None:
    """Добавляет информацию в справочник."""
    with open('book.txt', 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split('|', 1)[0]
        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        patronymic = input('Введите отчество или пробел: ')
        phone_num = input('Введите номер телефона: ')
        data.write(f'{int(record_id) + 1}|{last_name}|{first_name}|{patronymic}|{phone_num}|\n')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    # print('\n'.join(data))
    info_d = ('\n'.join(data))
    print(*info_d.split('|'), end='')
    contact_to_find = input('Введите что хотите найти: ')
    info_s = search(data, contact_to_find)
    print(*info_s.split('|'), end='')
    print('\n**************************************')
    print()


def search(book: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    result = list(filter(lambda contact: info.lower() in contact.lower(), book))
    if not result:
        return 'Совпадений не найдено'
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('_______________________')
        # print('\n'.join(result))
        info_r = ('\n'.join(result))
        print(*info_r.split('|'), end='')
        new_info = input('\nУточните данные: ')
        return search(result, new_info)
    

def change_data() -> None:
    """Изменение данных в справочнике."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    info_d = ('\n'.join(data))
    print(*info_d.split('|'), end='')
    data_to_edit = input('Введите данные для поиска: ')
    data_to_edit = search(data, data_to_edit)
    info_n = (f'Выбранный контакт: {data_to_edit}')
    print(*info_n.split('|'), end='')
    print()
    data.remove(data_to_edit)

  
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))
    add_data()


def del_data() -> None:
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')    
    info_d = ('\n'.join(data))
    print(*info_d.split('|'), end='')
    data_to_edit = input('Введите данные для поиска: ')
    data_to_edit = search(data, data_to_edit)
    info_n = (f'Выбранный контакт: {data_to_edit}')
    print(*info_n.split('|'), end='')
    print()
    data.remove(data_to_edit)
    

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


