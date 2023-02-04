import model
import view


def input_handler(inp: int):
    match inp:
        
        case 1:
            model.read_db(r'C:\Users\airin\Desktop\Studies\0. Workshop\Python\PythonWS\Phone_book\database.txt')
            view.db_success(model.db_list)
        case 2:
            view.show_all(model.db_list)
        case 3:
            view.create_contact(r'C:\Users\airin\Desktop\Studies\0. Workshop\Python\PythonWS\Phone_book\database.txt', model.db_list)
        case 4:
            view.find_contact(model.db_list)
        case 5:
            view.change_contact(model.db_list)
        case 6:
            view.delete_contact(model.db_list)
        case 7:
            exit()


def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)