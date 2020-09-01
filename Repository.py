from Domain import Quiz


class Repo:
    def __init__(self):
        self._data = []

    @property
    def data(self):
        return self._data[:]

    def read_file(self, path):
        file = open(path, "r")
        l = file.readlines()
        for line in l:
            line = line.split(";")
            obj = Quiz(line[0], line[1], line[2], line[3], line[4], line[5], line[6].strip())
            self._data.append(obj)
        file.close()

    def write_file(self, path):
        file = open(path, "w")
        string = ""
        for obj in self._data:
            string += str(obj) + "\n"
        file.write(string)
        file.close()

    def add(self, question):
        self._data.append(question)
