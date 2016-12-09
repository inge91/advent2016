def splitLine(line):
    segments = []
    bracketSegments = []
    currentString =""
    inBrackets = False
    for character in line:
        if character == "[" or character =="]":
            if len(currentString) > 0:
                if inBrackets:
                    bracketSegments.append(currentString)
                else:
                    segments.append(currentString)
                currentString = ""
            if character == "[":
                inBrackets = True
            else:
                inBrackets = False
        else:
            currentString += character
    if len(currentString) > 0:
        if inBrackets:
            bracketSegments.append(currentString)
        else:
            segments.append(currentString)
    return segments, bracketSegments
                

def checkPattern(pattern, segment):
    for i in range(0, len(segment)-2):
        if pattern[0] == segment[i+1] and pattern[1] == segment[i] and pattern[1] == segment[i+2]:
            return True
    return False

def checkValid(nonbracket, bracket):
    for segment in nonbracket:
        for i in range(0,len(segment)-2):
            if segment[i] == segment[i+2] and segment[i] != segment[i+1]:
                pattern = segment[i:i+3]
                for segmentToCheck in bracket:
                    if checkPattern(pattern, segmentToCheck):
                        return True
    return False

if __name__ == '__main__':
    numCorrect = 0
    with open('inputday7') as f:
        for line in f:
            line = line.rstrip()
            print line
            lineSegments = splitLine(line)
            if checkValid(lineSegments[0], lineSegments[1]):
                numCorrect += 1
    print numCorrect





