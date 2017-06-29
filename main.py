'''
Created on Jun 7, 2017

@author: Alex
'''
import sys, random
dictOne = dict()
sequence = []
limit = 3
def printDict():
    triDict = dictOne.keys() 
    for i in range(len(triDict)):
        print triDict[i], ':', str(dictOne[triDict[i]][0])
        biDict = dictOne[triDict[i]][1].keys()
        for j in range(len(biDict)):
            print '\t', biDict[j], ':', str(dictOne[triDict[i]][1][biDict[j]][0])
            uniDict = dictOne[triDict[i]][1][biDict[j]][1].keys()
            for k in range(len(uniDict)):
                print '\t\t', uniDict[k], ':', str(dictOne[triDict[i]][1][biDict[j]][1][uniDict[k]])
        
        
textFile = ['alice-27.txt', 'doyle-27.txt', 'doyle-case-27.txt', 'london-call-27.txt', 'melville-billy-27.txt', 'twain-adventures-27.txt']
sherlock = ['doyle-27.txt', 'doyle-case-27.txt']
def main(argv):

    global dictOne
    count = 0
    for fileName in sherlock: # for each file in list of files
        with open(fileName, 'r') as openText: #read each file
            for line in openText:   # for line in each file
                for words in line.split():  # split each line by word into a list 
                    count +=1
                    sequence.append(words.lower()) #add words to sequence
                    #print sequence
                    if len(sequence) == limit:
                        if dictOne.has_key(sequence[0]):
                            dictOne[sequence[0]] = (dictOne[sequence[0]][0] + 1, dictOne[sequence[0]][1])
                            if dictOne[sequence[0]][1].has_key(sequence[1]):
                                dictOne[sequence[0]][1][sequence[1]] = (dictOne[sequence[0]][1][sequence[1]][0] + 1, dictOne[sequence[0]][1][sequence[1]][1])
                                if dictOne[sequence[0]][1][sequence[1]][1].has_key(sequence[2]):
                                    dictOne[sequence[0]][1][sequence[1]][1][sequence[2]] + 1
                                else:
                                    dictOne[sequence[0]][1][sequence[1]][1][sequence[2]] = 1
                            else:
                                dictOne[sequence[0]][1][sequence[1]] = (1, dict())
                                dictOne[sequence[0]][1][sequence[1]][1][sequence[2]] = 1
                        else:
                            dictOne[sequence[0]] = (1, dict())
                            dictOne[sequence[0]][1][sequence[1]] = (1, dict())
                            dictOne[sequence[0]][1][sequence[1]][1][sequence[2]] = 1
                        sequence.remove(sequence[0])
                    
                    
    printDict()
    output = []
    position = random.randint(0,count)
    index = -1
    currentWord = ''
    for key in dictOne:
        currentWord = key
        index += 1
        position -= dictOne[key][0]
        if position < 0:
            break
    output.append(currentWord)
    while len(output) < 1000:
        index = -1
        position = random.randint(0,dictOne[output[-1]][0])
        for key in dictOne[output[-1]][1]:
            currentWord = key
            index += 1
            position -= dictOne[output[-1]][1][key][0]
            if position < 0:
                break
        output.append(currentWord)
        if len(output) == 1000: break
        for key in dictOne[output[-2]][1][output[-1]][1]:
            currentWord = key
            index += 1
            position -= dictOne[output[-2]][1][output[-1]][1][key]
            if position < 0:
                break
        output.append(currentWord)

    with open("sherlock.txt", "w") as outfile:
        for word in output:
            outfile.write(word + ' ')
    
                            
    '''              
                d = {}
                ({'word1':(occurences1, {'word2':(occurences2,{'word3":'occurences3'})})})
                dict1[word1][1][word1]
    '''
                                    
if __name__ == "__main__":
    main(sys.argv[1:])                              
                                    
                                    
                                    
                                    
                                    
                                    
                                    