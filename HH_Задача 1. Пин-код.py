d = {'0': ['0', '8'],
     '1': ['1', '2', '4'],
     '2': ['1', '2', '3', '5'],
     '3': ['2', '3', '6'],
     '4': ['1', '4', '5', '7'],
     '5': ['2', '4', '5', '6', '8'],
     '6': ['3', '5', '6', '9'],
     '7': ['4', '7', '8'],
     '8': ['0', '5', '7', '8', '9'],
     '9': ['6', '8', '9'],
     }

pinStart = input()
pinInd = [0 for i in pinStart] # создать нулевой массив длины pinStart
itOfPinInd = len(pinInd) - 1
while pinInd[0] < len(d[pinStart[0]]):
    for i in range(len(pinInd)):
        print(d[pinStart[i]][pinInd[i]], end='')
    while (itOfPinInd >= 0):
        if pinInd[itOfPinInd] + 1 == len(d[pinStart[itOfPinInd]]):
            itOfPinInd -= 1
        else:
            pinInd[itOfPinInd] += 1
            for i in range(itOfPinInd + 1, len(pinInd)):
                pinInd[i] = 0
            itOfPinInd = len(pinInd) - 1
            break
    else:
        break
    print(',', end='')