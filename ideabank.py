import sys
import os
from os import path                 

def writeIdeaToAFile(index, idea):
    with open('ideas.txt', 'a') as saveIdea:
        saveIdea.write(str(index) + '. ' + idea + '\n')

def readIdeaFromAFile():
    with open('ideas.txt', 'r') as readIdea:  
        ideaContent = readIdea.read()

def lastIndexFromAFile():
    with open('ideas.txt', 'r') as readIdea:
        lastLine = (list(readIdea)[-1])
        splitLine = lastLine.split('.')
        lastIndex = int(splitLine[0])
        return lastIndex

def isFileExcist():
    if(path.exists('ideas.txt')):
        ideaIndex = lastIndexFromAFile()
    else:
        ideaIndex = 0
    return ideaIndex

ideaIndex = isFileExcist()
listOfIdeas = []

for arg in sys.argv:
    if(arg == '--list' and len(sys.argv) == 2):
        with open('ideas.txt', 'r') as readIdea: 
            print(readIdea.read())
            exit()
    elif(arg == '--delete' and len(sys.argv) == 2):
        print('Specify a number after --delete')
        exit()
    elif(arg == '--delete' and len(sys.argv) > 2):
        try:
            indexOfItemToDelete = int(sys.argv[2])
            readIdeaList = []
            writeIdeaList = []
            with open('ideas.txt', 'r') as readIdea:
                for line in readIdea:
                    data = line.split(" ")
                    readIdeaList.append(line)
                for index, item in enumerate(readIdeaList):
                    if(item.startswith(str(indexOfItemToDelete))):
                        deletedIdea = readIdeaList.pop(index)
                        print("Idea deleted from a list: %s" % deletedIdea)
                for index, idea in enumerate(readIdeaList, start= 0):
                        readIdeaList[index] = idea.split(' ')
                        writeIdeaList.append(readIdeaList[index][1])
            with open('ideas.txt', 'w') as writeIdea:
                for index, line in enumerate(writeIdeaList, start=0):
                    writeIdea.write('%d. %s' % (index + 1, writeIdeaList[index]))
                    writeIdea.truncate()
            exit()
        except ValueError:
            print('Specify a number after --delete')
            exit()    
       

while(True):
    userIdea = input('What is your new idea?')
    listOfIdeas.append(userIdea)
    ideaIndex += 1
    writeIdeaToAFile(ideaIndex, userIdea)

    for index, idea in enumerate(listOfIdeas, start=1):
        print('%d. %s' % (index, idea))

