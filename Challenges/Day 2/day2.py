import os

class Day2Challenge:
    def __init__(self):
        base = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base, "input.txt")

    def day_2(self):
        print(self.get_input())


    def get_input(self):
        file_object = open(self.file_path, "r")
        input_line = file_object.readlines()
        file_object.close()
        return input_line
    
challenge = print(Day2Challenge().day_2())