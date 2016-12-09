
if __name__ == "__main__":
    newline = ''
    with open("inputday9") as f:
        for line in f:
            line = line.rstrip()
            i = 0
            while i < len(line):
                character = line[i]
                if character ==" ":
                    i+=1
                elif character  == "(":
                    xindex = i + line[i:].find('x')
                    closeIndex = xindex + line[xindex:].find(')')
                    amount= int(line[i+1:xindex])
                    repeat= int(line[xindex+1:closeIndex])
                    newline += line[closeIndex+1: closeIndex + amount+1] * repeat
                    i = closeIndex + amount + 1
                    
                else:
                    print character
                    newline += character
                    i+=1
    count = 0
    print len(newline)

