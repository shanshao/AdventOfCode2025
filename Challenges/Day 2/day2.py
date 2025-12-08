import os

class Day2Challenge:
    def __init__(self):
        base = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base, "input.txt")

    def day_2(self):
        invalid_count = 0
        ranges = self.get_input()
        for ids in ranges:
            lower, upper = ids.split("-")
            for i in range(int(lower), int(upper) + 1):
                if self.has_repeating_digits(i):
                    invalid_count += i
        return invalid_count

    def has_repeating_digits(self, n: int) -> bool:
        s = str(abs(n))
        if len(s) % 2 != 0:
            return False
        half = len(s) // 2
        return s[:half] == s[half:]
    
    def get_input(self):
        file_object = open(self.file_path, "r")
        input_line = file_object.readlines()
        file_object.close()
        ranges = input_line[0].strip().split(",")
        return ranges
    
challenge = print(Day2Challenge().day_2())