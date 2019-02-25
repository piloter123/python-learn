
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isSym(root.left,root.right)
    def isSym(self,p,q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return self.isSym(p.left,q.right) and self.isSym(p.right,q.left)
        else:
            return False
        