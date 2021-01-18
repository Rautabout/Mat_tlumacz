import dictionary as dic
import re
from treelib import Node, Tree


def modifyNegativePhrase(inputString):
    output = ''
    indexOfNextStart = 0
    minusLength = len("<mo>-")

    for i in range(len(inputString)):
        if inputString[i:(i + minusLength)] == "<mo>-":
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
    indexOfFirstAfterNext=inputString.find('<',indexOfSpace+2)
    if ' ' in inputString[indexOfSpace:indexOfFirstAfterNext]:
        lenOfObjectAfter = indexOfFirstAfterNext - indexOfSpace - 2
    else:
        lenOfObjectAfter = indexOfFirstAfterNext - indexOfSpace - 1
    return lenOfObjectAfter


def swapPlacesOfSup(inputString):
    keyValue="<msup>"
    firstOutput = addSpaceInsteadOfSpecial(inputString,keyValue)
    if ' ' in firstOutput:
        output=''
        # print(firstOutput)
        index = 0
        while index < len(firstOutput):
            lenOfObject = findObjectAfterSpecial(firstOutput)
            index=firstOutput.find(' ',index)
            if index == -1:
                break
            output=firstOutput[:index]+firstOutput[(index+1):(index+lenOfObject+1)]+"^{"+firstOutput[(index+lenOfObject+1):]
            firstOutput=output
            # print(index)
            # print(lenOfObject)
            index+=1+len("^{")-1

        # print(output)
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
            output=firstOutput[:index]+firstOutput[(index+1):(index+lenOfObject+1)]+"^{"+firstOutput[(index+lenOfObject+1):]
            firstOutput=output
            index+=1+len("^{")-1
        return output
    else:
        return inputString


def stripUnnecessary(inputString):
    symbolsToSwitchPlace = ["<msub>", "<msup>"]
    inputString = inputString.lstrip('<math>\n')
    inputString = inputString.replace("<mrow>\n", "")
    inputString = inputString.replace(" ", "")
    inputString = inputString.replace("\n", "")
    # inputString = inputString.replace("<mi>", "")
    # inputString = inputString.replace("<mo>", "")
    # inputString = inputString.replace("<mn>", "")
    inputString = changeClosingOfSpecial(inputString, dic.mathMlEndSymbolsWithNesting)
    inputString = re.sub('</[^>]+>', '', inputString)
    inputString = swapPlacesOfSup(inputString)
    inputString = swapPlacesOfSub(inputString)
    inputString = changeOpeningOfSpecial(inputString, dic.mathMlStartSymbolsWithNesting)
    inputString = modifyNegativePhrase(inputString)
    print(inputString)

    return inputString


def addMultiplySign(inputString, listOfKeys):
    i = 0
    isPreviousMI = False
    previousIsNotEmpty = False
    indexFound = False
    keyValue = ["</mo>", "</msup>", "<msup>", "</msub>", "<msub>"]
    vvalue = "</mo>"
    output = ""
    inputString = inputString.replace(" ", "")

    # print(inputString)
    for key in listOfKeys:
        index = 0
        while index < len(inputString):
            index = inputString.find(key, index)
            if index == -1:
                break
            # print(index, index + len(key))
            # print(inputString[index:index + len(key)])
            # for value in keyValue:
            # print(inputString[index-1-len(value):index+len(key)-len(value)])
            if inputString[(index - 1 - len(vvalue)):(index + len(key) - len(vvalue))] != vvalue:
                output = inputString[:index] + "<mo>*</mo>\n" + inputString[index:]
            inputString = output
            index += len(key) + len("<mo>*</mo>\n")

    print(output)

    return inputString


def findNestedSubStrings(inputString):
    print(inputString)
    for symbol in dic.mathMlStartSymbolsWithNesting + dic.mathMlEndSymbolsWithNesting:
        print(symbol)
        res = [i.start() for i in re.finditer(symbol, inputString)]
        for x in res:
            print(x)
            print(x + len(symbol))


def mathMlToTree(inputString):
    tree = Tree()
    dictionary = dic.symbols
    maxPriority = dic.findMaxPriority(dictionary)
    # inputString = addMultiplySign(inputString, dic.mathMlSymbolsWithUndercoverMultiplySign)
    inputString = stripUnnecessary(inputString)
    print(inputString)

    # findNestedSubStrings(inputString)


input = """<math>
    <mo>-</mo>
    <mi>b</mi>
    <msqrt>
        <mo>-</mo>
        <msup>
            <mi>b</mi>
            <msup>
                <mn>2</mn>
                <mn>3</mn>
            </msup>
        </msup>
        <mo>-</mo>
        <mn>4</mn>
        <mi>a</mi>
        <mi>c</mi>
    </msqrt>
    <mo>+</mo>
    <mo>(</mo>
    <mo>-</mo>
    <mn>5</mn>
    <mo>+</mo>
    <mi>a</mi>
    <mo>)</mo>
    <mi>b</mi>
    <mo>+</mo>
    <mn>3</mn>
    <mi>sin</mi>
    <mo>(</mo>
    <mo>&alpha;</mo>
    <mo>-</mo>
    <mn>5</mn>
    <mi>e</mi>
    <mo>)</mo>
</math>"""

mathMlToTree(input)
