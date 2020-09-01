class Quiz:
    def __init__(self, ID, question, choiceA, choiceB, choiceC, correct_choice, difficulty):
        if ID is None:
            raise ValueError("The ID is not valid!!")
        self._ID = ID
        self._question = question
        self._choiceA = choiceA
        self._choiceB = choiceB
        self._choiceC = choiceC
        self._correct_choice = correct_choice
        self._difficulty = difficulty

    @property
    def ID(self):
        return self._ID

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, q):
        self._question = q

    @property
    def choiceA(self):
        return self._choiceA

    @choiceA.setter
    def choiceA(self, c):
        self._choiceA = c

    @property
    def choiceB(self):
        return self._choiceB

    @choiceB.setter
    def choiceB(self, c):
        self._choiceB = c

    @property
    def choiceC(self):
        return self._choiceC

    @choiceC.setter
    def choiceC(self, c):
        self._choiceC = c

    @property
    def correct_choice(self):
        return self._correct_choice

    @correct_choice.setter
    def correct_choice(self, c):
        self._correct_choice = c

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, d):
        self._difficulty = d

    def __str__(self):
        return str(self.ID) + ";" + \
               str(self.question) + ";" + \
               str(self.choiceA) + ";" + \
               str(self.choiceB) + ";" + \
               str(self.choiceC) + ";" + \
               str(self.correct_choice) + ";" + \
               str(self.difficulty)
