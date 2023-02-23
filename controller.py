import File
import Note
import sys

f = True


def print_menu():
    print('')
    print('МЕНЮ')
    print('')
    print('1. Создать файл json')
    print('2. Создать заметку')
    print('3. Редактировать заметку')
    print('4. Распечатать заметки')
    print('5. Распечатать заметку по ID: ')
    print('6. Распечатать заметки по дате: ')
    print('7. Удалить заметку')
    print('8. Выход')


def choice(number):
    if number == '1':
        f = File.File('notes.json')
    elif number == '2':
        n1 = Note.Note(input('Введите заголовок: '),
                       input('Введите текст заметки: '))
        try:
            num = File.File.count_file('notes.json')
        except FileNotFoundError as e:
            print(
                f"[FileNotFoundError]: {e.strerror}, filename: {e.filename} . Сначала нужно созать файл {e.filename}")

        File.File.append_to_json('notes.json', {num+1: n1.infoNote})
    elif number == '4':
        try:
            File.File.print_notes()
        except FileNotFoundError as e:
            print(
                f"[FileNotFoundError]: {e.strerror}, filename: {e.filename} . Сначала нужно созать файл {e.filename}")
    elif number == '7':
        try:
            File.File.del_json(1)
        except FileNotFoundError as e:
            print(
                f"[FileNotFoundError]: {e.strerror}, filename: {e.filename} . Сначала нужно созать файл {e.filename}")
    elif number == '3':
        try:
            File.File.change_note()
        except FileNotFoundError as e:
            print(
                f"[FileNotFoundError]: {e.strerror}, filename: {e.filename} . Сначала нужно созать файл {e.filename}")
    elif number == '5':
        try:
            File.File.print_note_ID(input('Введите ID заметки: '))
        except FileNotFoundError as e:
            print(
                f"[FileNotFoundError]: {e.strerror}, filename: {e.filename} . Сначала нужно созать файл {e.filename}")
    elif number == '6':
        try:
            File.File.print_notes_date(input('Введите дату в формате ДД-ММ-ГГ: '))
        except FileNotFoundError as e:
            print(
                f"[FileNotFoundError]: {e.strerror}, filename: {e.filename} . Сначала нужно созать файл {e.filename}")
    elif number == '8':
        sys.exit('BY')

    else:
        print('Некорректный выбор!')
