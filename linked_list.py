"""
CSCE 3110 Linked list creation and handling methods
containing student information such as: id, name, dob, and addresses
"""
class PersonLL:
    def __init__(self, id, name, dob, address):
        self.id = id   
        self.name = name
        self.dob = dob
        self.address = address

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}, Address: {self.address}"


class Node:         # Node Implementation with id, name, dob, address(all in one)
    def __init__(self, person):
        self.person = person
        self.next = None
   

class LinkedList:   # Linked List Implementation
    def __init__(self):
        self.head = None
    
    def insert(self, person, index):
        newNode = Node(person)

        if index <= 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        current = self.head
        prev = None
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if prev:
            prev.next = newNode
            newNode.next = current

    def insertAtBegin(self, person):        # insert at the start of the linked list
        new_node = Node(person)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            
            
    def get_id_index(self, id):                             # fetches index for specified id requested
        cur_index = 0
        cur_node = self.head
        while cur_node:        # O(n) time complexity
            person = cur_node.person
            if person.id==id:
                return cur_node
            cur_node = cur_node.next
            cur_index+=1
        #print("ID not in list!")
        return None 
    
    def get_name_index(self, name):                         # fetches index for name requested
        cur_index = 0
        cur_node = self.head
        while cur_node:        # O(n) time complexity
            person = cur_node.person
            if person.name==name: 
                return cur_node
            cur_node = cur_node.next
            cur_index+=1
       
        return None 
    
    def get_data(self, id):                                 # get data at index (can be improved for time complexity)
        index = self.get_id_index(id)
        cur_node = self.head
        for n in range (index):
            cur_node = cur_node.next
        return cur_node.person.name

    def delete(self, id):
        current = self.head
        prev = None

        while current:
            if current.person.id == id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

        #if ID is not found 
        print("Student with ID: ", id, "was not found")

    def delete_first_node(self):                            # delete the first item in list
        if(self.head == None): return
        self.head = self.head.next
    
    def delete_at_index(self, index):                       # delete the node at index
        if self.head == None: return
        current_node = self.head
        position = 0

        if position == index:
            self.delete_first_node()

        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present!")

    def update(self, id, new_name, new_address):
        current = self.head
        while current:
            if current.person.id == id:  # Accessing id attribute of the Person object
                current.person.name = new_name  # Update the name
                current.person.address = new_address  # Update the address
                #print("Student with ID", id, "updated successfully")
                return True  # Indicate successful update
            current = current.next
        # If ID is not found
        print("Student with ID:", id, "not found")
        return False

    def printLL(self):                                      # print linked List formatted
        cur_node = self.head

        while(cur_node):
            person = cur_node.person
            print(person.id,
                   person.name, "\n",
                   person.dob, "\n",
                   person.address)
            cur_node = cur_node.next
