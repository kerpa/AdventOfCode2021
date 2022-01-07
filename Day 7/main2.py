import numpy as np
import matplotlib.pyplot as plt


with open('input.txt') as f:
    crab_list = f.read().split(',')

crab_list = [int(i) for i in crab_list]
crab_list = np.array(crab_list)

def get_arithmetic_sum(n):
    return int(n * (n + 1) / 2)

# find the minimum distance thrust
def get_distance(list,value):
    distance = 0
    for i in range(len(list)):
        distance += get_arithmetic_sum(abs(list[i] - value))
    return distance

list_thrust = []
for i in crab_list:
    list_thrust.append(get_distance(crab_list, i))

print(min(list_thrust))