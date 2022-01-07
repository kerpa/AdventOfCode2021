with open('input.txt') as f:
    lines = f.read().splitlines()

numbers = lines[0].split(',')
boards = []

for i in range(2, len(lines), 6):
	boards.append([line.split() for line in lines[i:i+5]])

print(boards)