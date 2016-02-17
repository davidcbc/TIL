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
        if self.balance is 2 and self.left_node.balance is -1:
            self.left_node.rotate_left()
            self.left_node.parent = self
            self.rotate_right()
        if self.balance is 2 and self.left_node.balance is 1:
            self.rotate_right()
        if self.balance is -2 and self.right_node.balance is 1:
            self.right_node.rotate_right()
            self.right_node.parent = self
            self.rotate_left()
        if self.balance is -2 and self.right_node.balance is -1:
            self.rotate_left()
    def delete(self, value):
        if super(AVLNode, self).delete(value) is True:
            if self is None:
                return True
            else:
                if value < self.value:
                    self.balance = self.balance - 1
                    self.left_depth = self.left_depth - 1    
                else:
                    self.balance = self.balance + 1
                    self.right_depth = self.right_depth - 1
                return True
        else:
            return False
        
        
    def rotate_right(self):
        y = self.left_node
        t3 = self.left_node.right_node
        self.left_node = t3
        y.right_node = self
        y.parent_node = self.parent_node
        self.parent_node = y
        if self.parent_node.parent_node is not None:
            self.parent_node.parent_node.right_node = y
        if t3 is not None:
            t3.parent_node = self
        new_left_depth = y.right_depth
        y.left_depth = self.left_depth - 1
        y.right_depth = self.right_depth + 1
        self.left_depth = new_left_depth
        y.balance = y.left_depth - y.right_depth
        self.balance = self.left_depth - self.right_depth

    def rotate_left(self):
        y = self.right_node
        t3 = self.right_node.left_node
        self.right_node = t3
        y.left_node = self
        y.parent_node = self.parent_node
        self.parent_node = y
        if self.parent_node.parent_node is not None:
            self.parent_node.parent_node.left_node = y
        if t3 is not None:
            t3.parent_node = self
        new_right_depth = y.left_depth
        y.right_depth = self.right_depth - 1
        y.left_depth = self.left_depth + 1
        self.right_depth = new_right_depth
        y.balance = y.right_depth - y.left_depth
        self.balance = self.left_depth - self.right_depth


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
                
        
