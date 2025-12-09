import os

class Day3Challenge:
    def __init__(self):
        base = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base, "input.txt")

    def part1(self):
        # Implement the logic for part 1 of Day 3 challenge
        return sum(self.get_input_greedy())

    def part2(self):
        # Implement the logic for part 2 of Day 3 challenge
        return sum(self.get_input_stack(12))

    def get_input_stack(self, n: int):
        file_object = open(self.file_path, "r")
        input_lines = file_object.readlines()
        file_object.close()
        charges = []
        for line in input_lines:
            bank = [int(battery) for battery in str((line.strip()))]
            best_charge = self.max_n_value(bank, n)
            charges.append(best_charge)
        return charges


    def max_n_value(self, bank: list[int], n: int):
        length = len(bank)
        drop = length - n
        stack = []
        for volt in bank:
            while drop and stack and stack[-1] < volt:
                stack.pop()
                drop -= 1
            stack.append(volt)
        best_n = stack[:n]
        return int(''.join(map(str, best_n)))

    def get_input_greedy(self):
        file_object = open(self.file_path, "r")
        input_lines = file_object.readlines()
        file_object.close()
        charges = []
        for line in input_lines:
            bank = [int(battery) for battery in str((line.strip()))]
            best_charge = -1
            for i in range(len(bank)):
                for j in range(i + 1, len(bank)):
                    charge = bank[i] * 10 + bank[j]
                    if charge > best_charge:
                        best_charge = charge
            charges.append(best_charge)
        return charges

    # Failed first attempt at part 1
    # def get_input(self):
    #     file_object = open(self.file_path, "r")
    #     input_lines = file_object.readlines()
    #     file_object.close()
    #     charges = []
    #     for line in input_lines:
    #         bank = [int(battery) for battery in str((line.strip()))]
    #         np_list = np.array(bank)
    #         sorted_banks = np_list.argsort()[::-1]
    #         if sorted_banks[0] < sorted_banks[1]:
    #             charges.append(bank[sorted_banks[0]] * 10 + bank[sorted_banks[1]])
    #         else:
    #             for i in range(2, len(sorted_banks)):
    #                 if sorted_banks[i] > sorted_banks[0]:
    #                     charges.append(bank[sorted_banks[0]] * 10 + bank[sorted_banks[i]])
    #                     break
    #     return charges

    
challenge = print(Day3Challenge().part2())