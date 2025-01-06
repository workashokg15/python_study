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
        

root = Node(5)

if __name__ == "__main__":
    insert(root, Node(10))
    insert(root, Node(8))
    insert(root, Node(6))
    insert(root, Node(12))

    ## 5 10 8 6 12
    print_tree_pre_order(root)
