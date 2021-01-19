import DocToTree
import TreeToDoc
import TexToTree
import TreeToTex


def convert(inL,outL,string):
    languages = {}

    languages['tex'] = [TexToTree.texToTree, TreeToTex.treeToTex]
    languages['doc'] = [DocToTree.docToTree, TreeToDoc.treeToDoc]
            
    return languages[outL][1](languages[inL][0](string))
