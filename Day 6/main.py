

def one_day_passing(list_of_fishes):

    for fish in range(len(list_of_fishes)):
        if list_of_fishes[fish] == 0:
            list_of_fishes[fish] = 7
            list_of_fishes.append(8)
        list_of_fishes[fish] -= 1


    return list_of_fishes


def day_passing(list_of_fishes, days):

    for i in range(days):
        list_of_fishes = one_day_passing(list_of_fishes)
        #print('day:', i+1, '  ',list_of_fishes)
        if i == days-1:
            length = len(list_of_fishes)
            print(f"there is {length} fishes ")

    return list_of_fishes

with open('input.txt') as f:
    shoal_of_fishes = f.read().split(',')
shoal_of_fishes = [int(i) for i in shoal_of_fishes]

day_passing(shoal_of_fishes, 256)