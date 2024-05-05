class Tree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def parse(data):
    if isinstance(data,tuple) and len(data)==3:
        node=Tree(data[1])
        node.left=parse(data[0])
        node.right=parse(data[2])
    elif data is None:
        node=None
    else:
        node=Tree(data)
    return node

tuple1=((1,3,None),2,((None,3,4),5,(6,7,8)))

treeGenerated=parse(tuple1)

#print(treeGenerated.left.key)



                #                             2
                #             3                               5
                # 1                                  3                7
                #                                         4       6       8

#tree to tuple

output=()
def parseTree(node):
    if node is None:
        return None
    else:
        return (parseTree(node.left),node.key,parseTree(node.right))

print(parseTree(treeGenerated))

def tree_to_tuple(node):
    if(node.left==None and node.right==None):
        return node.key
    return (tree_to_tuple(node.left) if node.left is not None else None,node.key,tree_to_tuple(node.right) if node.right is not None else None)

print(tree_to_tuple(treeGenerated))


