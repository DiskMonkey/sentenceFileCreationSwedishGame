import os
import codecs

numFiles = 0
directoryList = os.listdir('./generatedSentenceFiles')

for entry in directoryList:
    numFiles += 1

originalFile = open("meningar.txt", "r")
originalList = []

for line in originalFile:
    originalList.append(line.strip())

originalFile.close()

newFileName = "./generatedSentenceFiles/sentenceFile" + str(numFiles) + ".txt"

newFile = open(newFileName, 'w', encoding='cp1252')

spanishFile = open("./spanishData.txt", 'r', encoding='utf-8')
# spanishFile.readline()
spanishFileList = []
for line in spanishFile:
    spanishFileList.append(line.strip().split(',')) # need to work on randomization
spanishFileListIndex = 0

levelSentCount = 0
levelCount = 1

condition1 = True # true means cond 1, and false is cond 2
for line in originalList:
    try:
        spanishFileListIndex += 1
        spanishList = spanishFileList[spanishFileListIndex]
    except:
        print("Done with spanish file")
        break

    lineList = line.split(',')

    lineList[1] = "1"
    lineList[2] = spanishList[0] + ".wav"
    lineList[3] = "0"
    lineList[4] = "0"
    lineList[5] = "1"

    if (levelSentCount == 16):
        levelCount += 1
        levelSentCount = 1
        lineList[6] = str(levelCount)
    else:
        levelSentCount += 1
        lineList[6] = str(levelCount)

    lineList[7] = spanishList[3]

    if (condition1):
        lineList[8] = spanishFileList[spanishFileListIndex + 1][3]
    else:
        lineList[8] = spanishFileList[spanishFileListIndex - 1][3]

    condition1 = not condition1

    lineList[9] =
    lineList[10] = " "
    lineList[11] = spanishList[1]

    remakeString = ""
    for elem in lineList:
        remakeString += elem + ","
    remakeString = remakeString[:-1] + "\n"

    newFile.write(remakeString)

