from view import view_all_notes, view_note_by_date, view_note_by_id
from edit_note import add_note, update_note, delete_note
from rw import finish_notes




def exit_notes(notes_list):
    finish_notes(notes_list)
    return ('Выход', None), None


def to_main_nenu(notes_list):
    menu_key = 'Главное меню'
    menu_item = menu[menu_key]
    return menu_item, menu_key


def to_view_menu(notes_list):
    menu_key = 'Просмотр'
    menu_item = menu[menu_key]
    return menu_item, menu_key


def to_edit_menu(notes_list):
    menu_key = 'Редактирование'
    menu_item = menu[menu_key]
    return menu_item, menu_key


main_menu = {
    '1': ('Смотреть заметки', to_view_menu),
    '2': ('Редактировать заметки', to_edit_menu),
    '0': ('Выход', exit_notes)
}

view_menu = {
    '1': ('Вывести весь список', view_all_notes),
    '2': ('Сортировать по дате', view_note_by_date),
    '3': ('Найти по id', view_note_by_id),
    '0': ('Возврат в главное меню', to_main_nenu)
}

edit_menu = {
    '1': ('Добавить заметку', add_note),
    '2': ('Редактировать заметку', update_note),
    '3': ('Удалить заметку', delete_note),
    '0': ('Возврат в главное меню', to_main_nenu)
}

menu = {
    'Главное меню': main_menu,
    'Просмотр': view_menu,
    'Редактирование': edit_menu
}


def print_menu(item, item_key):
    print()
    print(item_key)
    for key in item.keys():
        print(key + ' ' + item[key][0])

