
def recursive_decompress(line):
    newline = ""
    i = 0
    while i < len(line):
        character = line[i]
        if character ==" ":
            i+=1
        elif character  == "(":
            xindex = i + line[i:].find('x')
            closeindex = xindex + line[xindex:].find(')')
            amount= int(line[i+1:xindex])
            repeat= int(line[xindex+1:closeindex])
            newline += recursive_decompress(line[closeindex+1: closeindex + amount+1] *
                    repeat)
            i = closeindex + amount + 1
            
        else:
            newline += character
            i+=1
    return newline

def alternative(line):
    multiplier = 0
    i = 0
    while i < len(line):
        character = line[i]
        if character ==" ":
            i+=1
        elif character  == "(":
            xindex = i + line[i:].find('x')
            closeindex = xindex + line[xindex:].find(')')
            amount= int(line[i+1:xindex])
            repeat= int(line[xindex+1:closeindex])
            if "(" not in line[closeindex+1: closeindex + amount+1] * repeat:
                print amount*repeat
                multiplier +=  amount * repeat
            else:
                print repeat * alternative(line[closeindex+1: closeindex + amount+1])
                multiplier += repeat * alternative(line[closeindex+1: closeindex + amount+1])
            i = closeindex + amount + 1
        else:
            i+=1
    return multiplier

def notMultiplied(line):
    i = 0
    count = 0
    while i < len(line):
        character = line[i]
        if character ==" ":
            i+=1
        elif character  == "(":
            xindex = i + line[i:].find('x')
            closeIndex = xindex + line[xindex:].find(')')
            amount= int(line[i+1:xindex])
            repeat= int(line[xindex+1:closeIndex])
            i = closeIndex + amount + 1
        else:
            i+=1
            count +=1
    return count


if __name__ == "__main__":
    newline = ''
    with open("inputday9") as f:
        for line in f:
            line = line.rstrip()
            v = alternative(line)
            v += notMultiplied(line)

    print v

