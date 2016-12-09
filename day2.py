from enum import Enum

class Direction(Enum):
    Up = 1
    Down = 2
    Left = 3
    Right = 4

position = [0,0]

def part1move(direction):
    if direction == Direction.Up:
        position[1] = max(-1, position[1]-1)
    if direction == Direction.Down:
        position[1] = min(1, position[1]+1)
    if direction == Direction.Left:
        position[0] = max(-1, position[0]-1)
    if direction == Direction.Right:
        position[0] = min(1, position[0]+1)

def part1getNumberAtLocation():
    if position == [0, 0]:
        return 5
    elif position == [1,0]:
        return 6
    elif position == [-1,0]:
        return 4
    elif position == [1,1]:
        return 9
    elif position == [-1,1]:
        return 7
    elif position == [1,-1]:
        return 3
    elif position == [-1,-1]:
        return 1
    elif position == [0,-1]:
        return 2
    elif position == [0,1]:
        return 8

def part2getNumberAtLocation():
    if position == [0, 0]:
        return '7'
    elif position == [1,0]:
        return '8'
    elif position == [-1,0]:
        return '6'
    elif position == [1,1]:
        return 'C'
    elif position == [-1,1]:
        return 'A'
    elif position == [1,-1]:
        return '4'
    elif position == [-1,-1]:
        return '2'
    elif position == [0,-1]:
        return '3'
    elif position == [0,1]:
        return 'B'
    elif position == [-2, 0]:
        return 'A'
    elif position == [2, 0]:
        return '9'
    elif position == [0, -2]:
        return '1'
    elif position == [0, 2]:
        return 'D'

def part2move(direction):
    if direction == Direction.Up:
        if position[0] == 0:
            position[1] = max(-2, position[1]-1)
        elif abs(position[0]) == 2:
            pass
        else:
            position[1] = max(-1, position[1]-1)
    if direction == Direction.Down:
        if position[0] == 0:
            position[1] = min(2, position[1]+1)
        elif abs(position[0]) == 2:
            pass
        else:
            position[1] = min(1, position[1]+1)
    if direction == Direction.Left:
        if position[1] == 0:
            position[0] = max(-2, position[0]-1)
        elif abs(position[1]) == 2:
            pass
        else:
            position[0] = max(-1, position[0]-1)

    if direction == Direction.Right:
        if position[1] == 0:
            position[0] = min(2, position[0]+1)
        elif abs(position[1]) == 2:
            pass
        else:
            position[0] = min(1, position[0]+1)



if __name__ == "__main__":
    with open('inputday2-1') as f:
        for line in f:
            for character in line:
                if character == "U":
                    part2move(Direction.Up)
                elif character == "D":
                    part2move(Direction.Down)
                elif character == "L":
                    part2move(Direction.Left)
                elif character == "R":
                    part2move(Direction.Right)
            n = part2getNumberAtLocation()
            print n,
    
    

    
