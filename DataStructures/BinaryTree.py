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
    def add(self, new_value):
        if self.value is None:
            self.value = new_value
            return
        if new_value < self.value:
            if self.left_node is None:
                self.left_node = self.__class__._create_new_node()
                self.left_node.parent_node = self
            self.left_node.add(new_value)
        else:
            if self.right_node is None:
                self.right_node = self.__class__._create_new_node()
                self.right_node.parent_node = self
            self.right_node.add(new_value)

    # Determine depth of tree recursively
    def depth(self):
        if self.value is None:
            return 0
        else:
            if self.left_node is None:
                left_depth = 1
            else:
                left_depth = self.left_node.depth() + 1

            if self.right_node is None:
                right_depth = 1
            else:
                right_depth = self.right_node.depth() + 1
            return max(left_depth, right_depth)

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
                return True
            elif self.left_node is not None and self.right_node is None:
                self.value = self.left_node.find_maximum()
                return self.left_node.delete(self.value)
            else:
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

    def make_string(self, rows, depth, max_depth):
        rows[depth] += ("x" * (pow(max_depth - depth, 2) - len(str(self.value)))) + str(self.value)
        if self.left_node is not None:
            self.left_node.make_string(rows, depth + 1, max_depth)
        else:
            current_depth = depth + 1
            while current_depth < max_depth:
                rows[current_depth] += ("x" * (pow(max_depth - current_depth, 2))) + "N"
                current_depth += 1
        if self.right_node is not None:
            self.right_node.make_string(rows, depth + 1, max_depth)
        else:
            current_depth = depth + 1
            while current_depth < max_depth:
                rows[current_depth] += ("x" * (pow(max_depth - current_depth, 2))) + "N"
                current_depth += 1


# Main implementation
class BinaryTree(object):
    head_node = None

    @staticmethod
    def _create_new_node():
        return BinaryNode()

    # Add a new value to the tree
    def add(self, new_value):
        if self.head_node is None:
            self.head_node = self.__class__._create_new_node()
        self.head_node.add(new_value)

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
        return_value = ""
        for i in range(0, depth):
            rows.append("")
        if self.head_node is not None:
            self.head_node.make_string(rows, 0, depth)
        for i in range(0, depth):
            return_value += rows[i] + "\n"
        return return_value
