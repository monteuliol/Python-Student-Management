# CSCE 3110 Group Project (Group 5)
### Members and Credits
- Montral Coleman: Setup menu of options, display student information before deletion, and duplicate id prevention for insertion.
- Maria Gonzalez: "Search by ID", "Search by Name", Updating Linked List  implementation and storing student records in a text file.
- Uziel Muteba: Midpoint presentation
- Kolade Olojo: "Update Student Records"
- Nidhi Ravala: Runtime calculations, display, and comparison.
- Monique Simberg: Implementation of linked list, AVL tree, "Person" class, "Search by Name" in tree, and python faker library.

## Features
This project creates an AVL tree and a linked list to hold a ficticious set of student information including Names, Student ID, DOB, and  Addresses. From here, the user may choose to:

    1. add a student to the existing database.    
    2. delete a student from the database once the student ID is given
    3. search for a student with an ID
    4. Search for a student with a name in case the student ID is not available
    5. update student records when the student ID is given, which allows the user to see current information and modify any information except student ID and birthdate.

## Files
main.py: the main driver file for the program
- User input functionality ("Menu of Options")
- Runtime calculations and output

avl.py: includes the methods for constructing and modifying a Binary Search Tree
- "Person" class: contains all the variables needed for each student in the database
- "TreeNode" class: nodes with left and right characteristics used for AVL Tree
- getBalance: checks for unbalanced tree upon insertion/deletion
- getHeight: checks height of the tree
- rightRotate: rotates right if unbalanced to the left
- leftRotate: rotates left if unbalanced to the right
- print_tree: prints entire tree (used during testing)
- inorder_traversal: traversal implementation used for print function
- min_value_node: finds the minimum node
- Insertion functions: used to insert new "Person" nodes to the tree
    - insert_person: passes root of the tree as a parameter for neater function call
    - insert: called by the insert_person function, has the actual insertion implementation
- Deletion functions: used to delete a "Person" node from the tree
    - delete_person: passes root of the tree as a parameter to make a neater function call
    - delete: called by delete_person, has actual deletion implementation
- Update functions: used to update "Person" node's name and address
    - update_person: passes root of the tree as a parameter to make a neater function call
    - update: called by update_person, has actual update implementation

linked_list.py: includes the methods for constructing and modifying a Linked List
- "Person" class: contains all the variables needed for each student in the database
- "Node" class: nodes with next node characteristic used for Linked List
- "LinkedList" class: defines the linked list and all of it's operations
- Insertion functions: used to insert new "Person" nodes to the LL
    - insert: insert node in a specific location in the LL
    - insertAtBegin: inserts at the start of the LL
- Search functions: used to search for a specific ID or Name in the LL
    - get_id_index: used to search for a specific ID in the LL and print the students info with that ID
    - get_name_index: used to search for a specific name in the LL and print the students info with that name
    - get_data: used to get the data for ID at a specific index
- Deletion functions:  used to delete a "Person" node from the LL
    - delete: used to delete a student in the LL if the ID matches
    - delete_first_node: used to delete the first item in the LL
    - delete_at_index: used to delete the student at the current index
- Update: used to update a student's Name and Address in the LL
- printLL: used to print the LL


## Compilation and Execution
First, ensure that you have python installed on your machine. 

Before running this program, you will need to **download the python faker library**. This command can vary based on your machine and the version of python you have downloaded. For example,
```
python -m pip install faker
```
or 
```
py -m pip install faker
```
or 
```
pip install faker
```

**To run** the driver file, use the following command:
```
python main.py
```
From here, the program should output a "Populating..." message to show that it is generating a database of 100,000 students. This may take a while, so please be patient. Next, you will be presented with a menu of options to modify the database as you please. After each function, the runtime for it to execute in the linked list and AVL tree will be displayed. Finally, when the "exit" option is chosen (6), there will be a table of the most recent runtime for each function displayed. If a function has not been used, the default runtime displayed is -1 to show an empty value.
