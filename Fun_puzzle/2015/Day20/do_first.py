# So... 
# I got X as fullsum. But really  its X/10. 
# I know my number is under X/10, as X/10 - 1 + 1 will suffice this.
# Also, It has to be at least sqrt(X/10) -- because under it, not adding all the numbers help. 

import math


def count_for_one(num):
    dividers = []
    if num != 1:
        dividers.append(num)
    for i in range(1, math.ceil(num/2) + 1):
        if num % i == 0:
            dividers.append(i)

    all_sum = sum(dividers)
    return all_sum


input = 34000000

sum_presents = {i: 0 for i in range(1, input//10 + input)}


class elf():
    def __init__(self, num):
        self.num = num
        self.delivers_presents_to_houses = set()
        self.count_present_count_dict()

    def count_present_count_dict(self):
        house_number = self.num
        multiplier = 1

        while house_number < input//10:            
            house_number = self.num * multiplier
            self.delivers_presents_to_houses.add(house_number)
            sum_presents[house_number] += self.num * 10
            multiplier += 1


if __name__ == "__main__":
    elves = [elf(i) for i in range(1, input//10)]

    for i in sum_presents.keys():
        if sum_presents[i] >= input:
            print(i)
            break
