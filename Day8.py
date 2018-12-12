from Tree import Tree

# trees = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
trees = open('D8.txt','r').read()
trees = trees.split(' ')
for i in range(0,len(trees)):
    trees[i] = int(trees[i])

# def getmeta(start):
#     global trees, metaSum
#     if start < len(trees):
#         info = []
#         info.append(start)
#         num_child = trees[start]
#         num_meta = trees[start+1]
#         next = start+2
#         if num_child > 0:
#             for i in range(0,num_child):
#                 next = getmeta(next)
#         tempMeta = []
#         for i in range(next,next+num_meta):
#             tempMeta.append(trees[i])
#         info.append(tempMeta)
#         metaSum.insert(0,info)
#         return next+num_meta
#     return -1

allTrees = []

def makeTrees(start):
    global trees
    if start < len(trees):
        num_child = trees[start]
        num_meta = trees[start+1]
        curTree = Tree(start, num_child, num_meta)
        if curTree not in allTrees:
            allTrees.append(curTree)
        next = start+2
        if num_child > 0:
            for i in range(0,num_child):
                curTree.children.append(next)
                next = makeTrees(next)
        for i in range(next,next+num_meta):
            curTree.metadata.append(trees[i])
        return next+num_meta
    return -1

def getTree(root):
    global allTrees
    for tree in allTrees:
        if tree.start == root:
            return tree
    return None

def getvalue(cur):
    global trees, allTrees
    if cur.child_count == 0:
        return cur.sum_meta()
    else:
        value = 0
        for meta in cur.metadata:
            ind = meta-1
            if ind < cur.child_count:
                value += getvalue(getTree(cur.children[ind]))
        return value


# part1 = True
# if part1:
#     metaSum = []
#     getmeta(0)
#     print metaSum

makeTrees(0)
allTrees.sort()
print getvalue(allTrees[0])
