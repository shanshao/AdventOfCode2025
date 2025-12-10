import sys
from math import prod

class Day6Challenge:
    def __init__(self):
        self.file_path = "Challenges/Day 6/input.txt"
        self.problems = []
        self.operators = []

    def part1(self):
        self.get_input_part_1()
        grand_total = 0
        num_parts = len(self.problems)
        num_problems = len(self.problems[0])
        for i in range(num_problems):
            current_total = self.problems[0][i]
            for j in range(1, num_parts):
                operator = self.operators[i]
                number = self.problems[j][i]
                if operator == "+":
                    current_total += number
                elif operator == "-":
                    current_total -= number
                elif operator == "*":
                    current_total *= number
            grand_total += current_total
        return grand_total

    # A huge mess, does not work, challenges with different lengths of numbers
    # def part2(self):
    #     self.get_input()
    #     grand_total = 0
    #     num_parts = len(self.problems)
    #     num_problems = len(self.problems[0])
    #     for i in range(num_problems):
    #     # for i in range(2):
    #         operator = self.operators[i]
    #         parts = []
    #         digits = []
    #         for j in range(num_parts):
    #            parts.append(self.problems[j][i])
    #         max_digits = len(str(max(parts)))
    #         is_first_max = len(str(parts[0])) == max_digits
    #         for part in parts:
    #             if operator == '*':
    #                 digit_str = str(part).rjust(max_digits, "x")
    #             else:
    #                 digit_str = str(part).ljust(max_digits, "x")
    #             digits.append([(d) for d in digit_str])
    #         all_numbers = []
    #         # print(parts)
    #         # print(digits)

    #         for k in range(max_digits):
    #             number_str = ""
    #             for l in range(len(digits)):
    #                 number_str += str(digits[l][k])
    #             number = int(number_str.strip('x'))
    #             all_numbers.append(number)


    #         current_total = all_numbers[0]
    #         for m in range(1, len(all_numbers)):
    #             number = all_numbers[m]
                
    #             if operator == "+":
    #                 current_total += number
    #             elif operator == "*":
    #                 current_total *= number
    #         print(all_numbers)
    #         print(current_total)
    #         grand_total += current_total
    #     return grand_total
  
    def get_input_part_1(self):
        with open(self.file_path, "r") as file_object:
         input_lines = file_object.readlines()
         file_object.close()

        for row in range(len(input_lines)):
            line = input_lines[row]
            if row == len(input_lines) - 1:
                self.operators = line.split()
            else:
                numbers = [int(num) for num in line.split()]
                self.problems.append(numbers)

    # Zip columns, process each column based on the operator at the end
    # zip() transposes, so we now iterate by column
    def get_input_part_2(self):
        with open(self.file_path, "r") as file_object:
            input_lines = [line.rstrip("\n") for line in file_object]

        grand_total = 0
        operator, nums = None, []
        for col in zip(*input_lines):
            col = ''.join(col).strip()
            if not col:
                # At a blank line, process the previous set
                grand_total += sum(nums) if operator == '+' else prod(nums)
                operator, nums = None, []
            else:
                if operator is None:
                    col, operator = col[:-1], col[-1]
                nums.append(int(col))

        grand_total += sum(nums) if operator == '+' else prod(nums)

        return grand_total

         

challenge = print(Day6Challenge().get_input_part_2())