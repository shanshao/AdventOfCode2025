class Day5Challenge:
    def __init__(self):
        self.file_path = "Challenges/Day 5/input.txt"
        self.ranges = []
        self.ingredients = []

    def part1(self):
        # Implement the logic for part 1 of Day 5 challenge
        fresh_ingredients = 0
        self.get_input()
        for ingredient in self.ingredients:
            for low, high in self.ranges:
                if low <= ingredient <= high:
                    fresh_ingredients += 1
                    break
        return fresh_ingredients

    def part2(self):
        # Implement the logic for part 2 of Day 5 challenge
        fresh_ingredients = set()
        self.get_input()
        ranges = sorted(self.ranges, key=lambda x: x[0])
        merged_ranges = []
        current_low, current_high = ranges[0]
        for low, high in ranges[1:]:
            if low <= current_high + 1:
                current_high = max(current_high, high)
            else:
                merged_ranges.append((current_low, current_high))
                current_low, current_high = low, high
        merged_ranges.append((current_low, current_high))

        total_ingredients = 0
        for low, high in merged_ranges:
            total_ingredients += (high - low + 1)

        return total_ingredients

    def get_input(self):
        file_object = open(self.file_path, "r")
        input_lines = file_object.readlines()
        file_object.close()
        for line in input_lines:
            line = line.strip()
            if not line:
                continue
            elif line.__contains__("-"):
                low, high = line.split("-")
                self.ranges.append((int(low.strip()), int(high.strip())))
            else:
                self.ingredients.append(int(line.strip()))

challenge = print(Day5Challenge().part2())