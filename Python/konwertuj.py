import TexToTree
import TreeToTex
import DocToTree
import TreeToDoc




def convert(input,output,string):
    if input=='doc' and output=='tex':
        return TreeToTex.treeToTex(DocToTree.docToTree(string))
    if input =='tex' and output=='doc':
        return TreeToDoc.treeToDoc(TexToTree.textToTree(string))



# print(convert('tex','doc','-b\sqrt{-b^{2^{3}}-4ac}+(-5+a)b+3\sin(\\alpha-5e)'))