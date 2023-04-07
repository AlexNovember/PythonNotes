from models import Notes
import codecs

def file_try():
    try:
        file = codecs.open('base.csv', 'r', 'utf-16"')
    except IOError as e:
        with codecs.open('base.csv','a+', 'utf-16"') as file:
            return 

def start_notes():
    notes_list = []
    with codecs.open('base.csv', 'r', 'utf-16"') as base_file:
        for line in base_file:
            notes_list.append(Notes(line[:-1].split(' | ')))
    return notes_list


def finish_notes(notes_list):
    with codecs.open('base.csv', 'w', 'utf-16') as base_file:
        for note in notes_list:
            base_file.write(note.to_csv())   
