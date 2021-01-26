import dictionary as dic
from treelib import Node,Tree
import MathMlToTree


def findIndexOfTheLastDot(inputString):
    index = -1
    tempString = inputString
    while (tempString.find(".") != -1):
        index = tempString.find(".")
        tempString = tempString[index + 1:]

    index = len(inputString) - (len(tempString) + 1)

    return index


def checkIfNumber(input):
    try:
        val=float(input)
        return True
    except:
        return False

mathMLJustSymbols=["alpha", "beta", "gamma", "delta", "pi", "e"]
mathMLSymbolsWithNoBrackets=['+', '-', '*', '<=', '>=','=', '<', '>','in', 'notin', 'and', 'or']
mathMLWithBrackets = ["mfrac"]
mathMlChildWithBracket="sqrt"
mathMlFunctions=["sin", "cos", "tan", "cot"]
mathMlChildWithRBracket = ["^", "_","/"]


def mergeString(inputString, root, left, right=None):
    if left in mathMLJustSymbols:
        left = inputString = "\n" +dic.symbols[left][4]+"\n"
    elif checkIfNumber(left) == True:
        left = inputString = "<mn>" + left + "</mn>"
    elif len(left)==1:
        left=inputString="<mi>"+left+"</mi>"
    elif '[minus]' in left:
        valueAfterMinus=left[len('[minus]'):]
        if checkIfNumber(valueAfterMinus) == True:
            left=inputString="<mo>-</mo>\n"+"<mn>"+valueAfterMinus+"</mn>\n"
        else:
            left=inputString="<mo>-</mo>\n"+"<mi>"+valueAfterMinus+"</mi>\n"
    if right in mathMLJustSymbols:
        right = inputString = "\n" +dic.symbols[right][4]+"\n"
    elif checkIfNumber(right)==True:
        right=inputString="<mn>"+right+"</mn>"
    elif right is not None:
        if len(right) == 1:
            right = inputString = "<mi>" + right + "</mi>" + "\n"
        elif '[minus]' in right:
            valueAfterMinus = right[len('[minus]'):]
            if checkIfNumber(valueAfterMinus) == True:
                right = inputString = "<mo>-</mo>\n" + "<mn>" + valueAfterMinus + "</mn>\n"
            else:
                right = inputString = "<mo>-</mo>\n" + "<mi>" + valueAfterMinus + "</mi>\n"
    if root in mathMLSymbolsWithNoBrackets:
        inputString = left +"\n"+ dic.symbols[root][4] +"\n" + right
    elif root in mathMLWithBrackets:
        inputString = dic.symbols[root][4] + '<mrow>' + left + '</mrow>\n<mrow>' + right + '</mrow>'+ dic.symbols[root][4][0:1]+"/"+dic.symbols[root][4][1:]
    elif root in mathMlChildWithRBracket:
        inputString =  dic.symbols[root][4] +"\n" + '<mrow>'+"\n" + left+ '</mrow>\n<mrow>'  +"\n" + right +"\n" +'</mrow>'+"\n" + dic.symbols[root][4][0:1]+"/"+dic.symbols[root][4][1:]
    elif root in mathMlChildWithBracket:
        inputString = dic.symbols[root][4] +"\n" + left +"\n"+ dic.symbols[root][4][0:1]+"/"+dic.symbols[root][4][1:]
    elif root in mathMlFunctions:
        inputString = dic.symbols[root][4]+"\n" + left
    elif root == '(':
        inputString = '<mo>(</mo>' + left + "<mo>)</mo>"
    return inputString


def treeToMathMl(tree):
    while (True):
        # Stwórz tablicę z liśćmi
        leavesTab = tree.leaves()
        i = 0
        while (True):
            # Sprawdzaj kolejne elementy tablicy, czy nie kończą się one ".left"
            if (leavesTab[i].identifier.endswith(".left")):
                # stwórz lewy liść, identyfikator rodzica, rodzica i prawy identyfikator
                left = leavesTab[i]
                parentIdentifier = left.identifier[0:findIndexOfTheLastDot(left.identifier)]
                parent = tree.get_node(parentIdentifier)
                rightIdentifier = parentIdentifier + ".right"

                # sprawdź, czy istnieje prawy liść
                if (tree.get_node(rightIdentifier) != None):
                    if tree.get_node(rightIdentifier).is_leaf():
                        right = tree.get_node(rightIdentifier)

                        # Usuń dzieci z drzewa
                        tree.remove_node(left.identifier)
                        tree.remove_node(rightIdentifier)

                        # podmień rodzica
                        tree.remove_node(parentIdentifier)
                        if (parentIdentifier == "root"):
                            tree.create_node(mergeString('', parent.tag, left.tag, right.tag), parentIdentifier)

                        else:
                            tree.create_node(mergeString('', parent.tag, left.tag, right.tag), parentIdentifier,
                                             parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])
                else:
                    # usuń lewe dziecko i podmień rodzica
                    tree.remove_node(left.identifier)
                    tree.remove_node(parentIdentifier)
                    if (parentIdentifier == "root"):
                        tree.create_node(mergeString('', parent.tag, left.tag), parentIdentifier)
                    else:
                        tree.create_node(mergeString('', parent.tag, left.tag), parentIdentifier,
                                         parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])

            i += 1
            if (i == len(leavesTab)):
                break

        if (len(leavesTab) == 1):
            break

    return tree.get_node("root").tag.replace(">\n\n<",">\n<")
