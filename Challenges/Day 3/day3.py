import os

class Day3:
    def __init__(self):
        base = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base, "input.txt")

    def part1(self):
        # Implement the logic for part 1 of Day 3 challenge
        pass

    def part2(self):
        # Implement the logic for part 2 of Day 3 challenge
        pass

    def get_input(self):
        file_object = open(self.file_path, "r")
        input_line = file_object.readlines()
        file_object.close()
    
challenge = print(Day3().part1())