import os

folder = './Joan Cut Audio Files'
directoryList = os.listdir(folder)

for file in directoryList:
    audioFile = folder + "/" + file
    print(audioFile)
