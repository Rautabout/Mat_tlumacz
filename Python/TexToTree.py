import Dictionary as dic 
from binarytree import Node

# def findNewRoot():

    
def findProperFragments(input):
    openBrackets = 0
    isSomeBracketOpen = False
    tableOfProperIndexes = []
    tempIndexes = []

    for i in range(len(input)):

        if tempIndexes==[] and isSomeBracketOpen==False and input[i]!='{':
            tempIndexes.append(i)
        
        if input[i] == '{':
            if openBrackets == 0:
                isSomeBracketOpen = True
                if tempIndexes !=[]:
                    tempIndexes.append(i)
                    tableOfProperIndexes.append(tempIndexes)
                    tempIndexes = []
            openBrackets += 1
        if input[i] == '}':
            openBrackets -= 1
            if openBrackets==0:
                isSomeBracketOpen =False

        
        
    return tableOfProperIndexes
            

def findRoot(tableofIndexes, input, maxPriority, dictionary):
    indexOfRoot = -1
    keyofRoot=""
    for t in tableofIndexes:
        for priority in range(maxPriority+1):
            for key,value in dictionary.items():
                if value[3]==str(priority):
                    maybeRoot=input[t[0]:t[1]].find(value[1])
                    if maybeRoot != -1:
                        if(indexOfRoot == -1 or indexOfRoot>maybeRoot):
                            indexOfRoot = maybeRoot
                            keyofRoot = key
        if(indexOfRoot!=-1):
            return [indexOfRoot,keyofRoot]


def addMultiplySign(input,dictionary):
    previousIsNotEmpty = False
    isPreviousASymbol = False
    output=""
    indexOfNextStart = 0


    changedString = input.replace('{'," ")
    changedString = changedString.replace('}'," ")
    for value in dictionary.values():
        changedString = changedString.replace(value[1], " "*len(value[1]))
    
    for i in range(len(changedString)):
        if changedString[i] == ' ':
            previousIsNotEmpty = False
            continue
        if previousIsNotEmpty:
            if isPreviousASymbol:
                output +=  input[indexOfNextStart:i] + '\cdot'
                indexOfNextStart = i
            else:
                if changedString[i] not in dic.numbers:
                    output +=  input[indexOfNextStart:i] + '\cdot'
                    indexOfNextStart = i
            
        else:
            previousIsNotEmpty = True

        if changedString[i] not in dic.numbers:
            isPreviousASymbol = True
        else:
            isPreviousASymbol = False
    
    if indexOfNextStart < len(input):
        output += input[indexOfNextStart:]
    

    return output

def textToTree(input):
    input = input.replace(" ","")
    input = input.replace("\n","")
    maxPriority = dic.findMaxPriority(dic.symbols)
    print(findRoot(findProperFragments(input),input,maxPriority,dic.symbols))

    


input = '275a-\\frac{-b-\sqrt{b^{2}-4ac}}{2abc}+5^{454}'

print(addMultiplySign(input, dic.symbols))
