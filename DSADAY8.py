#Removing leading zeros from a list of integers: Input:[0,0,1,2,0,3,0,0,4]

# arr=[0,0,1,2,0,3,0,0,4]

# while arr and arr[0]==0:
#     arr.pop(0)
# print(arr)    

#Find th firest Missing positive interger  Input=[3,4,1,1]
# arr=[3,4,1,1]
# positive=set()

# for i in arr:
#     if i > 0:
#         positive.add(i)

# i=1
# while True:
#     if i not in positive:
#         print(i)
#         break
#     i +=1    

#find the smallest missing postitve integer:  INPUT:[7,8,9,11,12]

# arr=[7,8,9,11,12]
# positive=set(arr)
# i=1
# while True:
#     if i not in positive:
#         print(i)
#         break
#     i +=1   


#BINARY SEARCH TREE
class BSTNode:
    def __init__(self, data):   # missing :
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue

    elif nodeValue <= rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)

    else:
        if rootNode.rightchild is None:
            rootNode.rightchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightchild, nodeValue)

def preorderTraversal(rootNode) :
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal (rootNode.leftchild)
    preorderTraversal(rootNode.rightchild)   


def InorderTraversal(rootnode):
    if not rootnode:
        return
    InorderTraversal(rootnode.leftchild)
    print(rootnode.data)
    InorderTraversal(rootnode.rightchild)

def postderTraversal(rootnode):
    if not rootnode:
        return
    postderTraversal(rootnode.leftchild)
    postderTraversal(rootnode.rightchild)
    print(rootnode.data)


def searchNode(rootnode,nodevalue):
    if rootnode.data == nodevalue:
        print ("The value is found") 
    elif nodevalue < rootnode.data:
        if rootnode.leftchild is None:
            return searchNode(rootnode.leftchild, nodevalue)

    else:
        if rootnode.rightchild.data == nodevalue:
            if rootnode.rightchild is None:
                print("THE VALUE IS FOUND")
        else:
            return searchNode(rootnode.rightchild, nodevalue)

        

    
# Creating BST
newBST = BSTNode(None)

insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
insertNode(newBST,10)

print('PreorderTraversal:')
preorderTraversal(newBST)
print('InorderTRAVERSAL:-------------------')
InorderTraversal(newBST)
print('postorderTraversal:--------')
postderTraversal(newBST)

print(searchNode(newBST,60))
print(searchNode(newBST,100))
# print(searchNode(newBST,25))








print(newBST.data)                 # 70
print(newBST.leftchild.data)       # 50
print(newBST.rightchild.data)      # 90
print(newBST.leftchild.leftchild.data)   # 30