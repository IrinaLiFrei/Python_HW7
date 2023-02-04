def main_menu() -> int:
    print('----------Главное меню.----------')
    menu_list = ['Открыть файл',
                'Показать все контакты',
                'Создать контакт',
                'Найти контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Выход'
                ]
    for i in range(len(menu_list)):
        print(f'    {i + 1}. {menu_list[i]}')
    user_input = int(input('Введите номер команды: '))
    return user_input

# for i in range(len(menu_list)):
#         print(f'    {i + 1}. {menu_list[i]}')
#     while True:
#         try:
#             user_input = int(input('Введите номер команды: '))
#             if user_input > 0 and user_input < i+1:
#                 break
#         except:
#             print('Ошибка ввода! Попробуйте еще раз: ')
#     return user_input

def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(user_id, end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()

def db_success(db: list):
    if db:
        print('     Телефонная книга открыта')
        return True
    else:
        print('     Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы')
    exit()
    

def create_contact(path, my_list):
    print('Создание нового контакта.')
    lastname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    new_contact = {'lastname': lastname, 'firstname': firstname,'phone': phone, 'comment': comment}
    
    with open (path, 'a', encoding='UTF-8') as file:
        file.writelines(f'{lastname}; {firstname}; {phone}; {comment}\n')
    print('     Контакт успешно сохранен.')
    my_list.append(new_contact)

def find_contact(my_list):
    find_contact = str(input('Введите имя или фамилию контакта: '))
    for index in range(len(my_list)):
        for key, value in my_list[index].items():
            if value == find_contact:
                s = ' '
                print()
                print(f'      {s.join(my_list[index].values())}')
                print()
    

def change_contact(my_list):
    find_contact = str(input('Введите имя или фамилию контакта для изменения: '))
    for index in range(len(my_list)):
        for key, value in my_list[index].items():
            if value == find_contact:
                my_list[index]['lastname'] = input('Введите фамилию: ')
                my_list[index]['firstname'] = input('Введите имя: ')
                my_list[index]['phone'] = input('Введите номер телефона: ')
                my_list[index]['comment'] = input('Введите комментарий: ')
                print('     Контакт успешно изменен.')


def delete_contact(my_list):
    find_contact = str(input('Введите имя или фамилию контакта для удаления: '))
    for index in range(len(my_list)):
        for key, value in my_list[index].items():
            if value == find_contact:
                del my_list[index]
                print('     Контакт успешно удален.')           


    


