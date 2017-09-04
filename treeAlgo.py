# BinaryTree function simply constructs a list with a root node
# and two empty sublists for the children
# this code build the tree from bottom up


def BinaryTree(r):  # formalized definition of a tree data structure
    return [r, [], []]  # r being the root/parent and the brackets the children


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
m = getRightChild(r)
print(l)
print(m)
print(r)

setRootVal(l, 9)
print(r)
insertLeft(l, 11)
print(r)
print(getRightChild(getRightChild(r)))


