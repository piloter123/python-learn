'''
求二叉数最大深度
'''
if root==None:
    return 0
    return max(self.maxDepth(root.left),self.maxDepth(root.right))+1