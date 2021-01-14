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


# leaf.identifier[0:findIndexOfTheLastDot(leaf.identifier)]    <--- tworzenie Rodzica
# tree.remove_node(leaf.identifier)    <--- usuwanie
# tree.get_node(leaf.identifier) <--- wzięcie węzła
# tree.get_node(leaf.identifier).identifier <---- wzięcie wartości węzła


# PIERWSZA WERSJA DZIAŁA, JAK SĄ LIŚCIE Z NONE

# def treeToDoc(tree):
#     tree.show()
#     while(True):
#         leavesTab = tree.leaves()
#         i = 0
#         while(True):
#             if(leavesTab[i].identifier.endswith(".left")):
#                 rightExists = False
#                 left = leavesTab[i]
#                 parentIdentifier = left.identifier[0:findIndexOfTheLastDot(left.identifier)]
#                 parent = tree.get_node(parentIdentifier)
#                 rightIdentifier = parentIdentifier + ".right"

#                 #if rightIdentifier in leavesTab:
#                 #    right = tree.get_node(parentIdentifier + ".right")

#                 if(tree.get_node(parentIdentifier + ".right").is_leaf()):
#                     #Usunięcie dzieci z drzewa
#                     tree.remove_node(left.identifier)
#                     if (tree.get_node(parentIdentifier + ".right") in leavesTab):
#                         rightExists = True
#                         right = tree.get_node(parentIdentifier + ".right")
#                         tree.remove_node(rightIdentifier)

#                     #Zamiana rodzica
#                     tree.remove_node(parentIdentifier)
#                     if(parentIdentifier=="root"):
#                         tree.create_node(parent.tag + " " + left.tag + " " + right.tag, parentIdentifier)
#                     elif (rightExists):
#                       tree.create_node(parent.tag + " " + left.tag + " " + right.tag, parentIdentifier, parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])
#                     else:
#                        tree.create_node(parent.tag + " " + left.tag, parentIdentifier, parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])
                    

#             i+=1
#             if(i == len(leavesTab)):
#                 tree.show()
#                 break
#         if(len(leavesTab)==2):
#             break


#DZIAŁA, GDY NIE MA LIŚCI NONE
def treeToDoc(tree):
    while(True):
        #Stwórz tablicę z liśćmi
        leavesTab = tree.leaves()
        i = 0
        while(True):
            tree.show()
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
                        print("jestem")
                        right = tree.get_node(rightIdentifier)

                        #Usuń dzieci z drzewa
                        tree.remove_node(left.identifier)
                        tree.remove_node(rightIdentifier)

                        #podmień rodzica
                        tree.remove_node(parentIdentifier)
                        if(parentIdentifier=="root"):
                            tree.create_node(parent.tag + " " + left.tag + " " + right.tag, parentIdentifier)
                        else:
                            tree.create_node(parent.tag + " " + left.tag + " " + right.tag, parentIdentifier, parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])
                else:
                    #usuń lewe dziecko i podmień rodzica
                    tree.remove_node(left.identifier)
                    tree.remove_node(parentIdentifier)
                    if(parentIdentifier=="root"):
                        tree.create_node(parent.tag + " " + left.tag, parentIdentifier)
                    else:
                        tree.create_node(parent.tag + " " + left.tag, parentIdentifier, parent.identifier[0:findIndexOfTheLastDot(parent.identifier)])
                

            i+=1
            if(i == len(leavesTab)):
                break

        if(len(leavesTab)==1):
            break

    return tree.get_node("root").tag
        
        

input = '\sqrt(b^2 - 4ac) + 5ab' 

tree = DTT.docToTree(input)
print(treeToDoc(tree))