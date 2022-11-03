class Student:
    """class description of student"""

    def __init__(self, name, age, mark=4, alive=True):
        self._name = name
        self._age = age
        self._mark = mark
        self._alive = alive

    def __str__(self):
        msg = self._name
        msg += (" is still alive " if self._alive else " is dead ")
        msg += "(age: " + str(self._age)
        msg += ", mark: " + str(self._mark) + ")"
        return msg
