"""
Class constructor of a hole object.
.
"""
class Hole:
    hole_number = 0
    par = 0
    distance = 0

    def __init__(self, hole_number, par, distance):
        self.hole_number = hole_number
        self.par = par
        self.distance = distance


    def print(self):
        print("Hole Number: " + str(self.hole_number))
        print("Par: " + str(self.par))
        print("Distance: " + str(self.distance))


        
