import dictionary as dic 
from treelib import Node, Tree


def prepareText(input):
    inputString = input.replace("\n","")
    inputString =" " + inputString + " "
    tempString = inputString
    testString = ""
    endingIndex=0
    numberOfOpenedBrackets=0
    numberOfOpenedCurlyBrackets=0

    for sign in dic.docAddOrChangeBracketsAfter:
        tempString = inputString
        while (tempString.find(sign)!=-1):

            indexOfSign = tempString.find(sign)
            shift = len(inputString) - len(tempString)
            indexOfSign+=shift  

            inputString = inputString[0:indexOfSign+1] + '{' +  inputString[indexOfSign+1:len(inputString)]
            for j in range(indexOfSign+2,len(inputString)):
                if(inputString[j]=='('):
                    numberOfOpenedBrackets+=1
                elif(inputString[j]==')'):
                    numberOfOpenedBrackets-=1
                elif(inputString[j]=='{'):
                    numberOfOpenedCurlyBrackets+=1
                elif(inputString[j]=='}'):
                    numberOfOpenedCurlyBrackets-=1
                elif ((inputString[j]==' ') and (numberOfOpenedBrackets==0) and (numberOfOpenedCurlyBrackets==0)):
                    inputString = inputString[0:j] + ' } ' +  inputString[j+1:len(inputString)]
                    testString = tempString[indexOfSign-shift+1:j-shift-1]
                    endingIndex=j
                    break

            if(testString!=""):
                if(isWholeInBracket(testString) or isWholeInCurlyBracket(testString)):
                    inputString = inputString[0:indexOfSign+2] + inputString[indexOfSign+3:endingIndex-1] + inputString[endingIndex:len(inputString)]  
            
            tempString = inputString[indexOfSign+1:len(inputString)]


    tempString = inputString
    while (tempString.find('/')!=-1):
        indexOfSign = tempString.find('/')
        shift = len(inputString) - len(tempString)
        indexOfSign+=shift  
        endingIndex=0
        numberOfOpenedBrackets=0
        numberOfOpenedCurlyBrackets=0

        inputString = inputString[0: indexOfSign] + '}' +  inputString[indexOfSign:len(inputString)]
        for j in range(indexOfSign-1,-1, -1):
            if(inputString[j]==')'):
                numberOfOpenedBrackets+=1
            elif(inputString[j]=='('):
                numberOfOpenedBrackets-=1
            elif(inputString[j]=='}'):
                numberOfOpenedCurlyBrackets+=1
            elif(inputString[j]=='{'):
                numberOfOpenedCurlyBrackets-=1
            elif ((inputString[j]==' ') and (numberOfOpenedBrackets==0) and (numberOfOpenedCurlyBrackets==0)):
                inputString = inputString[0:j] + ' { ' +  inputString[j+1:len(inputString)]
                testString = tempString[j-shift+1:indexOfSign-shift]
                endingIndex=j
                break

        if(testString!=""):
            if(isWholeInBracket(testString) or isWholeInCurlyBracket(testString)):
                inputString =  inputString[0:endingIndex+3] + inputString[endingIndex+4:indexOfSign+1] + inputString[indexOfSign+2:len(inputString)]
            
        tempString = inputString[indexOfSign+4:len(inputString)]


    
    for item in dic.docDeletSpaceBefore:
        tempString = inputString
        index = tempString.find(item)
        
        while (index!=-1):
            shift = len(inputString) - len(tempString)
            index+=shift  

            if((index>=2) and (tempString[index-shift-1]==" ") and ((tempString[index-shift-2]=="(") or (tempString[index-shift-2]=="{"))):
                inputString = inputString[0:index-1] + inputString[index:len(inputString)]

            tempString = inputString[index+1:len(inputString)]
            index = tempString.find(item)
            

    inputString = inputString.replace('\sqrt', '#')
    tempString = inputString
    while (tempString.find("#")!=-1):
        indexOfSign = tempString.find("#")
        shift = len(inputString) - len(tempString)
        indexOfSign+=shift  
        numberOfOpenedBrackets=0
        numberOfOpenedCurlyBrackets=0

        if inputString[indexOfSign+1] == ' ':
            inputString = inputString[0: indexOfSign+1] + '{' +  inputString[indexOfSign+2:len(inputString)]
        else:
            inputString = inputString[0: indexOfSign+1] + '{' +  inputString[indexOfSign+1:len(inputString)]

        i=indexOfSign+2
        while(i<len(inputString)):
            if(inputString[i]=='('):
                numberOfOpenedBrackets+=1
            elif(inputString[i]==')'):
                numberOfOpenedBrackets-=1
            elif(inputString[i]=='{'):
                numberOfOpenedCurlyBrackets+=1
            elif(inputString[i]=='}'):
                numberOfOpenedCurlyBrackets-=1

            if (numberOfOpenedBrackets==0) and (numberOfOpenedCurlyBrackets==0):
                if((inputString[i]=="#") and (inputString[i+1]==" ")):
                    i+=2
                elif(inputString[i]==" "):
                    inputString = inputString[0: i+1] + '}' +  inputString[i+1:len(inputString)]

                    testString = tempString[indexOfSign-shift+1:i-shift-1]
                    endingIndex=i
                    break

            i+=1
        if(testString!=""):
            if(isWholeInBracket(testString) or isWholeInCurlyBracket(testString)):
                inputString = inputString[0:indexOfSign+2] + inputString[indexOfSign+3:endingIndex-1] + inputString[endingIndex:len(inputString)]  
            
        tempString = inputString[indexOfSign+1:len(inputString)]

    inputString = inputString.replace('#', '\sqrt')
    inputString = inputString.replace(" ","")
    return inputString


def isWholeInBracket(input):
    openBrackets=1
    if input[0]=='(' and input[len(input)-1]==')':
        for i in range(1,len(input)):
            if input[i]=='(':
                openBrackets+=1
            if input[i]==')':
                openBrackets-=1
            if openBrackets == 0 and i<len(input)-1:
                return False

        if openBrackets==0:
            return True
        else:
            return False
    else:
        return False


def isWholeInCurlyBracket(input):
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
                isSomeCurlyBracketOpen = False

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


def addMultiplySign(input,dictionary,listtOfKeys):
    previousIsNotEmpty = False
    isPreviousASymbol = False
    output=""
    indexOfNextStart = 0


    changedString = input.replace('{'," ")
    changedString = changedString.replace('}'," ")
    for value in dictionary.values():
        if value[0] not in listtOfKeys:
            changedString = changedString.replace(value[0], " "*len(value[0]))
        else:
            changedString = changedString.replace(value[0], "\\"+" "*(len(value[0])-1))

    for i in range(len(changedString)):
        if changedString[i] == ' ':
            previousIsNotEmpty = False
            continue
        if previousIsNotEmpty:
            if isPreviousASymbol and (changedString[i]=="\\" or changedString[i]!=')') and changedString[i-1]!='(':
                output +=  input[indexOfNextStart:i] + '\\bullet'
                indexOfNextStart = i
            else:
                if changedString[i] not in dic.numbers and(changedString[i]=="\\" or changedString[i]!=')') and changedString[i-1]!='(':
                    output +=  input[indexOfNextStart:i] + '\\bullet'
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
            openBrackets +=1
        if input[i] == '}':
            openBrackets -=1
        if openBrackets ==0:
            return i

def findEndIndexOfActualCurlyBracketBackwards(openIndex, input):
    openBrackets =1
    
    for i in range(openIndex-1,-1,-1):
        if input[i]=='}':
            openBrackets +=1
        if input[i] == '{':
            openBrackets -=1
        if openBrackets ==0:
            return i

def findChilds(inputString,root):
    if root[1] in dic.teXChildsWithoutBrackets:
        left = inputString[0:root[0]]
        right = inputString[root[0]+len(root[2]):]
    if root[1] in dic.teXChildsWithBrackets:
        startOfFirst = findEndIndexOfActualCurlyBracketBackwards(root[0]-len(root[2]),inputString)
        endOfSecond = findEndIndexOfActualCurlyBracket(root[0]+len(root[2]),inputString)
        left=inputString[startOfFirst+1:root[0]-1]
        right=inputString[root[0]+len(root[2])+1:endOfSecond]
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
    if isWholeInCurlyBracket(inputString):
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

    

def docToTree(inputString):
    tree = Tree()
    dictionary = dic.symbols
    maxPriority = dic.findMaxPriority(dictionary)
    inputString = prepareText(inputString)
    inputString = addMultiplySign(inputString,dictionary,dic.docSymbolsWithUndercoverMultiplySign)
    inputString = modifyNegativePhrases(inputString)
    inputString = inputString.replace("(",'{')
    inputString = inputString.replace(')','}') 
    # root returns [indexOfRoot,keyofRoot,valueForRoot]
    tree = findNextSubtree(inputString,maxPriority,dictionary,tree,'root','')
  
    tree.show()




#input = '\sqrt(b^2 - 4ac) + 5ab' 
input = '-b\sqrt(-b^(2^(3)) - 4ac) + (-5+a)b + 3 \sin(\\alpha-5exp(1))'
#input ='(x+y)/(12-3)'

docToTree(input)

#print(prepareText("2^( 2^( 2 ) ) + 11^( 457^2) + 12_(152) - 13_45 + 15^789_12 "))
#print(prepareText("2+3-\sqrt 12x"))
#print(prepareText("2+3_3 - (x)/(( x)+1) + y/x - 1/( 2+3) + \sqrt( \sqrt( 12x)y )"))


