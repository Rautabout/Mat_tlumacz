import dictionary as dic 
from treelib import Node, Tree


def changeEndingBracket(iteretorStart, iteratorEnd, inputString):
    openBrackets = 0
    for j in range(iteretorStart+1,iteratorEnd):
        if (inputString[j]=='('):
            openBrackets+=1
        elif (inputString[j]==')'):
            if openBrackets==0:
                inputString = inputString[0:j] +' }' +  inputString[j+1:iteratorEnd]
                break
            else:
                 openBrackets-=1
    return inputString

def changeStartingBracket(iteretorStart,iteratorEnd, inputString):
    openBrackets = 0
    for j in range(iteretorStart,0,-1):
        if (inputString[j]==')'):
            openBrackets+=1
        elif (inputString[j]=='('):
            if openBrackets==0:
                inputString = inputString[0:j] +'{' +  inputString[j+1:iteratorEnd]
                break
            else:
                 openBrackets-=1
    return inputString


def testPrepareText(input):
    inputString = input.replace("\n","")
    inputString += " "
    tempString = inputString

    for sign in dic.teXChildsWithRightBracket:
        tempString = inputString
        while (tempString.find(sign)!=-1):

            indexOfSign = tempString.find(sign)
            shift = len(inputString) - len(tempString)
            indexOfSign+=shift  

            if inputString[indexOfSign+1] == '(':
                inputString = inputString[0: indexOfSign+1] + '{' +  inputString[ indexOfSign+2:len(inputString)]
                inputString = changeEndingBracket(indexOfSign, len(inputString), inputString)
            else:
                inputString = inputString[0:indexOfSign+1] + '{' +  inputString[indexOfSign+1:len(inputString)]
                for j in range(indexOfSign+1,len(inputString)+1):
                    if (inputString[j]==' '):
                        inputString = inputString[0:j] +' }' +  inputString[j+1:len(inputString)]
                        break
            
            tempString = inputString[indexOfSign+1:len(inputString)]


    tempString = inputString
    while (tempString.find("\sqrt")!=-1):
        indexOfSign = tempString.find("\sqrt")
        shift = len(inputString) - len(tempString)
        indexOfSign+=shift  

        if inputString[indexOfSign+5] == '(':
            inputString = inputString[0: indexOfSign+5] + '{' +  inputString[ indexOfSign+6:len(inputString)]
            if(inputString[indexOfSign+6]!=' '):
                inputString = changeEndingBracket(indexOfSign+6, len(inputString), inputString)
                inputString = changeEndingBracket(indexOfSign+6, len(inputString), inputString)
            else:
                inputString = inputString[0: indexOfSign+6] + inputString[ indexOfSign+7:len(inputString)]
                inputString = changeEndingBracket(indexOfSign+6, len(inputString), inputString)
        else:
            if inputString[indexOfSign+5] == ' ':
                inputString = inputString[0:indexOfSign+5] + '{' +  inputString[indexOfSign+6:len(inputString)]
            else:
                inputString = inputString[0:indexOfSign+5] + '{' +  inputString[indexOfSign+5:len(inputString)]

            for j in range(indexOfSign+5,len(inputString)+1):
                if (inputString[j]==' '):
                   inputString = inputString[0:j] +' }' +  inputString[j+1:len(inputString)]
                   break
            
        tempString = inputString[indexOfSign+5:len(inputString)]


    tempString = inputString
    while (tempString.find('/')!=-1):
        indexOfSign = tempString.find('/')
        shift = len(inputString) - len(tempString)
        indexOfSign+=shift  

        if inputString[indexOfSign+1] == '(':
            inputString = inputString[0: indexOfSign+1] + '{' +  inputString[ indexOfSign+2:len(inputString)]
            inputString = changeEndingBracket(indexOfSign, len(inputString), inputString)
        else:
            inputString = inputString[0:indexOfSign+1] + '{' +  inputString[indexOfSign+1:len(inputString)]
            for j in range(indexOfSign+1,len(inputString)+1):
                if (inputString[j]==' '):
                    inputString = inputString[0:j] +' }' +  inputString[j+1:len(inputString)]
                    break

        if inputString[indexOfSign-1] == ')':
            inputString = inputString[0: indexOfSign-1] + '}' +  inputString[indexOfSign:len(inputString)]
            inputString = changeStartingBracket(indexOfSign, len(inputString), inputString)
        # else:
        #     inputString = inputString[0:indexOfSign] + '}' +  inputString[indexOfSign:len(inputString)]
        #     for j in range(indexOfSign+1,len(inputString)+1):
        #         for fun in dic.functions:
        #             inputString = inputString[0:j-2] + '{' +  inputString[j-2:len(inputString)]
        #             break

            
        tempString = inputString[indexOfSign+1:len(inputString)]

            
        

        
    #inputString = input.replace(" ","")
    return inputString

       
            
def prepareText(input):
    inputString = input.replace("\n","")
    inputString += " "
    i=0
    
    while(i < len(inputString)):
        
        if (inputString[i] == '^') or (inputString[i] == '_') or (inputString[i] == '/'):
            if inputString[i+1] == '(':
                inputString = inputString[0:i+1] + '{' +  inputString[i+2:len(inputString)]
                inputString = changeEndingBracket(i, len(inputString), inputString)
            else:
                inputString = inputString[0:i+1] + '{' +  inputString[i+1:len(inputString)]
                for j in range(i+1,len(inputString)+1):
                    if (inputString[j]==' '):
                        inputString = inputString[0:j] +' }' +  inputString[j+1:len(inputString)]
                        break
        if(inputString[i] == '/'):
            if (inputString[i-1] == ')'):
                inputString = inputString[0:i-1] + '}' +  inputString[i:len(inputString)]
                inputString = changeStartingBracket(i, len(inputString), inputString)
            else:
                inputString = inputString[0:i] + '}' +  inputString[i:len(inputString)]
                for j in range(i+1,0,-1):
                    if (inputString[j] in dic.functions):
                        inputString = inputString[0:j-2] + '{' +  inputString[j-2:len(inputString)]
                        i+=2
                        break
        #if(inputString[i] == '\\'):
           
                
        
        i+=1
                    

        
                        
        
                    
             
    
    #inputString = input.replace(" ","")
    return inputString
    

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
                isSomeBracketOpen = False

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
                    maybeRoot=input[t[0]:t[1]].find(value[0])
                    if maybeRoot != -1:
                        if(indexOfRoot == -1 or indexOfRoot>maybeRoot+t[0]):
                            indexOfRoot = maybeRoot+t[0]
                            keyofRoot = key
                            valueForRoot = value[0]
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
        changedString = changedString.replace(value[0], " "*len(value[0]))
    
    for i in range(len(changedString)):
        if changedString[i] == ' ':
            previousIsNotEmpty = False
            continue
        if previousIsNotEmpty:
            if isPreviousASymbol:
                output +=  input[indexOfNextStart:i] + "\\bullet"
                indexOfNextStart = i
            else:
                if changedString[i] not in dic.numbers:
                    output +=  input[indexOfNextStart:i] + "\\bullet"
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
        if input[i]=='(':
            openBrackets +=1
        if input[i] == ')':
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

    

def docToTree(inputString):
    tree = Tree()
    dictionary = dic.symbols
    prepareText(inputString)
    maxPriority = dic.findMaxPriority(dictionary)
    inputString = addMultiplySign(inputString,dictionary)
    
    # root returns [indexOfRoot,keyofRoot,valueForRoot]
    tree = findNextSubtree(inputString,maxPriority,dictionary,tree,'root','')

    tree.show()




input = '\sqrt(b^2 - 4ac)+5ab' 

#docToTree(input)

print(prepareText("2^(2^(2)) + 11^(457^2) + 12_(152) - 13_45 + 15^789_12 "))
print(prepareText("2+3 "))
print(prepareText("2+3_3 -()/(((x)+1))+y/x - 1/(2+3)"))

print(testPrepareText("2^(2^(2)) + 11^(457^2) + 12_(152) - 13_45 + 15^789_12 "))
print(testPrepareText("2+3-\sqrt(12x)"))
print(testPrepareText("2+3_3 -()/(((x)+1))+y/x - 1/(2+3) + \sqrt( \sqrt(12x)y )"))


