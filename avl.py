"""
CSCE 3110 AVL search tree creation and handling methods
holds name, dob, and address
"""

class Person:
    def __init__(self, val, name, dob, address):
        self.val = val      # val is ID!
        self.name = name
        self.dob = dob
        self.address = address

    def __str__(self):
        return f"ID: {self.val}, Name: {self.name}, DOB: {self.dob}, Address: {self.address}"

class TreeNode(object): # Node class for tree
    def __init__(self, person):
        self.left = None
        self.right = None
        self.height = 1

        self.person = person


class AVLTree(object):  # AVL implementation
    def __init__(self):
        self.root = None

    # rotate functions
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # rotation
        y.left = z
        z.right = T2

        # update height
        z.height = 1+max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1+max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
        
        return y    # new root

    def rightRotate(self, z):    
        y = z.left
        T3 = y.right

        # rotation
        y.right = z
        z.left = T3

        # height
        z.height = 1+max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1+max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
        
        return y    # new root
    

    # get height and the balance
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)


    # search functions
    def find_person(self, val):       # search by id
        return self._find_person(self.root, val)

    def _find_person(self, node, val):
        if not node:
            return None  # If the tree is empty or the value is not found
        
        if val == node.person.val:
            return node.person  # Found the person with the matching value
        
        # If val is smaller than the current node's value, search left
        if val < node.person.val:
            return self._find_person(node.left, val)
        # If val is larger than the current node's value, search right
        elif val > node.person.val:
            return self._find_person(node.right, val)

    def find_by_name(self, name):       # Search by name
        return self._find_by_name(self.root, name)

    def _find_by_name(self, node, name):
        found = []
        if not node:
            return found  # If the tree is empty or the value is not found
        
        if name == node.person.name:
            found.append(node.person)  # Found the person with the matching name
        
        # Search both subtrees regardless of the comparison result
        found.extend(self._find_by_name(node.left, name))
        found.extend(self._find_by_name(node.right, name))

        return found



    # insert into tree
    def insert(self, root, person):         # insert new node into tree 
        if not root:
            return TreeNode(person)
        if person.val < root.person.val:
            root.left = self.insert(root.left, person)
        else:
            root.right = self.insert(root.right, person)

        # update height
        root.height = 1 + max(self.getHeight(root.left),
                        self.getHeight(root.right))
        
        # get balance factor
        balance = self.getBalance(root)

        # if unbalanced, try:
        if balance > 1 and person.val < root.left.person.val:
            return self.rightRotate(root)
        if balance < -1 and person.val > root.right.person.val:
            return self.leftRotate(root)
        if balance > 1 and person.val > root.left.person.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and person.val < root.right.person.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    
    def insert_person(self, person):
        self.root = self.insert(self.root, person)


    # delete from tree
    def delete(self, root, val):            # delete using id
        if not root:
            return root

        if val < root.person.val:
            root.left = self.delete(root.left, val)
        elif val > root.person.val:
            root.right = self.delete(root.right, val)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.person = temp.person
            root.right = self.delete(root.right, temp.person.val)

        if not root:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete_person(self, key):
        self.root = self.delete(self.root, key)

    def min_value_node(self, node):         # get the minimum val node
        current = node
        while current.left is not None:
            current = current.left
        return current

    def update(self, root, val, new_name, new_address):
        if not root:
            return False  # ID not found in the tree
        
        if val == root.person.val:
            root.person.name = new_name
            root.person.address = new_address
            return True  # ID found and updated successfully
        
        # If val is smaller than the current node's value, search left
        if val < root.person.val:
            return self.update(root.left, val, new_name, new_address)
        # If val is larger than the current node's value, search right
        elif val > root.person.val:
            return self.update(root.right, val, new_name, new_address)

    def update_person(self, val, new_name, new_address):
        return self.update(self.root, val, new_name, new_address)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print("ID:", root.person.val, "Name:", root.person.name, "DOB:", root.person.dob, "\nAddress:", root.person.address, "\n")
            self.inorder_traversal(root.right)

    def print_tree(self):
        self.inorder_traversal(self.root)
