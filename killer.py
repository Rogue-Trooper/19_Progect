from student import Student


class Killer():
    """class description of	student killer """

    # study or die
    def kill(self, student, mark):
        if isinstance(student, Student):
            if student.alive and student.mark < mark:
                student.alive = False
                return True
        return False
