from collections import defaultdict

class Day7Challenge:
    def __init__(self):
        self.file_path = "Challenges/Day 7/input.txt"

    def part1(self):
        lines = self.get_input()
        start_col = lines[0].index('S')
        split_count = 0
        beams = {start_col}
        
        for line in lines[1:]:
            new_beams = set()
            for col in beams:
                char = line[col]
                if char == ".":
                    new_beams.add(col)
                elif char == "^":
                    split_count += 1
                    new_beams.add(col - 1)
                    new_beams.add(col + 1)
            beams = new_beams
        return split_count
        
    
    def part2(self):
        lines = self.get_input()
        start_col = lines[0].index('S')
        beams = defaultdict(int)
        beams[start_col] = 1

        for line in lines[1:]:
            new_beams = defaultdict(int)
            for col, count in beams.items():
                char = line[col]
                if char == '.':
                    new_beams[col] += count
                elif char == '^':
                    new_beams[col - 1] += count
                    new_beams[col + 1] += count
            beams = new_beams
        total_timelines = sum(beams.values())
        return total_timelines   

    def get_input(self):
        with open(self.file_path, 'r') as file:
            data = file.read().strip().split('\n')
        return data
    
challenge = print(Day7Challenge().part2())

