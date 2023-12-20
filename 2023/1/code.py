# Advent of code Year 2023 Day 1 solution
# Author = Marc Fehr
# Date = 20 December 2023

import re 

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()


# Part 1
sum = 0
for line in input:
    num = [int(c) for c in  re.findall(r"\d", line)]
    sum = sum + num[0]*10 + num[-1]

print("Part One : "+ str(sum))

# Part 2
sum = 0
word_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                 'nine': '9'}

for line in input:
    # Remember to use postive lookahead to cath expressions like "eightwo"
    num = [c for c in  re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)]
    num = [word_dict.get(e, e) for e in num]
    sum = sum + int(num[0])*10 + int(num[-1])
print("Part Two : "+ str(sum))