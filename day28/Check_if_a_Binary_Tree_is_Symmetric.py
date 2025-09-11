class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and \
               isMirror(t1.left, t2.right) and \
               isMirror(t1.right, t2.left)

    return isMirror(root.left, root.right) if root else True
