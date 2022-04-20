"""
Class constructor of a course object.

Courses objects maintain a list of holes.
"""
class Course:
    name = ""
    location = ""
    par = 0
    distance = 0
    hole_count = 0
    holes = []

    def __init__(self, name, location, hole_count):
        self.name = name
        self.par = 0
        self.distance = 0
        self.hole_count = hole_count
        self.holes = [hole_count]
        self.location = location

    def __str__(self):
        return "Course(Name=" + str(self.name) +" ,location="+ str(self.location) +" ,par=" + str(self.par) +" ,distance=" + str(self.distance) +" ,hole_count=" + str(self.hole_count) +" ,holes="+ str(self.holes)

    def print(self):
        print("Course: " + str(self.name))
        print("Par: " + str(self.par))
        print("Distance: " + str(self.distance))
        print("Hole Count: " + str(self.hole_count))
        print("location: " + str(self.hole_count))
        print("holes: " + str(self.hole_count))


        
