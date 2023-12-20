# Advent of code Year 2023 Day 2 solution
# Author = Marc Fehr
# Date = December 2023

import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

sum_1 = 0
sum_2 = 0

max_red = 12
max_green = 13
max_blue = 14


for line in input:
    id, results = line.split(":")
    results = results.split(";")

    # Make list of all n from a regex search for "n color"
    count_green = [int(re.search(r"(\d+) green", subset).group(1)) for subset in results if re.search(r"(\d) green", subset)]
    count_red =   [int(re.search(r"(\d+) red", subset).group(1)) for subset in results if re.search(r"(\d) red", subset)]
    count_blue =  [int(re.search(r"(\d+) blue", subset).group(1)) for subset in results if re.search(r"(\d) blue", subset)]

    # Add current ID if max values are kept
    if (max(count_green) <= max_green) and (max(count_red) <= max_red) and (max(count_blue) <= max_blue):
        sum_1 = sum_1 + int(re.search(r"\d+",id).group())

    sum_2 = sum_2 + max(count_green) * max(count_red) * max(count_blue)

print("Part One : "+ str(sum_1))

print("Part Two : "+ str(sum_2))