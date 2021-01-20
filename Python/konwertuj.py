import DocToTree
import TreeToDoc
import TexToTree
import TreeToTex
import MathMlToTree
import TreeToMathMl
import sys


def convert(inL,outL,string):
    languages = {}

    languages['tex'] = [TexToTree.texToTree, TreeToTex.treeToTex]
    languages['doc'] = [DocToTree.docToTree, TreeToDoc.treeToDoc]
    # languages['mathml']=[MathMlToTree.mathMlToTree, ]
            
    return languages[outL][1](languages[inL][0](string))

# inL = sys.argv[1]
# outL = sys.argv[2]
# string =sys.argv[3]
# result = convert(inL,outL,string)
# print(result)
