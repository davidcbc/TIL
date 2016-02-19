from BinaryTree import BinaryNode, BinaryTree


################################################################################
# Setup functions for tests                                                    #
################################################################################
def setup_one_add():
    x = BinaryTree()
    x.add(10)
    return x


def setup_two_adds_left():
    x = BinaryTree()
    x.add(10)
    x.add(5)
    return x


def setup_two_adds_right():
    x = BinaryTree()
    x.add(10)
    x.add(15)
    return x


def setup_multiple_adds():
    x = BinaryTree()
    x.add(10)
    x.add(5)
    x.add(19)
    x.add(17)
    x.add(16)
    x.add(18)
    x.add(23)
    x.add(20)
    return x


################################################################################
# BinaryTree tests                                                             #
################################################################################

#                               Empty Tree tests                               #
# The head_node of a new tree is None
def test_empty_tree():
    x = BinaryTree()
    assert x.head_node is None


def test_delete_empty_tree_false():
    x = BinaryTree()
    assert x.delete(1) is False


#                               One value tests                                #
def test_one_add_head_not_none():
    x = setup_one_add()
    assert x.head_node is not None


def test_one_add_head_value():
    x = setup_one_add()
    assert x.head_node.value is 10


def test_one_add_head_parent():
    x = setup_one_add()
    assert x.head_node.parent_node is None


def test_one_add_find():
    x = setup_one_add()
    assert x.find(10)


def test_one_add_depth():
    x = setup_one_add()
    assert x.depth() is 1


def test_delete_single_entry_true():
    x = setup_one_add()
    assert x.delete(10) is True


def test_delete_single_entry_find():
    x = setup_one_add()
    x.delete(10)
    assert x.find(10) is False


#                               Two value tests                                #
def test_two_adds_left_parent():
    x = setup_two_adds_left()
    assert x.head_node.left_node.parent_node is x.head_node


def test_two_adds_left_find():
    x = setup_two_adds_left()
    assert x.find(10)
    assert x.find(5)


def test_two_adds_left_depth():
    x = setup_two_adds_left()
    assert x.depth() is 2


def test_two_adds_right_parent():
    x = setup_two_adds_right()
    assert x.head_node.right_node.parent_node is x.head_node


def test_two_adds_right_find():
    x = setup_two_adds_right()
    assert x.find(10)
    assert x.find(15)


def test_two_adds_right_depth():
    x = setup_two_adds_right()
    assert x.depth() is 2


def test_delete_left_leaf_true():
    x = setup_two_adds_left()
    assert x.delete(5) is True


def test_delete_left_leaf_find():
    x = setup_two_adds_left()
    x.delete(5)
    assert x.find(5) is False


def test_delete_left_leaf_node_none():
    x = setup_two_adds_left()
    x.delete(5)
    assert x.head_node.left_node is None


def test_delete_right_true():
    x = setup_two_adds_right()
    assert x.delete(15) is True


def test_delete_right_leaf_find():
    x = setup_two_adds_right()
    x.delete(15)
    assert x.find(15) is False


def test_delete_right_leaf_node_none():
    x = setup_two_adds_right()
    x.delete(15)
    assert x.head_node.right_node is None


def test_delete_head_left_child_find():
    x = setup_two_adds_left()
    x.delete(10)
    assert x.find(10) is False


def test_delete_head_left_child_find_child_value():
    x = setup_two_adds_left()
    x.delete(10)
    assert x.find(5) is True


def test_delete_head_left_child_none():
    x = setup_two_adds_left()
    x.delete(10)
    assert x.head_node.left_node is None


def test_delete_head_right_child_find():
    x = setup_two_adds_right()
    x.delete(10)
    assert x.find(10) is False


def test_delete_head_right_child_find_child_value():
    x = setup_two_adds_right()
    x.delete(10)
    assert x.find(15) is True


def test_delete_head_right_child_none():
    x = setup_two_adds_left()
    x.delete(10)
    assert x.head_node.right_node is None


#                               Multiple value tests                           #
def test_multiple_adds_find():
    x = setup_multiple_adds()
    assert x.find(10)
    assert x.find(5)
    assert x.find(19)
    assert x.find(17)
    assert x.find(20)
    assert x.find(16)
    assert x.find(18)
    assert x.find(23)


def test_multiple_adds_depth():
    x = setup_multiple_adds()
    assert x.depth() is 4


def test_minimum():
    x = setup_multiple_adds()
    assert x.head_node.find_minimum() is 5


def test_maximum():
    x = setup_multiple_adds()
    assert x.head_node.find_maximum() is 23


def test_delete_head_two_children_find():
    x = setup_multiple_adds()
    x.delete(10)
    assert x.find(10) is False


def test_delete_head_two_children_find_child_values():
    x = setup_multiple_adds()
    x.delete(10)
    assert x.find(5) is True
    assert x.find(16) is True
    assert x.find(23) is True


def test_delete_head_two_children_head_value():
    x = setup_multiple_adds()
    x.delete(10)
    assert x.head_node.value is 16


def test_delete_head_two_children_find_missing_child_value():
    x = setup_multiple_adds()
    x.delete(10)
    assert x.head_node.right_node.find(16) is False


def test_delete_node_two_children_find():
    x = setup_multiple_adds()
    x.delete(19)
    assert x.find(19) is False


def test_delete_node_two_children_value():
    x = setup_multiple_adds()
    x.delete(19)
    assert x.head_node.right_node.value is 20


def test_delete_node_two_children_child_value():
    x = setup_multiple_adds()
    x.delete(19)
    assert x.head_node.right_node.value is 20
    assert x.head_node.right_node.right_node.value is 23


#                               To String tests                                #
def test_print_single_node():
    x = BinaryNode()
    x.value = 10
    assert x.to_string() == "Value: 10"


def test_print_two_nodes_left():
    x = BinaryNode()
    x.value = 10
    x.left_node = BinaryNode()
    x.left_node.value = 5
    print x.to_string()
    assert x.to_string() == "Value: 10\nLeft node->Value: 5"


def test_print_two_nodes_right():
    x = BinaryNode()
    x.value = 10
    x.right_node = BinaryNode()
    x.right_node.value = 15
    print x.to_string()
    assert x.to_string() == "Value: 10\nRight node->Value: 15"


def test_print_three_nodes_even():
    x = BinaryNode()
    x.value = 10
    x.left_node = BinaryNode()
    x.left_node.value = 5
    x.right_node = BinaryNode()
    x.right_node.value = 15
    print x.to_string()
    assert x.to_string() == "Value: 10\nLeft node->Value: 5\nRight node->Value: 15"


def test_print_four_nodes():
    x = BinaryNode()
    x.value = 10
    x.left_node = BinaryNode()
    x.left_node.value = 5
    x.right_node = BinaryNode()
    x.right_node.value = 15
    x.left_node.left_node = BinaryNode()
    x.left_node.left_node.value = 1
    print x.to_string()
    assert x.to_string() == "Value: 10\nLeft node->Value: 5\nLeft node->Value: 1\nRight node->Value: 15"
