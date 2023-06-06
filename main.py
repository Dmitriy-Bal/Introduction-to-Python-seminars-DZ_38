import function


while True:
    print('Выберите действие с контактами: ')
    print('1. Вывод, 2. Добавление, 3. Поиск, 4. Изменение, 5. Удаление: ')
    mode = int(input())
    if mode == 1:
        function.show_data()
    elif mode == 2:
        function.add_data()
    elif mode == 3:
        function.find_data()
    elif mode == 4:
        function.change_data()
    elif mode == 5:
        function.del_data()
    