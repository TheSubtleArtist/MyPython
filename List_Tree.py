from IPython.display import Image
Image(filename='resources/binary_tree.png')

class Node:
    
    def __init__ (self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)   
        else:
            self.data = data
            
    
    def Inorder(self):
        if self.left:
            self.left.Inorder()
        print(self.data)
        if self.right:
            self.right.Inorder()
    
    def Preorder(self):
        print(self.data)
        if self.left:
            self.left.Preorder()
        if self.right:
            self.right.Preorder()
            
    def Postorder(self):
        if self.left:
            self.left.Postorder()
        if self.right:
            self.right.Postorder()
        print(self.data)


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.Inorder()
root.Preorder()
root.Postorder()