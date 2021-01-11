import dictionary as dic 
from treelib import Node, Tree

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

        if i == len(input)-1 and tempIndexes!=[]:
            tempIndexes.append(i)
            tableOfProperIndexes.append(tempIndexes)

    return tableOfProperIndexes
            

def findRoot(tableofIndexes, input, maxPriority, dictionary):
    indexOfRoot = -1
    keyofRoot=""
    valueForRoot =""
    for priority in range(maxPriority+1):
        for t in tableofIndexes:
            for key,value in dictionary.items():
                if value[3]==str(priority):
                    maybeRoot=input[t[0]:t[1]].find(value[1])
                    if maybeRoot != -1:
                        if(indexOfRoot == -1 or indexOfRoot>maybeRoot+t[0]):
                            indexOfRoot = maybeRoot+t[0]
                            keyofRoot = key
                            valueForRoot = value[1]
        if(indexOfRoot!=-1):
            return [indexOfRoot,keyofRoot,valueForRoot]


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

def findEndIndexOfActualBracket(openIndex, input):
    openBrackets =1
    
    for i in range(openIndex+1,len(input)+1):
        if input[i]=='{':
            print('otwieram')
            openBrackets +=1
        if input[i] == '}':
            print('zamykam')
            openBrackets -=1
        if openBrackets ==0:
            return i

def findChilds(inputString,root):
    if root[1] in dic.teXChildsWithoutBrackets:
        left = inputString[0:root[0]]
        right = inputString[root[0]+len(root[2]):]
    if root[1] in dic.teXChildsWithBrackets:
        endOfFirst = findEndIndexOfActualBracket(root[0]+len(root[2]),inputString)
        endOfSecond = findEndIndexOfActualBracket(endOfFirst+1,inputString)
        left=inputString[root[0]+1+len(root[2]):endOfFirst]
        right=inputString[endOfFirst+2:endOfSecond]
        print(endOfFirst)
        print(endOfSecond)
    if root[1] in dic.teXChildsWithRightBracket:
        endOfBracket = findEndIndexOfActualBracket
        left = inputString[:root[0]]
        right = inputString[root[0]+2:-1]
    if root[1] in dic.teXChildWithBracket:
        left=inputString[root[0]+len(root[2])+1:-1]
        right = None
    return [left,right]

def findNextSubtree(inputString,maxPriority,dictionary,tree, rootName,parent):

    root = findRoot(findProperFragments(inputString),inputString,maxPriority,dictionary)    
    left = findChilds(inputString,root)[0]
    right = findChilds(inputString,root)[1]    
    
    if root != None:
        if parent== '':
            tree.create_node(root[1],rootName)
            print('root: ' +root[1])
        else:
            tree.create_node(root[1],rootName,parent=parent)
            print(rootName+': '+root[1])
        
        try:
            findNextSubtree(left,maxPriority,dictionary,tree,rootName+'.left',rootName)
            print(rootName+'.left: '+left)
        except:
            tree.create_node(left,rootName+'.left',parent=rootName)
        try:
            print(rootName+'.right: '+right)
            findNextSubtree(right,maxPriority,dictionary,tree,rootName+'.right',rootName)
        except:
            if right !=None:
                tree.create_node(right,rootName+'.right',parent=rootName)
            else:
                tree.create_node('None',rootName+'.right',parent=rootName)
    return tree

    

def textToTree(inputString):
    tree = Tree()
    dictionary = dic.symbols
    inputString = inputString.replace(" ","")
    inputString = inputString.replace("\n","")
    maxPriority = dic.findMaxPriority(dictionary)
    inputString = addMultiplySign(inputString,dictionary)
    
    # root returns [indexOfRoot,keyofRoot,valueForRoot]
    tree = findNextSubtree(inputString,maxPriority,dictionary,tree,'root','')

  

    


    tree.show()




input = '\sqrt{b^{2}-4ac}+5ab' #Pamiętać, żeby naprawić kwestię -b-4ac

textToTree(input)

