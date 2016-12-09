import md5
import re
if __name__ == "__main__":
    doorID ="cxdnnyjw"
    i = 0
    code = 8 * ['NaN']
    while True:
        hashable = doorID +str(i)
        hashValue = md5.new(hashable).hexdigest()
        hashValue = str(hashValue)
        if hashValue.startswith('00000'):
            if hashValue[5].isdigit():
                loc = int(hashValue[5])
                if loc < 8:
                    if 'NaN' in code[loc]:
                        code[loc] = hashValue[6]
                    if 'NaN' not in code:
                        break
                    print code 
        i+=1
    print code



def part1():
    doorID ="cxdnnyjw"
    i = 0
    code = ''
    while True:
        hashable = doorID +str(i)
        hashValue = md5.new(hashable).hexdigest()
        hashValue = str(hashValue)
        if hashValue.startswith('00000'):
            code += hashValue[5]
            print code
            if len(code) == 8:
                break
        i+=1
    print code


