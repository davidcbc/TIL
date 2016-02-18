###################################
# Implementation of a Binary Tree #
###################################

# Node class for BinaryTree
class BinaryNode(object):
    left_node = None
    right_node = None
    parent_node = None
    value = None

    @staticmethod
    def _create_new_node():
        return BinaryNode()
    
    # Recursively add newValue to tree
    def add(self, newValue):
        if self.value is None:
            self.value = newValue
            return
        if newValue < self.value:
            if self.left_node is None:
                self.left_node = self.__class__._create_new_node()
                self.left_node.parent_node = self
            self.left_node.add(newValue)
        else:
            if self.right_node is None:
                self.right_node = self.__class__._create_new_node()
                self.right_node.parent_node = self
            self.right_node.add(newValue)

    # Determine depth of tree recursively
    def depth(self):
        if self.value is None:
            return 0
        else:
            if self.left_node is None:
                leftDepth = 1
            else:
                leftDepth = self.left_node.depth()+1

            if self.right_node is None:
                rightDepth = 1
            else:
                rightDepth = self.right_node.depth()+1
            return max(leftDepth, rightDepth)

    # Find value in tree recursively.
    # Return True if found and False if not found
    def find(self, value):
        if self.value is value:
            return True
        else:
            if value < self.value and self.left_node is not None:
                return self.left_node.find(value)
            elif self.right_node is not None:
                return self.right_node.find(value)
            else:
                return False

    # Determine the minimum value starting at this node recursively
    def find_minimum(self):
        if self.left_node is None:
            return self.value
        return self.left_node.find_minimum()

    # Determine the maximum value starting at this node recursively
    def find_maximum(self):
        if self.right_node is None:
            return self.value
        return self.right_node.find_maximum()

    # Delete value from the tree recursively
    # Return True if the value was in the tree
    # Return False if the value was not in the tree
    def delete(self, value):
        if self.value is value:
            if self.left_node is None and self.right_node is None:
                print "Now I'm in here as expected: " + str(self.value)
                
                if self.parent_node is not None and self.parent_node.value > value:
                    self.parent_node.left_node = None
                elif self.parent_node is not None and self.parent_node.value < value:
                    self.parent_node.right_node = None
                elif self.parent_node is not None:
                    if self.parent_node.left_node is self:
                        self.parent_node.left_node = None
                    else:
                        self.parent_node.right_node = None
                self.value = None
                self = None
                return True
            elif self.left_node is not None and self.right_node is None:
                self.value = self.left_node.find_maximum()
                return self.left_node.delete(self.value)
            else:
                print "Going in here as expected"
                self.value = self.right_node.find_minimum()
                return self.right_node.delete(self.value)       
        else:
            if self.value is None:
                return False
            else:
                if self.value >= value and self.left_node is not None:
                    return self.left_node.delete(value)
                elif self.value < value and self.right_node is not None:
                    return self.right_node.delete(value)
                else:
                    return False

    # Print the value of the node and it's children nodes
    def to_string(self):
        to_string = "Value: " + str(self.value)
        if self.left_node is not None:
            to_string += "\nLeft node->" + self.left_node.to_string()
        if self.right_node is not None:
            to_string += "\nRight node->" + self.right_node.to_string()
        return to_string

    def make_string(self, rows, depth, maxDepth):
        print "Depth: " + str(depth) + " Max Depth: " + str(maxDepth)
        rows[depth] += ("x"*(pow(maxDepth-depth,2)-len(str(self.value)))) + str(self.value)
        if self.left_node is not None:
            print "Going into left node: " + str(self.left_node.value)
            self.left_node.make_string(rows, depth+1, maxDepth)
        else:
            currDepth = depth+1
            while currDepth < maxDepth:
                rows[currDepth] += ("x"*(pow(maxDepth-currDepth,2))) + "N"
                currDepth += 1
        if self.right_node is not None:
            print "Going into right node: " + str(self.right_node.value)
            self.right_node.make_string(rows, depth+1, maxDepth)
        else:
            currDepth = depth+1
            while currDepth < maxDepth:
                rows[currDepth] += ("x"*(pow(maxDepth-currDepth,2))) + "N"
                currDepth += 1
        
# Main implementation
class BinaryTree(object):
    head_node = None

    @staticmethod
    def _create_new_node():
        return BinaryNode()
    
    # Add a new value to the tree
    def add(self, newValue):
        if self.head_node is None:
            self.head_node = self.__class__._create_new_node()
        self.head_node.add(newValue)

    # Determine the depth of the tree
    def depth(self):
        if self.head_node is None or self.head_node.value is None:
            return 0
        else:
            return self.head_node.depth()
    # Find a value in the tree
    # Return True if found and False if not found
    def find(self, value):
        if self.head_node is not None:
            return self.head_node.find(value)
        else:
            return False

    # Delete a value from the tree
    # Return True if value is found and deleted, False if not found
    def delete(self, value):
        if self.head_node is not None:
            return self.head_node.delete(value)
        else:
            return False

    def to_string(self):
        depth = self.depth()
        rows = []
        retVal = ""
        for i in range(0,depth):
            rows.append("")
        if self.head_node is not None:
            self.head_node.make_string(rows, 0, depth)
        for i in range(0, depth):
            retVal += rows[i] + "\n"
        return retVal
        
