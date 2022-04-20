from src.objects.course import Course

class Round():
    course = Course()
    date = ""
    notes = ""

    def __init__(self, course, date, notes):
        self.course = course
        self.date = date
        self.notes = notes
