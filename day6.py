import operator
if __name__ == "__main__":
    maxOccurences = []
    maxValues = []
    with open('inputday6') as f:
        for line in f:
            line = line.rstrip()
            for i, character in enumerate(line):
                if len(maxOccurences) < len(line):
                    d = {character: 1}
                    maxOccurences.append(d)
                else:
                    amount = maxOccurences[i].get(character, 0)
                    amount += 1
                    maxOccurences[i][character] = amount
        for maxOccurence in maxOccurences:
            maxValue = 999999
            maxCharacter = 'a'
            for key in maxOccurence.keys():
                if maxOccurence[key] < maxValue:
                    maxValue = maxOccurence[key]
                    maxCharacter = key

            print "max: " + maxCharacter,


                    
                

