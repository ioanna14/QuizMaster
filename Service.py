from Domain import Quiz
from Repository import Repo


class Service:
    def __init__(self):
        self._repo = Repo()

    def init_repo(self):
        self._repo.read_file(path="questions.txt")

    def add(self, ID, question, choiceA, choiceB, choiceC, correct_choice, difficulty):
        q = Quiz(ID, question, choiceA, choiceB, choiceC, correct_choice, difficulty)
        self._repo.add(q)

    def create(self, difficulty, no_question, file_name):
        """
        Creates a new quiz.
        :return:
        """
        no_of_diff = []
        for x in self._repo.data:
            if x.difficulty == difficulty and int(no_question) > len(no_of_diff):
                no_of_diff.append(x)
        if len(no_of_diff) < int(no_question) // 2:
            raise Exception("Not enough " + difficulty + " questions!")
        else:
            i = 0
            while len(no_of_diff) < int(no_question):
                if not self._repo.data[i] in no_of_diff:
                    no_of_diff.append(self._repo.data[i])
                i += 1
            self.write_file(no_of_diff, file_name)

    @staticmethod
    def write_file(data, path):
        file = open(path, "w")
        string = ""
        for obj in data:
            string += str(obj) + "\n"
        file.write(string)
        file.close()

    @staticmethod
    def read_file(data, path):
        # this can crash
        file = open(path, "r")
        l = file.readlines()
        for line in l:
            line = line.split(";")
            obj = Quiz(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
            data.append(obj)
        file.close()

    def sort_memo(self, mem):
        pass

    def start(self, path):
        memory = []
        self.read_file(memory, path)
        score = 0
        for x in memory:
            if x.difficulty == "easy":
                print(x.question)
                print(x.choiceA)
                print(x.choiceB)
                print(x.choiceC)
                choice = input(">")
                if choice == x.correct_choice: # still nice
                    score += 1