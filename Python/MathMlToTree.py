import dictionary as dic
import re
from treelib import Node, Tree


def modifyNegativePhrase(inputString):
    output = ''
    indexOfNextStart = 0
    minusLength = len("-")

    for i in range(len(inputString)):
        if inputString[i:(i + minusLength)] == "-":
            if i - 1 == -1 or inputString[i - 1] == "(" or inputString[i - 1] == "{":
                output += inputString[indexOfNextStart:i] + '[minus]'
                indexOfNextStart = i + minusLength
    if (indexOfNextStart < len(inputString)):
        output += inputString[indexOfNextStart:]
    return output


def changeClosingOfSpecial(inputString, endSymbols):
    output = ''
    indexOfNextStart = 0

    for i in range(len(inputString)):
        for keyValue in endSymbols:
            if inputString[i:(i + len(keyValue))] == keyValue:
                output += inputString[indexOfNextStart:i] + '}'
                indexOfNextStart = i + len(keyValue)
    if (indexOfNextStart < len(inputString)):
        output += inputString[indexOfNextStart:]
    return output


def changeOpeningOfSpecial(inputString, openSymbols):
    output = ''
    indexOfNextStart = 0

    for i in range(len(inputString)):
        for keyValue in openSymbols:
            if inputString[i:(i + len(keyValue))] == keyValue:
                output += inputString[indexOfNextStart:i] + keyValue[0:len(keyValue) - 1] + '{'
                indexOfNextStart = i + len(keyValue)
    if (indexOfNextStart < len(inputString)):
        output += inputString[indexOfNextStart:]
    return output


def addSpaceInsteadOfSpecial(inputString,keyValue):
    output = ''
    indexOfNextStart = 0

    for i in range(len(inputString)):
        if inputString[i:(i + len(keyValue))] == keyValue:
            output += inputString[indexOfNextStart:i] + ' '
            indexOfNextStart = i + len(keyValue)
    if indexOfNextStart < len(inputString):
        output += inputString[indexOfNextStart:]

    return output


def findObjectAfterSpecial(inputString):
    indexOfSpace=inputString.find(' ')
    indexOfFirstAfterNext=inputString.find('<',indexOfSpace+4)
    temp=inputString[indexOfSpace:indexOfFirstAfterNext]
    temp=temp.rstrip(' ')
    tempPos=temp.find('<')
    temp2=''
    temp2+=temp[0:0]+temp[tempPos:]
    lenOfObjectAfter = len(temp2)

    return lenOfObjectAfter


def swapPlacesOfSup(inputString):
    keyValue="<msup>"
    firstOutput = addSpaceInsteadOfSpecial(inputString,keyValue)
    if ' ' in firstOutput:
        output=''
        index = 0
        while index < len(firstOutput):
            lenOfObject = findObjectAfterSpecial(firstOutput)
            index=firstOutput.find(' ',index)
            if index == -1:
                break
            output=firstOutput[:index]+firstOutput[(index+1):(index+lenOfObject+1)]+"^{"+firstOutput[(index+lenOfObject+1):]
            firstOutput=output
            index+=len("^{")

        return output
    else:
        return inputString


def swapPlacesOfSub(inputString):
    keyValue="<msub>"
    firstOutput = addSpaceInsteadOfSpecial(inputString,keyValue)
    if ' ' in inputString:
        output=''
        index = 0
        while index < len(firstOutput):
            lenOfObject = findObjectAfterSpecial(firstOutput)
            index=firstOutput.find(' ',index)
            if index == -1:
                break
            output=firstOutput[:index]+firstOutput[(index+1):(index+lenOfObject+1)]+"_{"+firstOutput[(index+lenOfObject+1):]
            firstOutput=output
            index+=1+len("^{")-1
        return output
    else:
        return inputString


def stripUnnecessary(inputString):
    inputString = inputString.lstrip('<math>\n')
    inputString = inputString.replace(" ", "")
    inputString = inputString.replace("\n", "")
    inputString = inputString.replace('<mrow>','{')
    inputString = inputString.replace('</mrow>','}')
    inputString = changeClosingOfSpecial(inputString, dic.mathMlEndSymbolsWithNesting)
    inputString = re.sub('</[^>]+>', '', inputString)
    inputString = swapPlacesOfSup(inputString)
    inputString = swapPlacesOfSub(inputString)
    inputString = changeOpeningOfSpecial(inputString, dic.mathMlStartSymbolsWithNesting)
    inputString = inputString.replace("<mi>", "")
    inputString = inputString.replace("<mo>", "")
    inputString = inputString.replace("<mn>", "")
    inputString = inputString.replace('<mfrac','mfrac')
    inputString = inputString.replace('<msqrt','msqrt')


    return inputString


def addMultiplySign(inputString, dictionary,listOfKeys):
    previousIsNotEmpty = False
    isPreviousASymbol = False
    output = ""
    indexOfNextStart = 0

    changedString = inputString.replace('{', " ")
    changedString = changedString.replace('}', " ")
    for value in dictionary.values():
        if value[2] not in listOfKeys:
            changedString = changedString.replace(value[2]," " * len(value[2]))
        else:
            changedString = changedString.replace(value[2], "/" + " " * (len(value[2]) - 1))

    for i in range(len(changedString)):
        if changedString[i] == ' ':
            previousIsNotEmpty = False
            continue
        if previousIsNotEmpty:
            if isPreviousASymbol and (changedString[i]=="/" or changedString[i]!=')') and changedString[i - 1] != '(':
                output += inputString[indexOfNextStart:i] + '*'
                indexOfNextStart = i
            else:
                if changedString[i] not in dic.numbers and (changedString[i]=="/" or changedString[i]!=')') and changedString[i - 1] != '(':
                    output += inputString[indexOfNextStart:i] + '*'
                    indexOfNextStart = i

        else:
            previousIsNotEmpty = True

        if changedString[i] not in dic.numbers and changedString[i] != '(':
            isPreviousASymbol = True
        else:
            isPreviousASymbol = False

    if indexOfNextStart < len(inputString):
        output += inputString[indexOfNextStart:]

    return output


def isWholeInBracket(inputString):
    openBrackets=1
    if inputString[0]=='{' and inputString[len(inputString)-1]=='}':
        for i in range(1,len(inputString)):
            if inputString[i]=='{':
                openBrackets+=1
            if inputString[i]=='}':
                openBrackets-=1
            if openBrackets == 0 and i<len(inputString)-1:
                return False

        if openBrackets==0:
            return True
        else:
            return False
    else:
        return False


def findProperFragments(inputString):
    openBrackets = 0
    isSomeCurlyBracketOpen = False
    tableOfProperIndexes = []
    tempIndexes = []

    for i in range(len(inputString)):

        if tempIndexes == [] and isSomeCurlyBracketOpen == False and inputString[i] != '{':
            tempIndexes.append(i)

        if inputString[i] == '{':
            if openBrackets == 0:
                isSomeCurlyBracketOpen = True
                if tempIndexes != []:
                    tempIndexes.append(i)
                    tableOfProperIndexes.append(tempIndexes)
                    tempIndexes = []
            openBrackets += 1
        if inputString[i] == '}':
            openBrackets -= 1
            if openBrackets == 0:
                isSomeCurlyBracketOpen = False

        if i == len(inputString) - 1 and tempIndexes != []:
            tempIndexes.append(i)
            tableOfProperIndexes.append(tempIndexes)

    return tableOfProperIndexes


def findEndIndexOfActualCurlyBracket(openIndex, inputString):
    openBrackets = 1

    for i in range(openIndex + 1, len(inputString) + 1):
        if inputString[i] == '{':
            openBrackets += 1
        if inputString[i] == '}':
            openBrackets -= 1
        if openBrackets == 0:
            return i


def findRoot(tableofIndexes, input, maxPriority, dictionary):
    indexOfRoot = -1
    keyofRoot=""
    valueForRoot =""
    for priority in range(maxPriority+1):
        for t in tableofIndexes:
            for key,value in dictionary.items():
                if value[3]==str(priority):
                    maybeRoot=input[t[0]:t[1]].find(value[2])
                    if maybeRoot != -1:
                        if(indexOfRoot == -1 or indexOfRoot>maybeRoot+t[0]):
                            indexOfRoot = maybeRoot+t[0]
                            keyofRoot = key
                            valueForRoot = value[2]
        if(indexOfRoot!=-1):
            return [indexOfRoot,keyofRoot,valueForRoot]


def findChilds(inputString, root):
    if root[1] in dic.mathMlChildsWithoutBrackets:
        left = inputString[0:root[0]]
        right = inputString[root[0] + len(root[2]):]
    if root[1] in dic.mathMlSymbolsWithBracket:
        endOfFirst = findEndIndexOfActualCurlyBracket(root[0] + len(root[2]), inputString)
        endOfSecond = findEndIndexOfActualCurlyBracket(endOfFirst + 1, inputString)
        left = inputString[root[0] + 1 + len(root[2]):endOfFirst]
        right = inputString[endOfFirst + 2:endOfSecond]
    if root[1] in dic.mathMlChildWithRightBracket:
        endOfBracket = findEndIndexOfActualCurlyBracket
        left = inputString[:root[0]]
        right = inputString[root[0] + 2:-1]
    if root[1] in dic.mathMlSymbolsWithBrackets:
        left = inputString[root[0] + len(root[2]) + 1 :-1]
        right = None
    if root[1] in dic.mathMlFunctions:
        left = inputString[root[0] + len(root[2]): ]
        right = None
    if root[1] in dic.mathMlJustSymbols:
        left = None
        right = None
    return [left, right]


def findNextSubtree(inputString, maxPriority, dictionary, tree, rootName, parent):
    if isWholeInBracket(inputString):
        if parent == '':
            root = tree.create_node('(', rootName)
        else:
            root = tree.create_node('(', rootName, parent=parent)
        left = inputString[1:len(inputString) - 1]
        try:
            findNextSubtree(left, maxPriority, dictionary, tree, rootName + '.left', rootName)
        except:
            tree.create_node(left, rootName + '.left', parent=rootName)

    else:
        root = findRoot(findProperFragments(inputString), inputString, maxPriority, dictionary)
        left = findChilds(inputString, root)[0]
        right = findChilds(inputString, root)[1]

        if root != None:
            if parent == '':
                tree.create_node(root[1], rootName)
            else:
                tree.create_node(root[1], rootName, parent=parent)

            try:
                findNextSubtree(left, maxPriority, dictionary, tree, rootName + '.left', rootName)
            except:
                tree.create_node(left, rootName + '.left', parent=rootName)
            try:
                findNextSubtree(right, maxPriority, dictionary, tree, rootName + '.right', rootName)
            except:
                if right != None:
                    tree.create_node(right, rootName + '.right', parent=rootName)

    return tree




def mathMlToTree(inputString):
    tree = Tree()
    dictionary = dic.symbols
    maxPriority = dic.findMaxPriority(dictionary)
    inputString = stripUnnecessary(inputString)
    inputString = addMultiplySign(inputString, dic.symbols, dic.mathMlSymbolsWithUndercoverMultiplySign)
    inputString = modifyNegativePhrase(inputString)
    inputString = inputString.replace("(",'{')
    inputString = inputString.replace(')','}')
    inputString = inputString.replace('mfrac','/')
    inputString = inputString.replace('msqrt','sqrt')
    inputString = inputString.replace('&','')
    inputString = inputString.replace(';','')
    tree = findNextSubtree(inputString,maxPriority,dictionary,tree,'root','')

    return tree
    # findNestedSubStrings(inputString)

#-b\cdot\sqrt{-b^{2^{3}}-4\cdota\cdotc}+(-5+a)\cdotb+3\cdot\sin(\alpha-5\cdote)
#-b*<msqrt{-b^{2^{3}}-4*a*c}+(-5+a)*b+3*sin(&alpha;-5*e)

# input = """<math>
#     <mo>-</mo>
#     <mi>b</mi>
#     <msqrt>
#         <mo>-</mo>
#         <msup>
#             <mi>b</mi>
#             <msup>
#                 <mn>2</mn>
#                 <mn>3</mn>
#             </msup>
#         </msup>
#         <mo>-</mo>
#         <mn>4</mn>
#         <mi>a</mi>
#         <mi>c</mi>
#     </msqrt>
#     <mo>+</mo>
#     <mo>(</mo>
#     <mo>-</mo>
#     <mn>5</mn>
#     <mo>+</mo>
#     <mi>a</mi>
#     <mo>)</mo>
#     <mi>b</mi>
#     <mo>+</mo>
#     <mn>3</mn>
#     <mi>sin</mi>
#     <mo>(</mo>
#     <mo>&alpha;</mo>
#     <mo>-</mo>
#     <mn>5</mn>
#     <mi>e</mi>
#     <mo>)</mo>
# </math>"""

# input="""
# <math>
#     <msqrt>
#         <mo>-</mo>
#         <msup>
#             <mi>b</mi>
#             <mn>2</mn>
#         </msup>
#         <mo>-</mo>
#         <mn>4</mn>
#         <mi>a</mi>
#         <mi>c</mi>
#     </msqrt>
#     <mo>+</mo>
#     <mn>5</mn>
#     <mi>a</mi>
#     <mi>b</mi>
# </math>
# """

# input="""
# <math>
#     <mfrac>
#         <mrow>
#             <mi>x</mo>
#             <mo>+</mo>
#             <mi>y</mi>
#         </mrow>
#         <mrow>
#             <mn>12</mn>
#             <mo>-</mo>
#             <mn>3</mn>
#         </mrow>
#     </mfrac>
# </math>
#
# """

# mathMlToTree(input)
