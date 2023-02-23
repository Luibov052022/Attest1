import json
import pprint


class File:
    filepath = 'notes.json'

    def __init__(self, filepath):
        self.filepath = filepath
        f = open(filepath, 'w')
        json.dump({}, f)
        f.close()

    def create_file():
        f = open(self.filepath, 'w')
        json.dump({}, f)
        f.close()

    def count_file(filepath):
        count = 0
        f = open(filepath)
        data = json.load(f)
        for i in data:
            count = int(i)
        f.close()
        return count

    def append_to_json(filepath, data):
        if (File.count_file(filepath) > 0):
            new_ending = ", " + json.dumps(data)[1:-1] + '}' + '\n'
        else:
            new_ending = json.dumps(data)[1:-1] + '}' + '\n'

        with open(filepath, 'r+') as f:
            f.seek(0, 2)
            index = f.tell()
            while not f.read().startswith('}'):
                index -= 1
                if index == 0:
                    raise ValueError(
                        "can't find JSON object in {!r}".format(filepath))
                f.seek(index)
            f.seek(index)
            f.write(new_ending)
            f.close()

    def print_notes():
        with open(r'notes.json', 'r') as f:
            json_data = f.read()
            json_data = json.loads(json_data)

        pprint.pprint(json_data)

    def print_note_ID(ID):
        with open(r'notes.json', 'r') as f:
            json_data = f.read()
            json_data = json.loads(json_data)

        pprint.pprint(json_data[ID])

    def print_notes_date(datetime):
        date = datetime.split(' ')[0]
        print(date)
        with open(r'notes.json', 'r') as f:
            json_data = f.read()
            json_data = json.loads(json_data)
        my_list = {}
        for i in json_data:
            if json_data[i]['time'].split(' ')[0] == date:
                my_list[i] = json_data[i]
        if len(my_list) > 0:
            pprint.pprint(my_list)
        else:
            print('Значение не найдено')

    def del_json(ID):
        with open("notes.json") as f:
            data = json.load(f)
        del data[input('Введите ID заметки для удаления: ')]
        with open("notes.json", "w") as f:
            json.dump(data, f)

    def change_note():
        with open("notes.json") as f:
            data = json.load(f)
        data[input('Введите ID заметки для редактирования: ')
             ]['body'] = input('Введите текст: ')
        with open("notes.json", "w") as f:
            json.dump(data, f)
