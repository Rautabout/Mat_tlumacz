import DocToTree
import TreeToDoc
import TexToTree
import TreeToTex
import MathMlToTree
import TreeToMathMl
import sys
import dictionary as dic


def checkInputString(inputString,indexOfValueInDic):
    isThereAnythingSpecial = False
    isThereSomethingNotIncludedInDic = False
    tempString = inputString
    
    for i in dic.symbols.values():
        if inputString.find(i[indexOfValueInDic])!=-1:
            isThereAnythingSpecial = True
        tempString = tempString.replace(i[indexOfValueInDic],'')
    if indexOfValueInDic == 0 or indexOfValueInDic==1:
        if tempString.find('\\') != -1:
            isThereSomethingNotIncludedInDic = True
    elif indexOfValueInDic == 4:
        tempString = tempString.replace('</mn>','')
        tempString = tempString.replace('</mi>','')
        if tempString.find('</') != -1:
            isThereSomethingNotIncludedInDic = False
    
    if (not isThereSomethingNotIncludedInDic) and (isThereAnythingSpecial):
        return True
    else:
        return False
    


def convert(inL,outL,string):
    languages = {}

    languages['tex'] = [TexToTree.texToTree, TreeToTex.treeToTex]
    languages['doc'] = [DocToTree.docToTree, TreeToDoc.treeToDoc]
    languages['mathml']=[MathMlToTree.mathMlToTree, TreeToMathMl.treeToMathMl]
            
    return languages[outL][1](languages[inL][0](string))

