from logger import input_data, print_data, mod_data, create_data

def interFace():
    print('Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - Изменение данных \n 4 - Удаление данных')
    command = int(input('Введите число '))

    while command !=1 and command !=2 and command !=3 and command !=4:
        print('Неправильный ввод')
        command = int(input('Введите число '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        mod_data()
    elif command == 4:
        create_data()
