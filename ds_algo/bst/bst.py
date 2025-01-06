#!/bin/python3


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

     
def print_tree_pre_order(node):
    if(node is not None):
        print(node.data)
        print_tree_pre_order(node.left)
        print_tree_pre_order(node.right)


def insert(root, node):
    if(root is None):
        root = node
        return
    if(node.data < root.data):
        if(root.left == None):
            root.left = node
        else:
            insert(root.left, node)
    if(node.data > root.data):
        if(root.right == None):
            root.right = node
        else:
            insert(root.right, node)


def minimum_value(node):
    if node.left is None:
        return node
    return minimum_value(node.left)
    


def delete(node, key):
    if(node is None):
        return node
    if(key < node.data):
        node.left = delete(node.left, key)
    elif(key > node.data):
        node.right = delete(node.right, key)
    else:
        if(node.left is None):
            temp = node.right
            del node
            return temp
        elif(node.right is None):
            temp = node.left
            del node
            return temp
        temp = minimum_value(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)
    return node
    


def search(node, key):
    if(node is None):
        print("no node found")
        return None
    print("current node is: ", node.data)
    if(node.data == key):
        print("found the node")
        return node
    if(key > node.data):
        return search(node.right, key)
    return search(node.left, key)


root = Node(5)

if __name__ == "__main__":
    insert(root, Node(3))
    insert(root, Node(4))
    insert(root, Node(2))
    insert(root, Node(10))
    insert(root, Node(8))
    insert(root, Node(6))
    insert(root, Node(12))
    insert(root, Node(14))

    ## 5 3 2 4 10 8 6 12
    print_tree_pre_order(root)
    print("searching 8")
    result = search(root, 8)
    if(result is not None):
        print("Node found at address : ", result, " with value : ", result.data)

    print("searching 7")
    result = search(root, 7)
    if(result is not None):
        print("Node found at address : ", result, " with value : ", result.data)
    else:
        print("Node not present with data")

    delete(root, 7)
    print_tree_pre_order(root)

    print("DELETING 8")
    delete(root, 8)
    print_tree_pre_order(root)
    print("DELETING 12")
    delete(root,12)
    print_tree_pre_order(root)
    print("DELETING 5")
    delete(root,5)
    print_tree_pre_order(root)
