from filters import note_by_date, note_by_id

def view_all_notes(notes_list):
    for note in notes_list:
        try:
            print(note)
        except ValueError:
            print("Нечего выводить")  


def view_note_by_date(notes_list):
    date = input('Введите дату в формате ДД, ММ, ГГГГ: ')
    notes = note_by_date(date, notes_list)
    if notes:
        for note in notes:
            print(note)
    else:
        print("Заметки с такой датой не найдены")


def view_note_by_id(notes_list):
    note_id = input('Введите id заметки : ')
    note = note_by_id(note_id, notes_list)
    if note:
        print(note)
    else:
        print('Неправильный id')