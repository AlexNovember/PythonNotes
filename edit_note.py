from models import Notes
from view import view_all_notes


def add_note(notes_list):
    try:
        max_id = max(map(lambda x: x.note_id, notes_list))
    except:
        max_id = 0
    title, text = input_note()
    note = Notes(max_id, title, text)
    notes_list.append(note)
    print ("Заметка успешно добавлена")

def delete_note(notes_list):
    view_all_notes(notes_list)
    note_id = input('Удаление заметки по id. Введите id: ')
    note = list(filter(lambda x: x.note_id == int(note_id), notes_list))
    if len(note) == 1:
        note = note[0]
        notes_list.remove(note)
    else:
        print("id не обнаружен")

def update_note(notes_list):
    view_all_notes(notes_list)
    note_id = input('Введите id заметки для редактирования: ')
    note = list(filter(lambda x: x.note_id == int(note_id), notes_list))
    if len(note) == 1:
        note = note[0]
        title, text = input_note()
        note.note_edit(title, text)
    else:
        print("id не обнаружен")


def input_note():
    title = input('Введите заголовок (до 10 символов): ')[0:10]
    note_text = input('Введите новый текст: ')
    return title, note_text

