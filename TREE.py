# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child = []

#     def __str__(self, level=0):
#         ret = " " * level + str(self.data) + "\n"

#         for ch in self.child:
#             ret += ch.__str__(level + 4)

#         return ret

#     def addChild(self, obj):
#         self.child.append(obj)
#         print("Tree node added")


# # Creating Nodes
# rootnode = Tree("Drinks")

# Hot = Tree("Hot")
# Cold = Tree("Cold")

# Tea = Tree("Tea")
# Coffee = Tree("Coffee")

# Nonalcoholic = Tree("Nonalcoholic")
# Alcoholic = Tree("Alcoholic")


# # Building Tree
# rootnode.addChild(Hot)
# rootnode.addChild(Cold)

# Hot.addChild(Tea)
# Hot.addChild(Coffee)

# Cold.addChild(Nonalcoholic)
# Cold.addChild(Alcoholic)


# # Printing Tree
# print(rootnode)


# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.child=[]
#     def addChild(self,child):
#         self.child.append(child)
#         print("child added")
#     def __str__(self,level=0):
#         ret="      "*level+str(self.data)+"\n"
#         for ch in self.child:
#             ret+=ch.__str__(level+1)
#         return ret
# a = Tree("N1")
# b = Tree("N2")
# c = Tree("N3")
# d = Tree("N4")
# e = Tree("N5")
# f = Tree("N6")
# g = Tree("N7")
# h = Tree("N8")

# a.addChild(b)
# a.addChild(c)
# b.addChild(d)
# b.addChild(e)
# c.addChild(f)
# d.addChild(g)
# d.addChild(h)
# print(a)
