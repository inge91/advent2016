

def splitLine(line):
    segments = []
    currentString =""
    inBrackets = False
    for character in line:
        if character == "[" or character =="]":
            if len(currentString) > 0:
                segments.append((currentString, inBrackets))
                currentString = ""
            if character == "[":
                inBrackets = True
            else:
                inBrackets = False
        else:
            currentString += character
    if len(currentString) > 0:
        segments.append((currentString, inBrackets))
    return segments
                

def checkValid(lineSegments):
    valid = False
    for segment, inBrackets in lineSegments:
        for i in range(0,len(segment)-3):
           if segment[i] == segment[i+3] and segment[i+1] == segment[i+2] and segment[i] != segment[i+1]:
               if inBrackets:
                   return False
               else:
                   valid = True
    return valid

if __name__ == '__main__':
    numCorrect = 0
    with open('inputday7') as f:
        for line in f:
            line = line.rstrip()
            print line
            lineSegments = splitLine(line)
            if checkValid(lineSegments):
                numCorrect += 1
    print numCorrect





