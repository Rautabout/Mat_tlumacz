import TexToTree
import dictionary as dic
import treelib


# def treeToTeX(tree,inputString,root):
#     if tree.get_node(root).tag!=None:
#         if tree.get_node(root+'.left').tag != None:
#             treeToTeX(tree, inputString,root+'.left')
#         else:
#             if tree.get_node(root[:len(root)-5]).tag in dic.teXChildsWithoutBrackets:
#                 inputString += tree.get_node(root).tag + dic.symbols[tree.get_node(root[:len(root)-5]).tag][1]
#             if tree.get_node(root[:len(root)-5]).tag in dic.teXChildsWithBrackets:
#                 inputString = "{"+tree.get_node(root).tag
#         if tree.get_node(root+'.right').tag != None:
#             treeToTeX(tree, inputString,root+'.right')
#         else:
#             if tree.get_node(root[:len(root)-6]).tag in dic.teXChildsWithoutBrackets:
#                 inputString += tree.get_node(root).tag   


#     return inputString

# def treeToTeX(tree):
#     output=''


