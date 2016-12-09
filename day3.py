


if __name__ == '__main__':
    possible = 0
    numbers = []
    with open("inputday3-2") as f:
        for line in f:
            line = line.rstrip()
            numbers.append(int(line))
            if len(numbers) == 3:
                numbers.sort()
                if numbers[0] + numbers[1] > numbers[2]:
                    possible += 1
                numbers = []
    print possible


def part1():
    possible = 0
    with open("inputday3-1") as f:
        for line in f:
            line = line.rstrip()
            line = line.split(' ')
            numbers = [int(x) for x in line if x.isdigit()]
            numbers.sort()
            if numbers[0] + numbers[1] > numbers[2]:
                possible += 1


    print possible
