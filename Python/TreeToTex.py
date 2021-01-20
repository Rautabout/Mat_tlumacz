import TexToTree
import dictionary as dic
import treelib
import DocToTree



def findIndexOfTheLastDot(inputString):
    index=-1
    tempString = inputString
    while(tempString.find(".")!=-1):
        index = tempString.find(".")
        tempString = tempString[index+1:]

    index = len(inputString) - (len(tempString)+1)

    return index


def mergeString(inputString,root,left,right=None):
    if left in dic.teXJustSymbols:
        left = inputString=dic.symbols[left][1]
    if right in dic.teXJustSymbols:
        right =inputString=dic.symbols[right][1]
    if root in dic.teXChildsWithoutBrackets:
        inputString = left+dic.symbols[root][1]+right
    elif root in dic.teXChildsWithBrackets:
        inputString=dic.symbols[root][1]+'{'+left+'}{'+right+'}'
    elif root in dic.teXChildsWithRightBracket:
        inputString=left+dic.symbols[root][1]+'{'+right+'}'
    elif root in dic.teXChildWithBracket:
        inputString = dic.symbols[root][1]+'{'+left+'}'
    elif root in dic.teXFunctions:
        inputString=dic.symbols[root][1]+left
    elif root=='(':
        inputString='('+left+')'
    
    return inputString

    
def treeToTex(tree):
    while(True):
        #Stwórz tablicę z liśćmi
        leavesTab = tree.leaves()
        i = 0
        while(True):
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
                            tree.create_node(mergeString('',parent.tag, left.tag, right.tag), parentIdentifier)
        
                        else:
                            tree.create_node(mergeString('',parent.tag, left.tag, right.tag), parentIdentifier,  parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])
                else:
                    #usuń lewe dziecko i podmień rodzica
                    tree.remove_node(left.identifier)
                    tree.remove_node(parentIdentifier)
                    if(parentIdentifier=="root"):
                        tree.create_node(mergeString('',parent.tag,left.tag),parentIdentifier)
                    else:
                        tree.create_node(mergeString('',parent.tag,left.tag),parentIdentifier, parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])                

            i+=1
            if(i == len(leavesTab)):
                break

        if(len(leavesTab)==1):
            break


    return tree.get_node("root").tag.replace('[minus]', '-')


    


# input = '-b\sqrt{-b^{2^{3}}-4ac}+(-5+a)b+3\sin(\\alpha-5e)' 
input = '2 + 3 - 4'
tree = DocToTree.docToTree(input)
tree.show()
print(treeToTex(tree))
