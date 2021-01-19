import dictionary as dic 
from treelib import Node, Tree

def isWholeInBracket(input):
    openBrackets=1
    if input[0]=='{' and input[len(input)-1]=='}':
        for i in range(1,len(input)):
            if input[i]=='{':
                openBrackets+=1
            if input[i]=='}':
                openBrackets-=1
            if openBrackets == 0 and i<len(input)-1:
                return False

        if openBrackets==0:
            return True
        else:
            return False
    else:
        return False
    

def modifyNegativePhrases(input):
    output=''
    IndexOfNextStart=0
    
    for i in range(len(input)):
        if input[i]=="-":
            if i-1==-1 or input[i-1]=="(" or input[i-1]=="{":
                output+=input[IndexOfNextStart:i]+'[minus]'
                IndexOfNextStart = i+1
    
    if IndexOfNextStart< len(input):
        output += input[IndexOfNextStart:]

    return output



    
def findProperFragments(input):
    openBrackets = 0
    isSomeCurlyBracketOpen = False
    tableOfProperIndexes = []
    tempIndexes = []

    for i in range(len(input)):

        if tempIndexes==[] and isSomeCurlyBracketOpen==False and input[i]!='{':
            tempIndexes.append(i)
        
        if input[i] == '{':
            if openBrackets == 0:
                isSomeCurlyBracketOpen = True
                if tempIndexes !=[]:
                    tempIndexes.append(i)
                    tableOfProperIndexes.append(tempIndexes)
                    tempIndexes = []
            openBrackets += 1
        if input[i] == '}':
            openBrackets -= 1
            if openBrackets==0:
                isSomeCurlyBracketOpen =False

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


def addMultiplySign(input,dictionary,listtOfKeys):
    previousIsNotEmpty = False
    isPreviousASymbol = False
    output=""
    indexOfNextStart = 0


    changedString = input.replace('{'," ")
    changedString = changedString.replace('}'," ")
    for value in dictionary.values():
        if value[1] not in listtOfKeys:
            changedString = changedString.replace(value[1], " "*len(value[1]))
        else:
            changedString = changedString.replace(value[1], "\\"+" "*(len(value[1])-1))

    for i in range(len(changedString)):
        if changedString[i] == ' ':
            previousIsNotEmpty = False
            continue
        if previousIsNotEmpty:
            if isPreviousASymbol and (changedString[i]=="\\" or changedString[i]!=')') and changedString[i-1]!='(':
                output +=  input[indexOfNextStart:i] + '\cdot'
                indexOfNextStart = i
            else:
                if changedString[i] not in dic.numbers and(changedString[i]=="\\" or changedString[i]!=')') and changedString[i-1]!='(':
                    output +=  input[indexOfNextStart:i] + '\cdot'
                    indexOfNextStart = i
            
        else:
            previousIsNotEmpty = True

        if changedString[i] not in dic.numbers and changedString[i]!='(':
            isPreviousASymbol = True
        else:
            isPreviousASymbol = False
    
    if indexOfNextStart < len(input):
        output += input[indexOfNextStart:]
    

    return output

def findEndIndexOfActualCurlyBracket(openIndex, input):
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
        endOfFirst = findEndIndexOfActualCurlyBracket(root[0]+len(root[2]),inputString)
        endOfSecond = findEndIndexOfActualCurlyBracket(endOfFirst+1,inputString)
        left=inputString[root[0]+1+len(root[2]):endOfFirst]
        right=inputString[endOfFirst+2:endOfSecond]
    if root[1] in dic.teXChildsWithRightBracket:
        endOfBracket = findEndIndexOfActualCurlyBracket
        left = inputString[:root[0]]
        right = inputString[root[0]+2:-1]
    if root[1] in dic.teXChildWithBracket:
        left=inputString[root[0]+len(root[2])+1:-1]
        right = None
    if root[1] in dic.teXFunctions:
        left = inputString[root[0]+len(root[2]):]
        right = None
    if root[1] in dic.teXJustSymbols:
        left=None
        right = None
    return [left,right]

def findNextSubtree(inputString,maxPriority,dictionary,tree, rootName,parent):
    if isWholeInBracket(inputString):
        if parent == '':
            root = tree.create_node('(',rootName)
        else:
            root = tree.create_node('(',rootName,parent=parent)
            tree.create_node("None",rootName+'.right',parent=rootName)
        left = inputString[1:len(inputString)-1]
        try:
           findNextSubtree(left,maxPriority,dictionary,tree,rootName+'.left',rootName)
        except:
            tree.create_node(left,rootName+'.left',parent=rootName)

    else:    
        root = findRoot(findProperFragments(inputString),inputString,maxPriority,dictionary)    
        left = findChilds(inputString,root)[0]
        right = findChilds(inputString,root)[1]    
        
        if root != None:
            if parent== '':
                tree.create_node(root[1],rootName)
            else:
                tree.create_node(root[1],rootName,parent=parent)
            
            try:
                findNextSubtree(left,maxPriority,dictionary,tree,rootName+'.left',rootName)
            except:
                tree.create_node(left,rootName+'.left',parent=rootName)
            try:
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
    inputString = addMultiplySign(inputString,dictionary,dic.TexsymbolsWithUndercoverMultiplySign)
    inputString = modifyNegativePhrases(inputString)
    inputString = inputString.replace("(",'{')
    inputString = inputString.replace(')','}') 
    print(inputString)
    # root returns [indexOfRoot,keyofRoot,valueForRoot]
    tree = findNextSubtree(inputString,maxPriority,dictionary,tree,'root','')
  
    tree.show()
