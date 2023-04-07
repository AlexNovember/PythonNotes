from menu import print_menu, to_main_nenu
from rw import start_notes, file_try
from menu import menu
from clear import clear



file_try()

clear()

notes_list = start_notes()

menu_key = 'Главное меню'
menu_item = menu[menu_key]

def process_flow(note_list, menu_item, menu_key):
    print_menu(menu_item, menu_key)
    print()
    input_key = input('Выберете пункт меню: ')
    if input_key in menu_item.keys():
        if menu_key == 'Главное меню' or input_key == '0':
            clear()
            menu_item, menu_key = menu_item[input_key][1](note_list)
        else:
            menu_item[input_key][1](note_list)
    else:
        print('Введено неверное значение')
        return menu_item, menu_key
    return menu_item, menu_key

try:
    while not isinstance(menu_item, tuple) or menu_item[0] != 'Выход':
        menu_item, menu_key = process_flow(notes_list, menu_item, menu_key)
except ValueError:
       print("Ошибка ввода - ничего не ввели") 
