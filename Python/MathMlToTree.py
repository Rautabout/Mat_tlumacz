import dictionary as dic
import re
from treelib import Node, Tree


def stripUnnecessary(inputString):
    inputString = inputString.lstrip('<math>\n')
    inputString = inputString.rstrip('</math>')
    inputString = inputString.replace("<mrow>\n", "")
    inputString = inputString.replace("\n</mrow>", "")
    inputString = inputString.replace(" ", "")
    inputString = inputString.replace("<mi>", "")
    inputString = inputString.replace("</mi>", "")
    inputString = inputString.replace("<mo>", "")
    inputString = inputString.replace("</mo>", "")
    inputString = inputString.replace("<mn>", "")
    inputString = inputString.replace("</mn>", "")
    inputString = inputString.rstrip("\n")
    return inputString


def addMultiplySign(inputString, listOfKeys):
    i = 0
    isPreviousMI = False
    previousIsNotEmpty = False
    indexFound = False
    keyValue = ["</mo>", "</msup>"]
    indexOfNextStart = 0
    output=""
    inputString = inputString.replace(" ", "")

    # print(inputString)

    # for key in listOfKeys:
    # for m in re.finditer("<mi>",inputString):
    #     print(m.start(),m.end())
    #     print(inputString[m.start():m.end()])
    #     print(inputString[m.start()-1-len(keyValue):m.end()-len(keyValue)])
    #     index=m.start()
    #     inputString = inputString[:index] + "<mo>*</mo>\n" + inputString[index:]
    for key in listOfKeys:
        index = 0
        while index < len(inputString):
            index = inputString.find(key, index)
            if index == -1:
                break
            print(index, index + len(key))
            print(indexOfNextStart)
            print(inputString[index:index + len(key)])
                #for value in keyValue:
                    #if inputString[index-len(value):index+len(key)-len(value)] != value:
            output=inputString[:index] + "<mo>*</mo>\n" +inputString[index:]
            inputString=output
            indexOfNextStart=index
            index += len(key)+10

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
    inputString = addMultiplySign(inputString, dic.mathMlSymbolsWithUndercoverMultiplySign)
    inputString = stripUnnecessary(inputString)
    # print(inputString)

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
    <mi>alpha</mi>
    <mo>-</mo>
    <mn>5</mn>
    <mi>e</mi>
    <mo>)</mo>
</math>"""

mathMlToTree(input)
