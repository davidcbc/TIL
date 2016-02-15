from BinaryTree import BinaryNode, BinaryTree

################################################################################
# Setup functions for tests                                                    #
################################################################################
def setupOneAdd():
    x = BinaryTree()
    x.add(10)
    return x

def setupTwoAddsLeft():
    x = BinaryTree()
    x.add(10)
    x.add(5)
    return x

def setupTwoAddsRight():
    x = BinaryTree()
    x.add(10)
    x.add(15)
    return x

def setupMultipleAdds():
    x = BinaryTree()
    x.add(10)
    x.add(5)
    x.add(19)
    x.add(17)
    x.add(16)
    x.add(18)
    x.add(20)
    x.add(23)
    return x

################################################################################
# BinaryTree tests                                                             #
################################################################################

####                            Empty Tree tests                            ####
# The headNode of a new tree is None
def testEmptyTree():
    x = BinaryTree()
    assert x.headNode is None

def testDeleteEmptyTreeFalse():
    x = BinaryTree()
    assert x.delete(1) is False
    
####                            One value tests                             ####
def testOneAddHeadNotNone():
    x = setupOneAdd()
    assert x.headNode is not None

def testOneAddHeadValue():
    x = setupOneAdd()
    assert x.headNode.value is 10

def testOneAddHeadParent():
    x = setupOneAdd()
    assert x.headNode.parentNode is None

def testOneAddFind():
    x = setupOneAdd()
    assert x.find(10)

def testOneAddDepth():
    x = setupOneAdd()
    assert x.depth() is 1

def testDeleteSingleEntryTrue():
    x = setupOneAdd()
    assert x.delete(10) is True

def testDeleteSingleEntryFind():
    x = setupOneAdd()
    x.delete(10)
    assert x.find(10) is False

####                            Two value tests                             ####
def testTwoAddsLeftParent():
    x = setupTwoAddsLeft()
    assert x.headNode.leftNode.parentNode is x.headNode
    
def testTwoAddsLeftFind():
    x = setupTwoAddsLeft()
    assert x.find(10)
    assert x.find(5)
    
def testTwoAddsLeftDepth():
    x = setupTwoAddsLeft()
    assert x.depth() is 2

def testTwoAddsRightParent():
    x = setupTwoAddsRight()
    assert x.headNode.rightNode.parentNode is x.headNode

def testTwoAddsRightFind():
    x = setupTwoAddsRight()
    assert x.find(10)
    assert x.find(15)

def testTwoAddsRightDepth():
    x = setupTwoAddsRight()
    assert x.depth() is 2

def testDeleteLeftLeafTrue():
    x = setupTwoAddsLeft()
    assert x.delete(5) is True

def testDeleteLeftLeafFind():
    x = setupTwoAddsLeft()
    x.delete(5)
    assert x.find(5) is False

def testDeleteLeftLeafNodeNone():
    x = setupTwoAddsLeft()
    x.delete(5)
    assert x.headNode.leftNode is None
    
def testDeleteRightLeafTrue():
    x = setupTwoAddsRight()
    assert x.delete(15) is True

def testDeleteRightLeafFind():
    x = setupTwoAddsRight()
    x.delete(15)
    assert x.find(15) is False

def testDeleteRightLeafNodeNone():
    x = setupTwoAddsRight()
    x.delete(15)
    assert x.headNode.rightNode is None

def testDeleteHeadLeftChildFind():
    x = setupTwoAddsLeft()
    x.delete(10)
    assert x.find(10) is False

def testDeleteHeadLeftChildFindChildValue():
    x = setupTwoAddsLeft()
    x.delete(10)
    assert x.find(5) is True

def testDeleteHeadLeftChildNone():
    x = setupTwoAddsLeft()
    x.delete(10)
    assert x.headNode.leftNode is None

def testDeleteHeadRightChildFind():
    x = setupTwoAddsRight()
    x.delete(10)
    assert x.find(10) is False

def testDeleteHeadRightChildFindChildValue():
    x = setupTwoAddsRight()
    x.delete(10)
    assert x.find(15) is True

def testDeleteHeadRightChildNone():
    x = setupTwoAddsLeft()
    x.delete(10)
    assert x.headNode.rightNode is None


####                            Multiple value tests                        ####
def testMultipleAddsFind():
    x = setupMultipleAdds()
    assert x.find(10)
    assert x.find(5)
    assert x.find(19)
    assert x.find(17)
    assert x.find(20)
    assert x.find(16)
    assert x.find(18)
    assert x.find(23)

def testMultipleAddsDepth():
    x = setupMultipleAdds()
    assert x.depth() is 4

def testMinimum():
    x = setupMultipleAdds()
    assert x.headNode.findMinimum() is 5

def testMaximum():
    x = setupMultipleAdds()
    assert x.headNode.findMaximum() is 23

def testDeleteHeadTwoChildrenFind():
    x = setupMultipleAdds()
    x.delete(10)
    assert x.find(10) is False

def testDeleteHeadTwoChildrenFindChildValues():
    x = setupMultipleAdds()
    x.delete(10)
    assert x.find(5) is True
    assert x.find(16) is True
    assert x.find(23) is True

def testDeleteHeadTwoChildrenHeadValue():
    x = setupMultipleAdds()
    x.delete(10)
    assert x.headNode.value is 16
    
def testDeleteHeadTwoChildrenFindMissingChildValue():
    x = setupMultipleAdds()
    x.delete(10)
    assert x.headNode.rightNode.find(16) is False

def testDeleteNodeTwoChildrenFind():
    x = setupMultipleAdds()
    x.delete(19)
    assert x.find(19) is False

def testDeleteNodeTwoChildrenValue():
    x = setupMultipleAdds()
    x.delete(19)
    assert x.headNode.rightNode.value is 20

def testDeleteNodeTwoChildrenChildValue():
    x = setupMultipleAdds()
    x.delete(19)
    assert x.headNode.rightNode.rightNode.value is 23

####                            To String tests                             ####
def testPrintSingleNode():
    x = BinaryNode()
    x.value = 10
    assert x.toString() == "Value: 10"

def testPrintTwoNodesLeft():
    x = BinaryNode()
    x.value = 10
    x.leftNode = BinaryNode()
    x.leftNode.value = 5
    print x.toString()
    assert x.toString() == "Value: 10\nLeft node->Value: 5"

def testPrintTwoNodesRight():
    x = BinaryNode()
    x.value = 10
    x.rightNode = BinaryNode()
    x.rightNode.value = 15
    print x.toString()
    assert x.toString() == "Value: 10\nRight node->Value: 15"


def testPrintThreeNodesEven():
    x = BinaryNode()
    x.value = 10
    x.leftNode = BinaryNode()
    x.leftNode.value = 5
    x.rightNode = BinaryNode()
    x.rightNode.value = 15
    print x.toString()
    assert x.toString() == "Value: 10\nLeft node->Value: 5\nRight node->Value: 15"
    
def testPrintFourNodes():
    x = BinaryNode()
    x.value = 10
    x.leftNode = BinaryNode()
    x.leftNode.value = 5
    x.rightNode = BinaryNode()
    x.rightNode.value = 15
    x.leftNode.leftNode = BinaryNode()
    x.leftNode.leftNode.value = 1
    print x.toString()
    assert x.toString() == "Value: 10\nLeft node->Value: 5\nLeft node->Value: 1\nRight node->Value: 15"

