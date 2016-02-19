from AVLTree import AVLNode, AVLTree


################################################################################
# Setup functions for tests                                                    #
################################################################################
def setup_one_add():
    x = AVLTree()
    x.add(1)
    return x


def setup_two_adds_left():
    x = AVLTree()
    x.add(2)
    x.add(1)
    return x


def setup_two_adds_right():
    x = AVLTree()
    x.add(1)
    x.add(2)
    return x


def setup_multiple_adds():
    x = AVLTree()
    x.add(1)
    x.add(2)
    x.add(3)
    x.add(4)
    x.add(5)
    x.add(6)
    x.add(7)
    x.add(8)
    return x


def setup_right_heavy_tree():
    x = AVLTree()
    x.add(1)
    x.add(2)
    x.add(3)
    x.add(4)
    return x


def setup_left_heavy_tree():
    x = AVLTree()
    x.add(4)
    x.add(3)
    x.add(2)
    x.add(1)
    return x


def setup_right_left_heavy_tree():
    x = AVLTree()
    x.add(1)
    x.add(2)
    x.add(4)
    x.add(3)
    return x


def setup_left_right_heavy_tree():
    x = AVLTree()
    x.add(4)
    x.add(3)
    x.add(1)
    x.add(2)
    return x


def setup_complicated_delete():
    x = AVLTree()
    x.add(50)
    x.add(25)
    x.add(75)
    x.add(15)
    x.add(40)
    x.add(60)
    x.add(80)
    x.add(35)
    x.add(55)
    x.add(65)
    x.add(90)
    x.add(62)
    return x


################################################################################
# AVLTree tests                                                                #
################################################################################
#                               AVL Specific tests                             #
def test_one_add_balance_head():
    x = setup_one_add()
    assert x.head_node.balance is 0


def test_one_add_left_depth():
    x = setup_one_add()
    assert x.head_node.left_depth is 0


def test_one_add_right_depth():
    x = setup_one_add()
    assert x.head_node.right_depth is 0


def test_two_adds_left_balance_head():
    x = setup_two_adds_left()
    assert x.head_node.balance is 1


def test_two_adds_left_balance_left():
    x = setup_two_adds_left()
    assert x.head_node.left_node.balance is 0


def test_two_adds_left_left_depth_head():
    x = setup_two_adds_left()
    assert x.head_node.left_depth is 1


def test_two_adds_left_right_depth_head():
    x = setup_two_adds_left()
    assert x.head_node.right_depth is 0


def test_two_adds_right_balance_head():
    x = setup_two_adds_right()
    assert x.head_node.balance is -1


def test_two_adds_right_balance_right():
    x = setup_two_adds_right()
    assert x.head_node.right_node.balance is 0


def test_two_adds_right_depth_head():
    x = setup_two_adds_right()
    assert x.head_node.right_depth is 1


def test_two_adds_right_left_depth_head():
    x = setup_two_adds_right()
    assert x.head_node.left_depth is 0


#   Rotation tests
def test_node_rebalance_left_left_balance():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(10)
    x.add(5)
    x.add(1)
    print x.to_string()
    assert x.head_node.balance is 0
    assert x.head_node.left_node.balance is 0
    assert x.head_node.right_node.balance is 0


def test_node_rebalance_left_left_depth():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(10)
    x.add(5)
    x.add(1)
    assert x.head_node.right_depth is 1
    assert x.head_node.left_depth is 1
    assert x.head_node.right_node.left_depth is 0
    assert x.head_node.right_node.right_depth is 0
    assert x.head_node.left_node.left_depth is 0
    assert x.head_node.left_node.right_depth is 0


def test_node_rebalance_left_left_structure():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(10)
    x.add(5)
    x.add(1)
    print x.to_string()
    assert x.head_node.value is 5
    assert x.head_node.left_node.value is 1
    assert x.head_node.right_node.value is 10


def test_node_rebalance_right_right_balance():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(1)
    x.add(5)
    x.add(10)
    print x.to_string()
    assert x.head_node.balance is 0
    assert x.head_node.left_node.balance is 0
    assert x.head_node.right_node.balance is 0


def test_node_rebalance_right_right_depth():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(1)
    x.add(5)
    x.add(10)
    assert x.head_node.right_depth is 1
    assert x.head_node.left_depth is 1
    assert x.head_node.right_node.left_depth is 0
    assert x.head_node.right_node.right_depth is 0
    assert x.head_node.left_node.left_depth is 0
    assert x.head_node.left_node.right_depth is 0


def test_node_rebalance_right_right_structure():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(1)
    x.add(5)
    x.add(10)
    assert x.head_node.value is 5
    assert x.head_node.left_node.value is 1
    assert x.head_node.right_node.value is 10


def test_node_rebalance_left_right_depth():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(10)
    x.add(1)
    x.add(5)
    print x.to_string()
    assert x.head_node.right_depth is 1
    assert x.head_node.left_depth is 1
    assert x.head_node.right_node.left_depth is 0
    assert x.head_node.right_node.right_depth is 0
    assert x.head_node.left_node.left_depth is 0
    assert x.head_node.left_node.right_depth is 0


def test_node_rebalance_right_left_depth():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(10)
    x.add(15)
    x.add(13)
    print x.to_string()
    assert x.head_node.right_depth is 1
    assert x.head_node.left_depth is 1
    assert x.head_node.right_node.left_depth is 0
    assert x.head_node.right_node.right_depth is 0
    assert x.head_node.left_node.left_depth is 0
    assert x.head_node.left_node.right_depth is 0


def test_node_rebalance_left_right_balance():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(10)
    x.add(1)
    x.add(5)
    print x.to_string()
    assert x.head_node.balance is 0


def test_node_rebalance_right_left_balance():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(10)
    x.add(15)
    x.add(13)
    print x.to_string()
    assert x.head_node.balance is 0


def test_node_rebalance_left_right_structure():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(10)
    x.add(1)
    x.add(5)
    print x.to_string()
    assert x.head_node.value is 5
    assert x.head_node.left_node.value is 1
    assert x.head_node.right_node.value is 10


def test_node_rebalance_right_left_structure():
    x = AVLTree()
    x.head_node = AVLNode()
    x.add(10)
    x.add(15)
    x.add(13)
    print x.to_string()
    assert x.head_node.value is 13
    assert x.head_node.left_node.value is 10
    assert x.head_node.right_node.value is 15


#                               Empty Tree tests                               #
# The head_node of a new tree is None
def test_empty_tree():
    x = AVLTree()
    assert x.head_node is None


def test_delete_empty_tree_false():
    x = AVLTree()
    assert x.delete(1) is False


#                               One value tests                                #
def test_one_add_head_not_none():
    x = setup_one_add()
    assert x.head_node is not None


def test_one_add_head_value():
    x = setup_one_add()
    assert x.head_node.value is 1


def test_one_add_head_parent():
    x = setup_one_add()
    assert x.head_node.parent_node is None


def test_one_add_find():
    x = setup_one_add()
    assert x.find(1)


def test_one_add_depth():
    x = setup_one_add()
    assert x.depth() is 1


def test_delete_single_entry_true():
    x = setup_one_add()
    assert x.delete(1) is True


def test_delete_single_entry_find():
    x = setup_one_add()
    x.delete(1)
    assert x.find(1) is False


#                               Two value tests                                #
def test_two_adds_left_parent():
    x = setup_two_adds_left()
    assert x.head_node.left_node.parent_node is x.head_node


def test_two_adds_left_find():
    x = setup_two_adds_left()
    assert x.find(2)
    assert x.find(1)


def test_two_adds_left_depth():
    x = setup_two_adds_left()
    assert x.depth() is 2


def test_two_adds_right_parent():
    x = setup_two_adds_right()
    assert x.head_node.right_node.parent_node is x.head_node


def test_two_adds_right_find():
    x = setup_two_adds_right()
    assert x.find(1)
    assert x.find(2)


def test_two_adds_right_depth():
    x = setup_two_adds_right()
    assert x.depth() is 2


#                               Multiple value tests                           #
def test_multiple_adds_find():
    x = setup_multiple_adds()
    print x.to_string()
    assert x.find(1)
    assert x.find(2)
    assert x.find(3)
    assert x.find(4)
    assert x.find(5)
    assert x.find(6)
    assert x.find(7)
    assert x.find(8)


def test_multiple_adds_depth():
    x = setup_multiple_adds()
    assert x.depth() is 4


def test_minimum():
    x = setup_multiple_adds()
    assert x.head_node.find_minimum() is 1


def test_maximum():
    x = setup_multiple_adds()
    assert x.head_node.find_maximum() is 8


####################################################
#                   Deletion tests                 #
####################################################

#   Delete and rotate left
def test_delete_rotate_left_balance_calculation():
    x = setup_right_heavy_tree()
    x.delete(1)
    assert x.head_node.balance is 0
    assert x.head_node.left_node.balance is 0
    assert x.head_node.right_node.balance is 0


def test_delete_rotate_left_depth_calculation():
    x = setup_right_heavy_tree()
    x.delete(1)
    assert x.head_node.left_depth is 1
    assert x.head_node.right_depth is 1
    assert x.head_node.left_node.left_depth is 0
    assert x.head_node.left_node.right_depth is 0
    assert x.head_node.right_node.left_depth is 0
    assert x.head_node.right_node.right_depth is 0


def test_delete_rotate_left_structure():
    x = setup_right_heavy_tree()
    x.delete(1)
    assert x.head_node.value is 3
    assert x.head_node.left_node.value is 2
    assert x.head_node.right_node.value is 4


#   Delete and rotate right
def test_delete_rotate_right_balance_calculation():
    x = setup_left_heavy_tree()
    x.delete(4)
    assert x.head_node.balance is 0
    assert x.head_node.left_node.balance is 0
    assert x.head_node.right_node.balance is 0


def test_delete_rotate_rightt_depth_calculation():
    x = setup_left_heavy_tree()
    x.delete(4)
    assert x.head_node.left_depth is 1
    assert x.head_node.right_depth is 1
    assert x.head_node.left_node.left_depth is 0
    assert x.head_node.left_node.right_depth is 0
    assert x.head_node.right_node.left_depth is 0
    assert x.head_node.right_node.right_depth is 0


def test_delete_rotate_right_structure():
    x = setup_left_heavy_tree()
    x.delete(4)
    assert x.head_node.value is 2
    assert x.head_node.left_node.value is 1
    assert x.head_node.right_node.value is 3


#   Delete and rotate right/left
def test_delete_rotate_left_right_balance_calculation():
    x = setup_right_left_heavy_tree()
    x.delete(1)
    assert x.head_node.balance is 0
    assert x.head_node.left_node.balance is 0
    assert x.head_node.right_node.balance is 0


def test_delete_rotate_left_right_depth_calculation():
    x = setup_right_left_heavy_tree()
    x.delete(1)
    assert x.head_node.left_depth is 1
    assert x.head_node.right_depth is 1
    assert x.head_node.left_node.left_depth is 0
    assert x.head_node.left_node.right_depth is 0
    assert x.head_node.right_node.left_depth is 0
    assert x.head_node.right_node.right_depth is 0


def test_delete_rotate_left_right_structure():
    x = setup_right_left_heavy_tree()
    x.delete(1)
    assert x.head_node.value is 3
    assert x.head_node.left_node.value is 2
    assert x.head_node.right_node.value is 4


#   Delete and rotate left/right
def test_delete_rotate_right_left_balance_calculation():
    x = setup_left_right_heavy_tree()
    x.delete(1)
    assert x.head_node.balance is 0
    assert x.head_node.left_node.balance is 0
    assert x.head_node.right_node.balance is 0


def test_delete_rotate_right_left_depth_calculation():
    x = setup_left_right_heavy_tree()
    x.delete(1)
    assert x.head_node.left_depth is 1
    assert x.head_node.right_depth is 1
    assert x.head_node.left_node.left_depth is 0
    assert x.head_node.left_node.right_depth is 0
    assert x.head_node.right_node.left_depth is 0
    assert x.head_node.right_node.right_depth is 0


def test_delete_rotate_right_left_structure():
    x = setup_left_right_heavy_tree()
    x.delete(4)
    assert x.head_node.value is 2
    assert x.head_node.left_node.value is 1
    assert x.head_node.right_node.value is 3


#   Multiple rotation delete test
def test_multiple_rotation_delete():
    x = setup_complicated_delete()
    x.delete(15)
    assert x.head_node.value is 60

    assert x.head_node.left_node.value is 50
    assert x.head_node.left_node.left_node.value is 35
    assert x.head_node.left_node.left_node.left_node.value is 25
    assert x.head_node.left_node.left_node.right_node.value is 40
    assert x.head_node.left_node.left_node.left_node.left_node is None
    assert x.head_node.left_node.left_node.right_node.right_node is None
    assert x.head_node.left_node.right_node.value is 55
    assert x.head_node.left_node.right_node.left_node is None
    assert x.head_node.left_node.right_node.right_node is None

    assert x.head_node.right_node.value is 75
    assert x.head_node.right_node.left_node.value is 65
    assert x.head_node.right_node.left_node.left_node.value is 62
    assert x.head_node.right_node.left_node.left_node.left_node is None
    assert x.head_node.right_node.left_node.left_node.right_node is None
    assert x.head_node.right_node.left_node.right_node is None
    assert x.head_node.right_node.left_node.left_node.value is 62
    assert x.head_node.right_node.right_node.value is 80
    assert x.head_node.right_node.right_node.left_node is None
    assert x.head_node.right_node.right_node.right_node.value is 90
    assert x.head_node.right_node.right_node.right_node.left_node is None
    assert x.head_node.right_node.right_node.right_node.right_node is None


#   Miscellaneous deletion tests
def test_delete_left_leaf_true():
    x = setup_two_adds_left()
    assert x.delete(1) is True


def test_delete_left_leaf_find():
    x = setup_two_adds_left()
    x.delete(2)
    assert x.find(2) is False


def test_delete_left_leaf_node_none():
    x = setup_two_adds_left()
    x.delete(2)
    assert x.head_node.left_node is None


def test_delete_right_true():
    x = setup_two_adds_right()
    assert x.delete(2) is True


def test_delete_right_leaf_find():
    x = setup_two_adds_right()
    x.delete(2)
    assert x.find(2) is False


def test_delete_right_leaf_node_none():
    x = setup_two_adds_right()
    x.delete(2)
    assert x.head_node.right_node is None


def test_delete_head_left_child_find():
    x = setup_two_adds_left()
    x.delete(2)
    assert x.find(2) is False


def test_delete_head_left_child_find_child_value():
    x = setup_two_adds_left()
    x.delete(2)
    assert x.find(1) is True


def test_delete_head_left_child_none():
    x = setup_two_adds_left()
    x.delete(2)
    assert x.head_node.left_node is None


def test_delete_head_right_child_find():
    x = setup_two_adds_right()
    x.delete(2)
    assert x.find(2) is False


def test_delete_head_right_child_find_child_value():
    x = setup_two_adds_right()
    print x.to_string()
    print x.head_node.balance
    x.delete(1)
    print x.head_node.balance
    print x.to_string()
    assert x.find(2) is True


def test_delete_head_right_child_none():
    x = setup_two_adds_left()
    x.delete(2)
    assert x.head_node.right_node is None


#                               To String tests                                #
def test_print_single_node():
    x = AVLNode()
    x.value = 10
    assert x.to_string() == "Value: 10"


def test_print_two_nodes_left():
    x = AVLNode()
    x.value = 10
    x.left_node = AVLNode()
    x.left_node.value = 5
    print x.to_string()
    assert x.to_string() == "Value: 10\nLeft node->Value: 5"


def test_print_two_nodes_right():
    x = AVLNode()
    x.value = 10
    x.right_node = AVLNode()
    x.right_node.value = 15
    print x.to_string()
    assert x.to_string() == "Value: 10\nRight node->Value: 15"


def test_print_three_nodes_even():
    x = AVLNode()
    x.value = 10
    x.left_node = AVLNode()
    x.left_node.value = 5
    x.right_node = AVLNode()
    x.right_node.value = 15
    print x.to_string()
    assert x.to_string() == "Value: 10\nLeft node->Value: 5\nRight node->Value: 15"


def test_print_four_nodes():
    x = AVLNode()
    x.value = 10
    x.left_node = AVLNode()
    x.left_node.value = 5
    x.right_node = AVLNode()
    x.right_node.value = 15
    x.left_node.left_node = AVLNode()
    x.left_node.left_node.value = 1
    print x.to_string()
    assert x.to_string() == "Value: 10\nLeft node->Value: 5\nLeft node->Value: 1\nRight node->Value: 15"
