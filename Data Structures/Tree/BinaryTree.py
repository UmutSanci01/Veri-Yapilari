class Node:
    def __init__(self, data):
        self.data : int = data
        self.right : Node = None
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

    # Delete
    def delete(self, data):
        pass

    # Search − Searches specific data in a tree to check whether it is present or not.
    def search(self, data):
        curr : Node | None = self.root # Belki None olabilir.
        while curr:
            if data == curr.data:
                return curr
            elif data > curr.data: # right
                curr = curr.right # continue to search from right
            elif data < curr.data: # left
                curr = curr.left # continue to search from left
        return



    # Traversal: Depth-First-Search Traversal and Breadth-First-Search Traversal
    def traversal(self) -> list[int]:
        datas : list[int] = []
        def step(node):
            if node:
                # -------------------- In-order Sorted list
                step(node.left)
                datas.append(node.data)
                step(node.right)
                # -------------------- Pre-order
                # datas.append(node.data)
                # step(node.left)
                # step(node.right)
                # -------------------- Post-order
                # step(node.left)
                # step(node.right)
                # datas.append(node.data)


        step(self.root)
        return datas

    # return all leafs of tree
    def leafs(self) -> list[Node]:
        leaf_nodes : list[Node] = []

        def step(node):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                leaf_nodes.append(node.data)
            
            step(node.left)
            step(node.right)
        
        step(self.root)
        return leaf_nodes

    # Given a Binary Search Tree and a value x, find the ceil value of x .Ceil means the smallest node value greater than or equal to the x.
    def ceil(self):
        pass

    # Given a Binary Search Tree and a number x, we have to find the floor of x in the given BST, 
    # where floor means the greatest value node of the BST which is smaller than or equal to x. 
    # if x is smaller than the smallest node of BST then return -1.
    def floor(self):
        pass

    def show(self):
        if self.root is None:
            print("Tree is empty.")
            return

        def step(node, prefix="", is_left=True):
            if node.right:
                step(node.right, prefix + ("│   " if is_left else "    "), False)

            leaf_sign = ""
            if node.left is None and node.right is None: leaf_sign = "^" # leaf indicate
            print(prefix + ("└── " if is_left else "┌── ") + leaf_sign + str(node.data))

            if node.left:
                step(node.left, prefix + ("    " if is_left else "│   "), True)

        step(self.root)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(38)
    tree.insert(11)
    tree.insert(40)
    tree.insert(45)
    tree.insert(22)
    tree.insert(10)
    tree.insert(23)
    tree.insert(22)

    print(tree.traversal())
    print(tree.search(10).payloads)
    print(tree.leafs())

    tree.show()

