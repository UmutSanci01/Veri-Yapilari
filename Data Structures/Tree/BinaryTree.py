class Node:
    def __init__(self, data):
        self.data = data
        self.rigt : Node = None
        self.left : Node = None
        self.payloads : list[Node] = [data] # list of same datas

class BinaryTree:
    def __init__(self):
        self.root : Node = None

    # Insert − Inserts data in a tree.
    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return

        temp = self.root        
        while temp:
            if data > temp.data: # right
                if temp.right:
                    temp = temp.right # continue from right
                else: # temp.right == None
                    temp.right = node
                    break
            elif data == temp.data: # list of same datas
                # # Append data instead of the node object 
                # because we no longer need the left and right pointers.
                temp.payloads.append(data) 
                break
            else: # left
                if temp.left:
                    temp = temp.left # continue from left
                else: # temp.left == None
                    temp.left = node
                    break

    # Search − Searches specific data in a tree to check whether it is present or not.
    def search(self, data):
        pass
    
    # Traversal: Depth-First-Search Traversal and Breadth-First-Search Traversal
    def traversal(self):
        pass