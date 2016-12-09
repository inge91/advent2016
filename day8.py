import numpy as np

if __name__ == "__main__":
    display = np.chararray((6, 50))
    display[:] = "."
    with open('inputday8') as f:
        for line in f:
            line = line.rstrip()
            command = line.split(" ")
            if command[0] == "rect":
                size = command[1].split('x')
                for row in range(0, int(size[1])):
                    width = int(size[0])
                    display[row,0:width] = "#"
            if command[0] == "rotate":
                amount = int(command[-1])
                index = int(command[2][2:])
                oldDisplay = display.copy()
                if "row" in command:
                    for i in range(0, 50):
                        display[index, i] = oldDisplay[index, i - amount % 50]
                if "column" in command:
                    for i in range(0, 6):
                        display[i, index] = oldDisplay[i - amount % 50, index]

            print display
    count = 0
    for i in range(0, 6):
        for j in range(0, 50):
            if display[i, j] == "#":
                print "#",
                count += 1
            else:
                print ".",
        print ""
                    
    print count

                


                        



