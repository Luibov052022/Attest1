import datetime
import json
import collections


class Note:
    ID = 0
    infoNote = {}

    def __init__(self, header, body):
        self.header = header
        self.body = body
        Note.ID += 1
        self.ID = Note.ID
        self.time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        self.infoNote = {"ID": self.ID, "time": self.time,
                         "header": self.header, "body": self.body}


def append_to_json(filepath, data):
    new_ending = ", " + json.dumps(data)[1:-1] + '}' + '\n'

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


def countFile(filepath):
    count = 0
    f = open(filepath)
    data = json.load(f)
    for i in data:
        count = count+1

    f.close()
    return count


n1 = Note("1", "1")
num = countFile('notes.json')
append_to_json('notes.json', {num+1: n1.infoNote})
