#!/bin/python3

#edges and vertices

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
    

def inorder(node): ##left root right
    if(node is not None):
        inorder(node.left)
        print(node.data)
        inorder(node.right)
    
def preorder(node): ##root left right
    if(node is not None):
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node): ##left right root
    if(node is not None):
        preorder(node.left)
        preorder(node.right)
        print(node.data)

root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)

if __name__ == "__main__":
    print("inorder print")
    inorder(root)
    print("preorder print")
    preorder(root)
    print("postorder print")
    postorder(root)
        