inFile = open("meningar.txt", 'r')

outFiles = []

numFiles = 12

for i in range(numFiles):
    outFile = open("./output/" + str(i) + ".txt", 'w')
    outFiles.append(outFile)

for lineObject in inFile:
    line = inFile.readline().strip()

    lineList = line.split(',')

    for i in range(numFiles):
        outFiles[i].write(lineList[i] + "\n")

inFile.close()

for i in range(numFiles):
    outFiles[i].close()