import DocToTree
import TreeToDoc
import TexToTree
import TreeToTex
import MathMlToTree
import TreeToMathml
import sys


def convert(inL,outL,string):
    languages = {}

    languages['tex'] = [TexToTree.texToTree, TreeToTex.treeToTex]
    languages['doc'] = [DocToTree.docToTree, TreeToDoc.treeToDoc]
    languages['mathml']=[MathMlToTree.mathMlToTree, TreeToMathml.treeToMathMl]
            
    return languages[outL][1](languages[inL][0](string))
