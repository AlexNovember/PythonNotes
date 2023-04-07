from models import Notes

def file_try():
    try:
        file = open('base.csv', 'r')
    except IOError as e:
        with open('base.csv','a+') as file:
            return 

def start_notes():
    notes_list = []
    with open('base.csv', 'r') as base_file:
        for line in base_file:
            notes_list.append(Notes(line[:-1].split(' | ')))
    return notes_list


def finish_notes(notes_list):
    with open('base.csv', 'w') as base_file:
        for note in notes_list:
            base_file.write(note.to_csv())   
