data = [open("/Users/jeancloarec/Documents/GitHub/AdventOfCode2021/Day 6/input.txt")
            .read().count(str(i)) for i in range(0, 9)]
print(data)
for day in range(256):
    data[(day + 7) % 9] += data[day % 9]
print(data)
print(sum(data))