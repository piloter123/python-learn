#! /usr/bin/env
# -- coding:utf-8 --
class Solution(object):
	def diameterOfBinaryTree(self, root):
		self.ans = 0;
	def dfs(root):
		if not root:
			return 0
		left = dfs(root.left);
		right = dfs(root.right);
		self.ans=max(self.ans,left+right);
		return max(left,right)+1
	dfs(root)
	return self.ans
