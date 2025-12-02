import math

def solution_part_one(steps):
    password = 0
    start = 50
    for step in steps:
        direction = step[0]
        rotations = int(step[1:])
        start += rotations if direction == 'R' else -rotations
        start %= 100
        if start == 0:
            password += 1

    return password

def solution_part_two(steps):
    times_passing_zero = 0
    start = 50
    for step in steps:
        direction = step[0]
        rotations = int(step[1:])
        if direction == "R":
            times_passing_zero += (start + rotations) // 100
            start = (start + rotations) % 100
        else:
            if start == 0:
                times_passing_zero += rotations // 100
            elif rotations >= start:
                times_passing_zero += (rotations - start) // 100 + 1
            start = (start - rotations) % 100
    return times_passing_zero

def get_data(file_name):
    with open(file_name, 'r') as file: 
        lines = [line.strip() for line in file]
        return lines

data = get_data('day1_data.txt')

print(solution_part_one(data))
print(solution_part_two(data))