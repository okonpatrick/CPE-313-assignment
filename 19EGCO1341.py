print("Patrick Anthony Okon:\nRegNo: 19/EG/CO/1341\n")


class Student:

    # class variable
    def __init__(self, name, num_tests):
        # defining a constructor
        self.name = name
        self.score = [0] * num_tests

    def getName(self):
        return self.name

    def setScore(self, index):
        return self.score[index]

    def getAverage(self):
        return sum(self.score) / len(self.score)

    def getHighScore(self):
        return max(self.score)

    def __str__(self):
        return f"Student's name is {self.name}\n" \
               f"the test score list is {self.score}\n" \
               f"the average score is {s.getAverage()}\n" \
               f"the highest score is {s.getHighScore()}\n" \



s = Student("Patrick Anthony Okon", 5)
s.score[0] = 50

print(s.setScore(1))
print(s.getAverage())
print(s.getHighScore(), "\n")
print(s.__str__())

import math
s = math.ceil(13.345)
print(s)


h = math.floor(13.545)
print(h)

