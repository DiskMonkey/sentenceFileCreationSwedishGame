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

for line in originalList:
    lineList = line.split(',')

    lineList[2] = "Example.ogg"
    lineList[7] = "RightSuffix"
    lineList[8] = "WrongSuffix"
    lineList[10] = "PrefixPartFull"
    lineList[11] = "FullText"

    remakeString = ""
    for elem in lineList:
        remakeString += elem + ","
    remakeString = remakeString[:-1] + "\n"

    newFile.write(remakeString)

