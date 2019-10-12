import sys
from functions import func

arguments = sys.argv
inputFileName = arguments[1]
outputFileName = arguments[2]

runtimes = 0
# print(inputFileName, outputFileName)

# Brutal Force method
def BF(rX1, rX2, rY1, rY2):
    BFmin = func(rX1, rY1)
    runtimes = 0
    for x in range(rX1, rX2+1):
        for y in range(rY1, rY2+1):
            runtimes+=1
            if BFmin > func(x, y):
                BFmin = func(x, y)
    roundBF = round(BFmin,3)
    print("%.3f"%roundBF, "    times: ", runtimes)
    exportOutput(roundBF)
    return

# Hill Climbing method
def HC(rX1, rX2, rY1, rY2, iX, iY):
    HCmin = func(iX, iY)
    stepSize = 1
    runtimes = 1
    while True:
        direction = 0
        if iX+stepSize <= rX2 and iX+stepSize >= rX1:     # X+1
            runtimes+=1
            if HCmin > func(iX+stepSize, iY):
                HCmin = func(iX+stepSize, iY)
                direction = 1
        if iX-stepSize <= rX2 and iX-stepSize >= rX1:     # X-1
            runtimes+=1
            if HCmin > func(iX-stepSize, iY):
                HCmin = func(iX-stepSize, iY)
                direction = 2
        if iY+stepSize <= rY2 and iY+stepSize >= rY1:     # Y+1
            runtimes+=1
            if HCmin > func(iX, iY+stepSize):
                HCmin = func(iX, iY+stepSize)
                direction = 3
        if iY-stepSize <= rY2 and iY-stepSize >= rY1:     # Y-1
            runtimes+=1
            if HCmin > func(iX, iY-stepSize):
                HCmin = func(iX, iY-stepSize)
                direction = 4
        
        if direction == 0:
            roundHC = round(HCmin,3)
            print("%.3f"%roundHC, "    times: ", runtimes)
            exportOutput(roundHC)
            break
        else:
            if direction == 1:
                iX = iX+stepSize
            elif direction == 2:
                iX = iX-stepSize
            elif direction == 3:
                iY = iY+stepSize
            elif direction == 4:
                iY = iY-stepSize
    return

def exportOutput(data):
    outputF.write("%.3f\n"%data)
    return


# main function
inputF = open(inputFileName, 'r')
outputF = open(outputFileName, 'w')
doTask = 1
for line in inputF.readlines():
    if doTask == 1:         # get X range
        rX1 = int(line.split(",")[0].strip())
        rX2 = int(line.split(",")[1].strip())
        doTask+=1
        # print(rX1, rX2)
    elif doTask == 2:       # get Y range
        rY1 = int(line.split(",")[0].strip())
        rY2 = int(line.split(",")[1].strip())
        doTask+=1
        # print(rY1, rY2)
        BF(rX1, rX2, rY1, rY2)
    elif doTask == 3:       # get total initial point  
        totalInitPoint = int(line.strip())
        doTask+=1
        # print(totalInitPoint)
    else:                   # get each initial point and do HC
        initX = int(line.split(",")[0].strip())
        initY = int(line.split(",")[1].strip())
        # print(initX, initY)
        HC(rX1, rX2, rY1, rY2, initX, initY)

inputF.close()
outputF.close()