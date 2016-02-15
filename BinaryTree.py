###################################
# Implementation of a Binary Tree #
###################################

# Node class for BinaryTree
class BinaryNode:
    leftNode = None
    rightNode = None
    parentNode = None
    value = None

    # Recursively add newValue to tree
    def add(self, newValue):
        if self.value is None:
            self.value = newValue
            return
        if newValue < self.value:
            if self.leftNode is None:
                self.leftNode = BinaryNode()
                self.leftNode.parentNode = self
            self.leftNode.add(newValue)
        else:
            if self.rightNode is None:
                self.rightNode = BinaryNode()
                self.rightNode.parentNode = self
            self.rightNode.add(newValue)

    # Determine depth of tree recursively
    def depth(self):
        if self.value is None:
            return 0
        else:
            if self.leftNode is None:
                leftDepth = 1
            else:
                leftDepth = self.leftNode.depth()+1

            if self.rightNode is None:
                rightDepth = 1
            else:
                rightDepth = self.rightNode.depth()+1
            return max(leftDepth, rightDepth)

    # Find value in tree recursively.
    # Return True if found and False if not found
    def find(self, value):
        if self.value is value:
            return True
        else:
            if value < self.value and self.leftNode is not None:
                return self.leftNode.find(value)
            elif self.rightNode is not None:
                return self.rightNode.find(value)
            else:
                return False

    # Determine the minimum value starting at this node recursively
    def findMinimum(self):
        if self.leftNode is None:
            return self.value
        return self.leftNode.findMinimum()

    # Determine the maximum value starting at this node recursively
    def findMaximum(self):
        if self.rightNode is None:
            return self.value
        return self.rightNode.findMaximum()

    # Delete value from the tree recursively
    # Return True if the value was in the tree
    # Return False if the value was not in the tree
    def delete(self, value):
        if self.value is value:
            print "Found " + str(value)
            if self.leftNode is None and self.rightNode is None:
                if self.parentNode is not None and self.parentNode.value >= value:
                    self.parentNode.leftNode = None
                elif self.parentNode is not None:
                    self.parentNode.rightNode = None
                self.value = None
                self = None
                return True
            elif self.leftNode is not None and self.rightNode is None:
                self.value = self.leftNode.findMaximum()
                return self.leftNode.delete(self.value)
            else:
                self.value = self.rightNode.findMinimum()
                return self.rightNode.delete(self.value)       
        else:
            if self.value is None:
                return False
            else:
                if self.value >= value and self.leftNode is not None:
                    return self.leftNode.delete(value)
                elif self.value < value and self.rightNode is not None:
                    return self.rightNode.delete(value)
                else:
                    return False

    # Print the value of the node and it's children nodes
    def toString(self):
        toString = "Value: " + str(self.value)
        if self.leftNode is not None:
            toString += "\nLeft node->" + self.leftNode.toString()
        if self.rightNode is not None:
            toString += "\nRight node->" + self.rightNode.toString()
        return toString

# Main implementation
class BinaryTree:
    headNode = None

    # Add a new value to the tree
    def add(self, newValue):
        if self.headNode is None:
            self.headNode = BinaryNode()
        self.headNode.add(newValue)

    # Determine the depth of the tree
    def depth(self):
        if self.headNode is None or self.headNode.value is None:
            return 0
        else:
            return self.headNode.depth()
    # Find a value in the tree
    # Return True if found and False if not found
    def find(self, value):
        if self.headNode is not None:
            return self.headNode.find(value)
        else:
            return False

    # Delete a value from the tree
    # Return True if value is found and deleted, False if not found
    def delete(self, value):
        if self.headNode is not None:
            return self.headNode.delete(value)
        else:
            return False
