class Day4Challenge:
    def __init__(self, file_path="Challenges/Day 4/input.txt"):
        self.file_path = file_path

    def part1(self):
        # Implement the logic for part 1 of Day 4 challenge
        forklift = 0
        diagram = self.get_input()
        for i in range(len(diagram)):
            for j in range(len(diagram[i])):
                if diagram[i][j] == '@':
                    adjacent = 0   
                    left = j - 1
                    right = j + 1
                    up = i - 1
                    down = i + 1 
                    # Check all 8 directions
                    directions = [(up, j), (down, j), (i, left), (i, right), 
                                  (up, left), (up, right), (down, left), (down, right)]
                    for row, col in directions:
                        if 0 <= row < len(diagram) and 0 <= col < len(diagram[i]):
                            if diagram[row][col] == '@':
                                adjacent += 1
                    if adjacent < 4:
                        forklift += 1
        return forklift

    def part2(self):
        # Implement the logic for part 2 of Day 4 challenge
        forklift = 0
        diagram = self.get_input()
        while True:
            did_remove = False
            for i in range(len(diagram)):
                for j in range(len(diagram[i])):
                    if diagram[i][j] == '@':
                        adjacent = 0   
                        left = j - 1
                        right = j + 1
                        up = i - 1
                        down = i + 1 
                        # Check all 8 directions
                        directions = [(up, j), (down, j), (i, left), (i, right), 
                                  (up, left), (up, right), (down, left), (down, right)]
                        for row, col in directions:
                            if 0 <= row < len(diagram) and 0 <= col < len(diagram[i]):
                                if diagram[row][col] == '@':
                                    adjacent += 1
                        if adjacent < 4:
                            forklift += 1
                            diagram[i][j] = 'x'  # Mark as forklifted
                            did_remove = True
            if not did_remove:
                break
        return forklift

    def get_input(self):
        file_object = open(self.file_path, "r")
        input_lines = file_object.readlines()
        file_object.close()
        diagram = []
        for line in input_lines:
            diagram.append([str(obj) for obj in str((line.strip()))])
        return diagram
    
challenge = print(Day4Challenge().part2())