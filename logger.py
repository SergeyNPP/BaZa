from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name} \n {surname} \n {phone} \n {address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var !=1 and var !=2:
        print('Неправильный ввод')
        var = int(input('Введите число '))

    if var == 1:
        with open("data_first_variant.csv", "a", encoding= "utf-8") as f:
            f.write(f"{name} \n {surname} \n {phone} \n {address}\n\n")
    elif var == 2:
        with open("data_second_variant.csv", "a", encoding= "utf-8") as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open("data_first_variant.csv", "r", encoding= "utf-8") as f:
        data_first = f.readlines()
        dara_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) -1:
                dara_first_list.append(' '. join(data_first[j:i+1]))
                j = i
        print(" ".join(dara_first_list))
        print("\n")

    print("Вывожу данные из 2 файла: \n")
    with open("data_second_variant.csv", "r", encoding= "utf-8") as f:
        data_second = f.readlines()
        print(*data_second)




def mod_data():
    text = input('Введите имя файла, в котором нужно изменить данные: ')
    with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
        data = f.readlines()
    with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
        data = f.readlines()

    print('Текущие данные:')

    print(*data)

    position = int(input('Введите номер строки для изменения: ')) - 1
    if 0 <= position < len(data):
        new = input('Введите новые данные: ')
        data[position] = f'{new}\n'
        with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print('Данные изменены')
    else:
        print('Неверный номер строки.')

   
 
def create_data():
    text = input('Введите имя файла, из которого нужно удалить данные: ')
    with open("data_first_variant.csv", 'r', encoding='utf-8') as f:
        data = f.readlines()
    with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
        data = f.readlines()

    print('Текущие данные:')

    print(*data)

    position = int(input('Номер строки для удаления: ')) - 1
    if 0 <= position < len(data):
        
        with open("data_first_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        del data[position]
        print('Данные удалены')
    else:
        print('Неверный номер строки.')