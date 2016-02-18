import pdb
from BinaryTree import BinaryTree, BinaryNode
class AVLTree(BinaryTree):
    
    @staticmethod
    def _create_new_node():
        return AVLNode()

    def add(self, newValue):
        super(AVLTree, self).add(newValue)
        if self.head_node.parent_node is not None:
            self.head_node = self.head_node.parent_node
            self.head_node.parent_node = None

        self.head_node._test_integrity()
        print "Integrity test done!\n\n"
            
class AVLNode(BinaryNode):
    balance = 0
    left_depth = 0
    right_depth = 0

    @staticmethod
    def _create_new_node():
        return AVLNode()

    def add(self, newValue):
        super(AVLNode, self).add(newValue)
        if self.value is not newValue:
            if newValue < self.value:
                self.left_depth = max(self.left_node.left_depth, self.left_node.right_depth) + 1
            else:
                self.right_depth = max(self.right_node.left_depth, self.right_node.right_depth) + 1
        self.balance =  self.left_depth - self.right_depth
        if self.balance is 2 and self.left_node is not None and self.left_node.balance is -1:
            print "Balance is 2, rotate left then right"
            self.left_node.rotate_left()
            self.left_node.parent = self
            self.rotate_right()
        if self.balance is 2 and self.left_node is not None and self.left_node.balance is 1:
            print "Balance is 2, rotate right"
            self.rotate_right()
        if self.balance is -2 and self.right_node is not None and self.right_node.balance is 1:
            print "Balance is -2, rotate right then left"
            self.right_node.rotate_right()
            self.right_node.parent = self
            self.rotate_left()
        if self.balance is -2 and self.right_node is not None and self.right_node.balance is -1:
            print "Balance is -2, rotate left"
            print "self.value: " + str(self.value)
            print "self.right_node.value: " + str(self.right_node.value)
            print "self.right_node.right_node.value: " + str(self.right_node.right_node.value)
            self.rotate_left()

            
    def delete(self, value):
        if super(AVLNode, self).delete(value) is True:
            if self is None:
                return True
            else:
                self.left_depth = 0 if self.left_node is None else max(self.left_node.left_depth, self.left_node.right_depth) + 1
                self.right_depth = 0 if self.right_node is None else max(self.right_node.left_depth, self.right_node.right_depth) + 1
                self.balance = self.left_depth - self.right_depth
                if self.balance is 2 and self.left_node is not None and self.left_node.balance is -1:
                    self.left_node.rotate_left()
                    self.left_node.parent = self
                    self.rotate_right()
                if self.balance is 2 and self.left_node is not None and self.left_node.balance is 1:
                    self.rotate_right()
                if self.balance is -2 and self.right_node is not None and self.right_node.balance is 1:
                    self.right_node.rotate_right()
                    self.right_node.parent = self
                    self.rotate_left()
                if self.balance is -2 and self.right_node is not None and self.right_node.balance is -1:
                    self.rotate_left()
                return True
        else:
            return False
        
################################################################################
## Right rotation around z
##               z                   y
##              / \                 / \
##             y   t1  ----->      t3  z
##            / \                     / \
##           t3  t2                  t2  t1
##
################################################################################        
    def rotate_right(self):
        z = self
        y = self.left_node
        t1 = z.right_node
        t2 = y.right_node
        z_parent = z.parent_node
        
        z.left_node = t2
        y.right_node = z
        y.parent_node = z_parent
        z.parent_node = y

        if t2 is not None:
            t2.parent_node = z
        if z_parent is not None:
            if z_parent.value < y.value:
                z_parent.right_node = y
            else:
                z_parent.left_node = y
                
        new_left_depth = y.right_depth
        y.left_depth = z.left_depth - 1
        y.right_depth = z.right_depth + 1
        z.left_depth = new_left_depth
        y.balance = y.right_depth - y.left_depth
        z.balance = z.left_depth - z.right_depth

################################################################################
## Left rotation around z
##               z                    y
##              / \                  / \
##             t1  y   ------>      z   t3
##                / \              / \
##               t2  t3           t1  t2
##
################################################################################
    def rotate_left(self):
        z = self
        y = self.right_node
        t1 = z.left_node
        t2 = y.left_node
        z_parent = z.parent_node
        
        z.right_node = t2
        y.left_node = z
        y.parent_node = z_parent
        z.parent_node = y

        if t2 is not None:
            t2.parent_node = z
        if z_parent is not None:
            if z_parent.value < y.value:
                z_parent.right_node = y
            else:
                z_parent.left_node = y
                
        new_right_depth = y.left_depth
        y.right_depth = z.right_depth - 1
        y.left_depth = z.left_depth + 1
        z.right_depth = new_right_depth
        y.balance = y.right_depth - y.left_depth
        z.balance = z.left_depth - z.right_depth


    def _test_integrity(self):
        print "Checking integrity of node with value " + str(self.value)
        if self.left_node is not None:
            if self.left_node.parent_node is self:
                print "self.left_node.parent_node checks out, continuing..."
                self.left_node._test_integrity()
                print "back in parent"
            else:
                print "self.left_node.parent_node is WRONG"
        else:
            print "no left node"
        if self.right_node is not None:
            if self.right_node.parent_node is self:
                print "self.right_node.parent_node checks out, continuing"
                self.right_node._test_integrity()
                print "back in parent"
            else:
                print "self.right_node.parent_node is WRONG"
        else:
            print "no right node"
                
        
