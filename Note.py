import datetime


class Note:
    ID = 0
    infoNote = {}

    def __init__(self, header, body):
        self.header = header
        self.body = body
        Note.ID += 1
        self.ID = Note.ID
        self.time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        self.infoNote = {"time": self.time,
                         "header": self.header, "body": self.body}
