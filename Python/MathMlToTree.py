import dictionary as dic
import re
from treelib import Node, Tree

mathMlStartSymbolsWithNesting = ["<msqrt>", "<msup>", "<msub>", "<mfrac>"]
mathMlEndSymbolsWithNesting = ["</msqrt>", "</msup>", "</msub>", "</mfrac>"]
mathMlSymbolOpenRow = "{"
mathMlSymbolClosedRow = "}"
mathMlSymbolsToPutBetween = ["<mfrac>", "<msup>", "<msub>"]
mathMlSymbolsWithUndercoverMultiplySign = ["[msqrt]", "[&alpha;]", "[&beta;]", "[&gamma;]", "[&delta;]", "[sin]",
                                           "[cos]", "[tan]", "[cot]", "[pi]", "[e]"]


def checkIfStartBracketExistBetweenSpecial(inputString, openingSymbols):
    output = ''
    indexOfNextStart = 0

    for i in range(len(inputString)):
        for keyValue in openingSymbols:
            if inputString[i:(i + len(keyValue))] == keyValue:
                if inputString[
                   (i + len(keyValue) + 1):(i + len(keyValue) + len(mathMlSymbolOpenRow) + 1)] == mathMlSymbolOpenRow:
                    output += inputString[indexOfNextStart:i] + keyValue[0:len(keyValue)] + mathMlSymbolOpenRow
                    indexOfNextStart = i + len(keyValue) + len(mathMlSymbolOpenRow) + 1
                else:
                    output += inputString[indexOfNextStart:i] + keyValue[0:len(keyValue)] + '{'
                    indexOfNextStart = i + len(keyValue)
    if (indexOfNextStart < len(inputString)):
        output += inputString[indexOfNextStart:]

    return output


def checkIfEndBracketExistBetweenSpecial(inputString, closingSymbols):
    output = ''
    indexOfNextStart = 0

    for i in range(len(inputString)):
        for keyValue in closingSymbols:
            if inputString[i:(i + len(keyValue))] == keyValue:
                if (inputString[(i - len(mathMlSymbolClosedRow) - 1):i - 1]) == mathMlSymbolClosedRow:
                    output += inputString[indexOfNextStart:i]
                    indexOfNextStart = i
                else:
                    output += inputString[indexOfNextStart:i]
                    indexOfNextStart = i + len(keyValue)
    if (indexOfNextStart < len(inputString)):
        output += inputString[indexOfNextStart:]
    return output


def addSpaceInsteadOfSpecial(inputString, keyValue):
    output = ''
    indexOfNextStart = 0

    for i in range(len(inputString)):
        if inputString[i:(i + len(keyValue))] == keyValue:
            output += inputString[indexOfNextStart:i] + ' '
            indexOfNextStart = i + len(keyValue)
    if indexOfNextStart < len(inputString):
        output += inputString[indexOfNextStart:]

    return output


def removeClosingSpecial(inputString, keyValue):
    for key in keyValue:
        inputString = inputString.replace(key, '')

    return inputString


def checkIfMrowAfterSpecial(inputString, keyValue):
    # print(inputString)
    output = ''
    for key in keyValue:
        index = 0
        while index < len(inputString):
            index = inputString.find(key, index)
            indexClosingAfterSpecial = inputString.find('>', (index + len(key) + 1))
            indexOpeningAfterSpecial = inputString.find('<', (index + len(key)))
            indexOfKeyClosing = inputString.find(('/' + key[1:]), index)
            indexOfFirstClosing = inputString.find('</', index)
            indexOfClosingAfterFirstClosing = inputString.find('>', indexOfFirstClosing + 1)
            if index == -1:
                break
            if inputString[(index + len(key) + 1):indexClosingAfterSpecial + 1] == "<mrow>":
                output = inputString
                inputString = output
                index += 1
            else:
                if key != "<msqrt>":
                    output = inputString[:indexOpeningAfterSpecial] + "<mrow>" + inputString[
                                                                                 indexOpeningAfterSpecial:indexOfClosingAfterFirstClosing + 1] + "</mrow><mrow>" + inputString[
                                                                                                                                                                   indexOfClosingAfterFirstClosing + 1:(
                                                                                                                                                                               indexOfKeyClosing - 1)] + "</mrow>" + inputString[
                                                                                                                                                                                                                     (
                                                                                                                                                                                                                                 indexOfKeyClosing - 1):]
                    inputString = output
                    index += 1
                else:
                    output = inputString[:indexOpeningAfterSpecial] + "<mrow>" + inputString[indexOpeningAfterSpecial:(
                                indexOfKeyClosing - 1)] + "</mrow>" + inputString[(indexOfKeyClosing - 1):]
                    inputString = output
                    index += 1
    # print(output)
    return output


def putSpecialInBetween(inputString, keyValue):
    output = ''
    for key in keyValue:
        numberOfLeftBrackets = 0
        numberOfRightBrackets = 0
        index = 0
        indexOfLeftBracket = 0
        indexOfRightBracket = 0
        indexOfKeyValue = 0
        numberOfKeyOccurences = 0
        for i in inputString:
            if inputString[index:index + len(key)] == key:
                numberOfKeyOccurences = numberOfKeyOccurences + 1
            index = index + 1
        while numberOfKeyOccurences > 0:
            numberOfLeftBrackets = 0
            numberOfRightBrackets = 0
            indexOfLeftBracket = 0
            indexOfRightBracket = 0
            jindex = 0
            for j in inputString:
                if inputString[jindex:jindex + len(key)] == key:
                    indexOfKeyValue = jindex
                jindex = jindex + 1
            kindex = 0
            for k in inputString:
                if kindex > indexOfKeyValue:
                    if k == '{':
                        numberOfLeftBrackets = numberOfLeftBrackets + 1
                        indexOfLeftBracket = kindex
                    if k == '}':
                        numberOfRightBrackets = numberOfRightBrackets + 1
                        indexOfRightBracket = kindex
                kindex = kindex + 1
                if (indexOfLeftBracket == indexOfRightBracket + 1) and (
                        numberOfLeftBrackets == numberOfRightBrackets + 1):
                    output = inputString[:indexOfKeyValue] + inputString[indexOfKeyValue + len(
                        key):indexOfRightBracket + 1] + '[' + key[1:(len(key) - 1)] + ']' + inputString[
                                                                                            indexOfLeftBracket:]
            inputString = output
            numberOfKeyOccurences = numberOfKeyOccurences - 1

    return inputString


def addMultiplySign(inputString, dictionary, listOfKeys):
    previousIsNotEmpty = False
    isPreviousASymbol = False
    output = ""
    indexOfNextStart = 0

    changedString = inputString.replace('{', " ")
    changedString = changedString.replace('}', " ")
    for value in dictionary.values():
        if value[2] not in listOfKeys:
            changedString = changedString.replace(value[2], " " * len(value[2]))
        else:
            changedString = changedString.replace(value[2], "/" + " " * (len(value[2]) - 1))
    for i in range(len(changedString)):
        if changedString[i] == ' ':
            previousIsNotEmpty = False
            continue
        if previousIsNotEmpty:
            if isPreviousASymbol and (changedString[i] == "/" or changedString[i] != ']') and changedString[
                i - 1] != ']':
                output += inputString[indexOfNextStart:i] + '[*]'
                indexOfNextStart = i
            else:
                if changedString[i] not in dic.numbers and (changedString[i] == "/" or changedString[i] != ']') and \
                        changedString[i - 1] != '[' and changedString[i - 2] != '(' and changedString[i + 1] != ')':
                    output += inputString[indexOfNextStart:i] + '[*]'
                    indexOfNextStart = i

        else:
            previousIsNotEmpty = True

        if changedString[i] not in dic.numbers and changedString[i] != '[':
            isPreviousASymbol = True
        else:
            isPreviousASymbol = False

    if indexOfNextStart < len(inputString):
        output += inputString[indexOfNextStart:]

    return output


def modifyNegativePhrase(inputString):
    output = ''
    indexOfNextStart = 0
    minusLength = len("[-]")

    for i in range(len(inputString)):
        if inputString[i:(i + minusLength)] == "[-]":
            if i - 1 == -1 or inputString[i - 2] == "(" or inputString[i - 1] == "{":
                output += inputString[indexOfNextStart:i] + '[minus]'
                indexOfNextStart = i + minusLength
    if (indexOfNextStart < len(inputString)):
        output += inputString[indexOfNextStart:]
    # print(output)
    return output


def prepareString(inputString):
    inputString = inputString.lstrip('<math>\n')
    inputString = inputString.rstrip('</math>')
    inputString = inputString.replace(" ", "")
    inputString = checkIfMrowAfterSpecial(inputString, mathMlStartSymbolsWithNesting)
    inputString = inputString.replace('<mrow>', '{')
    inputString = inputString.replace('</mrow>', '}')
    inputString = checkIfEndBracketExistBetweenSpecial(inputString, mathMlEndSymbolsWithNesting)
    inputString = checkIfStartBracketExistBetweenSpecial(inputString, mathMlStartSymbolsWithNesting)
    inputString = inputString.replace('</mfrac>', '')
    inputString = inputString.replace('</msup>', '')
    inputString = inputString.replace('</msub>', '')
    inputString = inputString.replace('</msqrt>', '')
    inputString = inputString.replace("\n", "")
    inputString = putSpecialInBetween(inputString, mathMlSymbolsToPutBetween)
    inputString = inputString.replace('<msqrt>', '[msqrt]')
    inputString = re.sub('</[^>]+>', ']', inputString)
    inputString = re.sub('<[^>]+>', '[', inputString)
    inputString = inputString.replace('msup', '^')
    inputString = inputString.replace('msub', '_')
    inputString = addMultiplySign(inputString, dic.symbols, mathMlSymbolsWithUndercoverMultiplySign)
    inputString = modifyNegativePhrase(inputString)
    inputString = inputString.replace("[(]", '{')
    inputString = inputString.replace("[)]", '}')
    # print(inputString)

    # inputString=inputString.replace('[','')
    # inputString=inputString.replace(']','')
    # inputString=inputString.replace('minus','[minus]')
    # inputString=inputString.replace('[msqrt]','msqrt')

    # print(inputString)

    # print(inputString)

    return inputString


def mathMlToTree(inputString):
    tree = Tree()
    dictionary = dic.symbols
    maxPriority = dic.findMaxPriority(dictionary)
    inputString = prepareString(inputString)
    tree = findNextSubtree(inputString, maxPriority, dictionary, tree, 'root', '')

    leaves = tree.leaves()
    for i in leaves:
        name = i.identifier
        if name.endswith('.left'):
            parent = name[0:-5]
            # print(parent)
        elif name.endswith('.right'):
            parent = name[0:-6]
        i.tag = i.tag.replace('[minus]', '-')
        i.tag = i.tag.replace('[', '')
        i.tag = i.tag.replace(']', '')
        i.tag = i.tag.replace(';', '')
        i.tag = i.tag.replace('&', '')
        tag = i.tag.replace('-', '[minus]')
        tree.remove_node(name)
        tree.create_node(tag, name, parent)
    tree.show()


def isWholeInBracket(inputString):
    openBrackets = 1
    if inputString[0] == '{' and inputString[len(inputString) - 1] == '}':
        for i in range(1, len(inputString)):
            if inputString[i] == '{':
                openBrackets += 1
            if inputString[i] == '}':
                openBrackets -= 1
            if openBrackets == 0 and i < len(inputString) - 1:
                return False

        if openBrackets == 0:
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


def findStartBracket(inputString, indexofEndBracket):
    sumOfBrackets = 1
    # print('startbracket')
    # print(indexofEndBracket)
    for a in range(indexofEndBracket - 2, -1, -1):
        # print('i:' + str(a))
        # print(inputString[a])
        # print()
        if inputString[a] == '}':
            sumOfBrackets += 1
        elif inputString[a] == '{':
            sumOfBrackets -= 1
            if sumOfBrackets == 0:
                return a


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
    keyofRoot = ""
    valueForRoot = ""
    for priority in range(maxPriority + 1):
        for t in tableofIndexes:
            for key, value in dictionary.items():
                if value[3] == str(priority):
                    maybeRoot = input[t[0]:t[1]].find(value[2])
                    if maybeRoot != -1:
                        if (indexOfRoot == -1 or indexOfRoot > maybeRoot + t[0]):
                            indexOfRoot = maybeRoot + t[0]
                            keyofRoot = key
                            valueForRoot = value[2]
        if (indexOfRoot != -1):
            return [indexOfRoot, keyofRoot, valueForRoot]


mathMlJustSymbols = ["alpha", "beta", "gamma", "delta", "pi", "e"]
mathMlFunctions = ["sin", "cos", "tan", "cot"]
mathMlChildsWithoutBrackets = ['+', '-', '*', '<=', '>=', '<', '>', 'in', 'notin', 'and', 'or']
mathMlChildWithRightBracket = ["^", "_", "/"]
mathMlSymbolsWithBrackets = ["[msqrt]"]


def findChilds(inputString, root):
    if root[1] in mathMlChildsWithoutBrackets:
        left = inputString[0:root[0]]
        right = inputString[root[0] + len(root[2]):]
    if root[1] in dic.mathMlSymbolsWithBracket:
        endOfFirst = findEndIndexOfActualCurlyBracket(root[0] + len(root[2]), inputString)
        endOfSecond = findEndIndexOfActualCurlyBracket(endOfFirst + 1, inputString)
        left = inputString[root[0] + 1 + len(root[2]):endOfFirst]
        right = inputString[endOfFirst + 2:endOfSecond]
    if root[1] in dic.mathMlChildWithRightBracket:
        if inputString[root[0] - 1] == '}':
            start = findStartBracket(inputString, root[0])
            inputString = inputString[:start] + inputString[start + 1:]
        left = inputString[:root[0] - 2]
        right = inputString[root[0] + 3:-1]
    if root[1] in dic.mathMlSymbolsWithBrackets:
        left = inputString[root[0] + len(root[2]) + 1:-1]
        right = None
    if root[1] in mathMlFunctions:
        left = inputString[root[0] + len(root[2]):]
        right = None
    if root[1] in mathMlJustSymbols:
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
        <mi>a</mi>
        <mn>444</mn>
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
#       <mfrac>
#          <mrow>
#              <msup>
#                  <mrow>
#                      <mo>-</mo>
#                      <mi>b</mi>
#                  </mrow>
#                  <mrow>
#                      <msup>
#                          <mn>2</mn>
#                          <mn>3</mn>
#                      </msup>
#                  </mrow>
#              </msup>
#              <mo>+</mo>
#              <mi>y</mi>
#          </mrow>
#          <mrow>
#              <mn>12</mn>
#              <mo>-</mo>
#              <mn>3</mn>
#         </mrow>
#      </mfrac>
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
#     <mfrac>
#         <mrow>
#             <msup>
#                 <mrow>
#                     <mo>-</mo>
#                     <mi>b</mi>
#                 </mrow>
#                 <mrow>
#                     <msup>
#                         <mn>2</mn>
#                         <mn>3</mn>
#                     </msup>
#                 </mrow>
#             </msup>
#             <mo>+</mo>
#             <mi>y</mi>
#         </mrow>
#         <mrow>
#             <mfrac>
#                 <mrow>
#                     <mn>345</mn>
#                     <mo>+</mo>
#                     <mi>b</mi>
#                 </mrow>
#                 <mrow>
#                     <mi>c</mi>
#                     <mo>-</mo>
#                     <mi>d</mi>
#                 </mrow>
#             <mo>-</mo>
#             <mn>3</mn>
#         </mrow>
#     </mfrac>
#     <msqrt>
#     <mi>b</mi>
#     </msqrt>
#     <msqrt>
#     <mrow>
#     <mi>a</mi>
#     <mi>b</mi>
#     </mrow>
#     </msqrt>
#     <mi>sin</mi>
#      <mo>(</mo>
#      <mo>&alpha;</mo>
#      <mo>-</mo>
#      <mn>5</mn>
#      <mi>e</mi>
#      <mo>)</mo>
# </math>
#
# """

mathMlToTree(input)

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