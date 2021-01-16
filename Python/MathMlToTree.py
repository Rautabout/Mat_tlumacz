import dictionary as dic
import re
from treelib import Node, Tree


def stripUnnecessary(inputString):
    inputString = inputString.lstrip('<math>')
    inputString = inputString.rstrip('</math>')
    inputString = inputString.replace(" ", "")
    inputString = inputString.replace("<mi>", "")
    inputString = inputString.replace("</mi>", "")
    inputString = inputString.replace("<mo>", "")
    inputString = inputString.replace("</mo>", "")
    inputString = inputString.replace("<mn>", "")
    inputString = inputString.replace("</mn>", "")
    inputString = inputString.strip("\n")
    return inputString


def findNestedSubStrings(inputString):
    inputString = stripUnnecessary(inputString)
    print(inputString)
    for symbol in dic.mathMlStartSymbolsWithNesting + dic.mathMlEndSymbolsWithNesting:
        print(symbol)
        res = [i.start() for i in re.finditer(symbol, inputString)]
        for x in res:
            print(x)
            print(x + len(symbol))


def mathMlToTree(inputString):
    tree=Tree()
    findNestedSubStrings(inputString)

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
