

if __name__ == "__main__":
    numbers = 0
    with open("inputday4") as f:
        for line in f:
            line = line.rstrip()
            code = line.rsplit("-")
            doorID = int(code[-1][:-7])
            doorID = doorID % 26
            code = code[:-1]
            for i in range(0,len(code)):
                for j in range(0, len(code[i])):
                    letterCode =  ord(code[i][j]) 
                    letterCode += doorID
                    if letterCode > 122:
                        letterCode = 96 + letterCode % 122
                    newWord = code[i][:j] + chr(letterCode) + code[i][j+1:]
                    code[i] =newWord
            if 'northpole' in code:
                print code
                print doorID
                print line



def part1():
    numbers = 0
    with open("inputday4") as f:
        for line in f:
            line = line.rstrip()
            code = line.rsplit("-")
            doorN = int(code[-1][:-7])
            checksum = code[-1][-6:-1]
            allLetters = ""
            for i in range(0, len(code)-1):
                allLetters += code[i]
            allLetters = list(allLetters)
            occurences = {}
            for i in allLetters:
                v = occurences.get(i, 0)
                occurences[i] = v+1
            countsList = []
            for key in occurences.keys():
                countsList.append((key,occurences[key]))
            countsList = sorted(countsList, key=lambda x: x[0])
            countsList = sorted(countsList, key=lambda x: x[1], reverse=True)
            countsList = countsList[:5]
            grChecksum = ""
            countsList = [ x[0] for x in countsList]
            for i in countsList:
                grChecksum += i

            if grChecksum == checksum:
                numbers += doorN
    print numbers

        
            
