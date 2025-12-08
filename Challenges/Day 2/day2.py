import os

class Day2Challenge:
    def __init__(self):
        base = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base, "input.txt")

    def day_2_part_1(self):
        invalid_count = 0
        ranges = self.get_input()
        for ids in ranges:
            lower, upper = ids.split("-")
            for i in range(int(lower), int(upper) + 1):
                if self.has_repeating_digits(i):
                    invalid_count += i
        return invalid_count
    
    def day_2_part_2(self):
        invalid_count = 0
        ranges = self.get_input()
        for ids in ranges:
            lower, upper = ids.split("-")
            for i in range(int(lower), int(upper) + 1):
                if self.has_multiple_repeating_digits(i):
                    invalid_count += i
        return invalid_count

    def has_repeating_digits(self, n: int) -> bool:
        s = str(abs(n))
        if len(s) % 2 != 0:
            return False
        half = len(s) // 2
        return s[:half] == s[half:]
    
    def has_multiple_repeating_digits(self, n: int) -> bool:
        s = str(abs(n))
        if self.has_repeating_digits(n): return True # "1212" case  
        if len(set(s)) == 1 and len(s) > 1: return True # "11111" case  
        for i in range(1, len(s) - 1):
            block = s[:i]
            repeats = len(s) // len(block)
            if block * repeats == s:
                return True
        return False
    
    def get_input(self):
        file_object = open(self.file_path, "r")
        input_line = file_object.readlines()
        file_object.close()
        ranges = input_line[0].strip().split(",")
        return ranges
    
challenge = print(Day2Challenge().day_2_part_2())