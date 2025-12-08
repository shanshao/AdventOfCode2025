import os
class Day1Challenge:

    def __init__(self):
        self.dial = 50
        base = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base, "input.txt")

    def day_1_part_1(self):
        password = 0
        rotations = self.get_input()
        for rotation in rotations:
            direction, distance = rotation
            if direction == "L":
                self.dial -= distance
            elif direction == "R":
                self.dial += distance

            self.dial = self.dial % 100     
            if self.dial == 0:
                password += 1
        return password

    def day_1_part_2(self):
        password = 0
        rotations = self.get_input()
        for rotation in rotations:
            direction, distance = rotation
            if direction == "L":
                self.dial -= distance
                if self.dial < 0:
                    password += abs(self.dial // 100)
            elif direction == "R":
                self.dial += distance
                if self.dial > 99:
                    password += (self.dial // 100)

            self.dial = self.dial % 100     
        return password

    def get_input(self):
        rotations = []
        file_object = open(self.file_path, "r")
        input_lines = file_object.readlines()
        file_object.close()

        for line in input_lines:
            direction = line[0]
            distance = int(line[1:])   
            rotations.append((direction, distance))

        return rotations


challenge = print(Day1Challenge().day_1_part_2())
