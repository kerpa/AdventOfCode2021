import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

with open('input.txt') as f:
    crab_list = f.read().split(',')

crab_list = [int(i) for i in crab_list]
crab_list = np.array(crab_list)

# plot histogram
plt.hist(crab_list, bins=100)
plt.show()


# find the distance of each element from a possible value
def find_distance(crab_list, value):
    distance = np.abs(crab_list - value)
    return distance


# find crab_thrust
def find_crab_thrust(crab_list, value):
    distance = find_distance(crab_list, value)
    return np.sum(distance)


# find the minimum distance thrust
def find_min_distance_thrust(crab_list):
    eval_value = []
    for i in range(len(crab_list)):
        print(find_crab_thrust(crab_list, i))
        eval_value.append(find_crab_thrust(crab_list, i))
        if eval_value[i] > eval_value[i - 1]:
            break
    return i-1

list_value = np.linspace(300, 320, 100)
list_thrust = []
for i in list_value:
    list_thrust.append(find_crab_thrust(crab_list, i))

plt.plot(list_value, list_thrust)
plt.show()

print(min(list_thrust))