import dictionary as dic 
from treelib import Node, Tree
import DocToTree as DTT

def findIndexOfTheLastDot(inputString):
    index=-1
    tempString = inputString
    while(tempString.find(".")!=-1):
        index = tempString.find(".")
        tempString = tempString[index+1:]

    index = len(inputString) - (len(tempString)+1)

    return index

def tagFromParentAndLeftChild(parentTag, leftTag):
    if(leftTag in dic.teXJustSymbols):
        leftTag = dic.symbols[leftTag][0]

    if(parentTag=='sqrt'):
        return dic.symbols[parentTag][0] + "(" + leftTag + ")"
    elif(parentTag=='('):
        return "(" + leftTag + ")"
    else:
        print("jestem" + dic.symbols[parentTag][0])
        return dic.symbols[parentTag][0] + leftTag


def tagFromParentAndChildren(parentTag, leftTag, rightTag):
    if(leftTag in dic.teXJustSymbols):
        leftTag = dic.symbols[leftTag][0]
    if(rightTag in dic.teXJustSymbols):
        rightTag = dic.symbols[rightTag][0]

    if parentTag in dic.teXChildsWithoutBrackets:
        return leftTag + " " + dic.symbols[parentTag][0] + " " + rightTag
    elif parentTag in dic.teXChildsWithBrackets:
        return  "(" + leftTag + ")" + dic.symbols[parentTag][0] + "(" + rightTag + ")"
    elif parentTag in dic.teXChildsWithRightBracket:
        return   leftTag  + dic.symbols[parentTag][0] + "(" + rightTag + ")"

def treeToDoc(tree):
    while(True):
        #Stwórz tablicę z liśćmi
        leavesTab = tree.leaves()
        i = 0
        while(True):
            #tree.show()
            #Sprawdzaj kolejne elementy tablicy, czy nie kończą się one ".left"
            if(leavesTab[i].identifier.endswith(".left")):
                #stwórz lewy liść, identyfikator rodzica, rodzica i prawy identyfikator
                left = leavesTab[i]
                parentIdentifier = left.identifier[0:findIndexOfTheLastDot(left.identifier)]
                parent = tree.get_node(parentIdentifier)
                rightIdentifier = parentIdentifier + ".right"

                #sprawdź, czy istnieje prawy liść
                if(tree.get_node(rightIdentifier)!=None):
                    if tree.get_node(rightIdentifier).is_leaf():
                        right = tree.get_node(rightIdentifier)

                        #Usuń dzieci z drzewa
                        tree.remove_node(left.identifier)
                        tree.remove_node(rightIdentifier)

                        #podmień rodzica
                        tree.remove_node(parentIdentifier)
                        if(parentIdentifier=="root"):
                            tree.create_node(tagFromParentAndChildren(parent.tag, left.tag, right.tag), parentIdentifier)
                        else:
                            tree.create_node(tagFromParentAndChildren(parent.tag, left.tag, right.tag), parentIdentifier,  parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])
                else:
                    #usuń lewe dziecko i podmień rodzica
                    tree.remove_node(left.identifier)
                    tree.remove_node(parentIdentifier)
                    if(parentIdentifier=="root"):
                        tree.create_node(tagFromParentAndLeftChild(parent.tag,left.tag),parentIdentifier)
                    else:
                        tree.create_node(tagFromParentAndLeftChild(parent.tag,left.tag),parentIdentifier, parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])
                        

            i+=1
            if(i == len(leavesTab)):
                break

        if(len(leavesTab)==1):
            break


    return tree.get_node("root").tag.replace('[minus]', '-')
        
        
#input = '-b\sqrt(-b^(2^(3)) - 4ac) + (-5+a)b + 3 \sin(\\alpha-5exp(1))'
#input = '\sqrt(b^2 - 4ac) + 5ab' 
#input ='(x+y)/(12-3)'
#input = "2+3_3 - (x)/(( x)+1) + y/x - 1/( 2+3) + \sqrt( \sqrt( 12x)y )"

#tree = DTT.docToTree(input)
#print(treeToDoc(tree))