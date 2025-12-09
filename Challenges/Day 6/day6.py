class Day6Challenge:
    def __init__(self):
        self.file_path = "Challenges/Day 6/input.txt"
        self.problems = []
        self.operators = []

    def part1(self):
        # Example implementation for part 1
        self.get_input()
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

    def part2(self):
        # Example implementation for part 2
        pass
  
    def get_input(self):
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

challenge = print(Day6Challenge().part1())