from faker import Faker
from linked_list import LinkedList, PersonLL
from avl import AVLTree, Person

import timeit               # for runtime calc

"""
CSCE 3110 Project implementing a binary search tree and a linked list
to store student information in a quasi-database format
"""

def main ():
    # create faker, linked list, and binary search tree
    fake = Faker()
    linked_list = LinkedList()
    avl = AVLTree()

    # runtime formatting
    rt = ["Insertion", "Deletion", "Search by ID (success)", "Search by ID (fail)", "Search by Name (success)", "Search by Name (fail)", "Update"]     # runtime label array, preset index for each function
    rt_bst = [-1, -1, -1, -1, -1, -1, -1]     # bst runtimes
    rt_ll = [-1, -1, -1, -1, -1, -1, -1]      # linked list runtimes

    print("Populating...") # so that user can know it's thinkin

    # generate linked list with student Id, name, dob, address (must address be split into stree, city,state,zip>?)
    for i in range(1,100000):
        id = i + 5          # chosen for test so as not be confused with index
        fName = fake.name()
        fDob = fake.date_between(1990,2010)
        fAddress = fake.address()

        person = PersonLL(id, fName, fDob, fAddress)

        linked_list.insertAtBegin(person) #   StudentId, Name, DOB, Address
        
        p = Person(id, fName, fDob, fAddress)
        avl.insert_person(p)
    

    while True:
        print("\nOptions:")
        print("1. Add a student to the database")
        print("2. Delete a student from the database")
        print("3. Search for a student with ID")
        print("4. Search for a student with name")
        print("5. Update student records")
        print("6. Exit")

        choice = input("Choose an option: ")
        print("++++++++++++++++++++++++++++++++++++")
        if choice == "1":       # ADD STUDENT
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (YYYY-MM-DD): ")
            address = input("Enter the student's address: ")

            # check if ID exists
            if linked_list.get_id_index(id) or avl.find_person(id):
                print("Error student already exits in system. Please try again.")
                continue #starts the operation over if ID is in list
            else:
                print("Adding ID to the system...")

           
            start = timeit.default_timer()          # start clock
            person = Person(id, name, dob, address) # create 'student'
            avl.insert_person(person)                           # insert 'student' into tree         
            end = timeit.default_timer()            # end clock 
            rt_bst[0] = end-start       ## place into bst insertion runtime
            
            start = timeit.default_timer()          # start clock
            person_ll = PersonLL(id, name, dob, address)   #insert student into ll
            linked_list.insertAtBegin(person_ll)
            end = timeit.default_timer()            # end clock 
            rt_ll[0] = end-start        ## place into bst insertion runtime

            print("Student added successfully.")
            print('Runtime (LL, BST): %g, %g' % (rt_ll[0], rt_bst[0]))
        
        elif choice == "2":     # DELETE STUDENT
            # display student records before deleting

            id = int(input("Enter the ID of the student to delete: "))
            person = avl.find_person(id)
            print("Student found: ")
            print(person)

            choice = input("Is this the person you'd like to delete? (Y/N): ")

            if choice == 'Y' or choice == 'y':
                start = timeit.default_timer()          # start clock
                avl.delete_person(id)                       # delete from tree
                end = timeit.default_timer()            # end clock
                rt_bst[1] = end - start     ## store in array of tree runtimes

                start = timeit.default_timer()          # start clock
                linked_list.delete(id)               # delete from linked list
                end = timeit.default_timer()            # end clock
                rt_ll[1] = end - start      ## store in array of ll runtimes

                print('Runtime (LL, BST): %g, %g' % (rt_ll[1], rt_bst[1]))
            else:
                print("Aborting deletion.")

        elif choice == "3":     # SEARCH BY ID
            student_id = int(input("Enter student ID to search: "))
            result = None
            index = None

            start = timeit.default_timer()          # start clock
            result = avl.find_person(student_id)                # search tree
            end = timeit.default_timer()            # end clock
            sid_bst = end-start      ## store in array of tree runtimes

            start = timeit.default_timer()          # start clock
            index = linked_list.get_id_index(student_id)
            end = timeit.default_timer()            # end clock
            sid_ll = end-start      ## store in array of ll runtimes

            if result:
                print(f"TREE: Student {student_id} found.")
                print (f"-------------------------------------")
                print(result)
                print("+++++++++++++++++++++++++++++++++++++++")
                rt_bst[2] = sid_bst
            else: 
                print(f"TREE: Student {student_id} NOT found")
                rt_bst[3] = sid_bst
           
            if index:
                
                print(f"LL: Student {student_id} found.")
                print ("--------------------------------------")
                print(index.person)
                print("+++++++++++++++++++++++++++++++++++++++")
                rt_ll[2] = sid_ll
                print('Runtime (LL, BST): %g, %g' % (rt_ll[2], rt_bst[2]))
            else: 
                print(f"LL: Student {student_id} NOT found")
                rt_ll[3] = sid_ll
                print('Runtime (LL, BST): %g, %g' % (rt_ll[3], rt_bst[3]))

        elif choice == "4":     # SEARCH BY NAME
            student_name = input("Enter student name to search: ")

            start = timeit.default_timer()
            result = avl.find_by_name(student_name)
            end = timeit.default_timer()

            sn_bst = end-start

            start = timeit.default_timer()
            index = linked_list.get_name_index(student_name)        #call get_name_index from ll
            end = timeit.default_timer()
            sn_ll = end-start

            if result:
                print("+++++++++++++++++++++++++++++++++++++++")
                print(f"TREE: {student_name} found.")
                print (f"-------------------------------------")
                print(result[0])
                rt_bst[4] = sn_bst
                
            else: 
                print(f"TREE: {student_name} NOT found")
                rt_bst[5] = sn_bst


            if index:     
                print("+++++++++++++++++++++++++++++++++++++++")                               #check if index is found
                print(f"LL: {student_name} found.")
                print (f"-------------------------------------")
                print(index.person)
                rt_ll[4] = sn_ll
                print("+++++++++++++++++++++++++++++++++++++++")
                print('Runtime (LL, BST): %g, %g' % (rt_ll[4], rt_bst[4]))
            else:
                print(f"LL: {student_name}, not found.")
                rt_ll[5] = sn_ll
                print('Runtime (LL, BST): %g, %g' % (rt_ll[5], rt_bst[5]))
           
        elif choice == "5":  # UPDATE
            id = int(input("Enter the ID of the student to update: "))
            current = linked_list.head
            while current:
                if current.person.id == id:
                    print("\nCurrent student information:")
                    print("ID:", current.person.id)
                    print("Name:", current.person.name)
                    print("DOB:", current.person.dob)
                    print("Address:", current.person.address)

                    new_name = input("\nEnter the updated name of the student(Hit Enter to keep the name the same): ")
                    if new_name.strip() == "":
                        new_name = current.person.name
                        print("No name changes were made.\n")

                    new_address = input("Enter the updated address of the student(Hit Enter to keep the address the same): ")
                    if new_address.strip() == "":
                        new_address = current.person.address
                        print("No address changes were made.\n")

                    # Update student record in tree
                    start = timeit.default_timer()
                    if avl.update_person(id, new_name, new_address):
                        print(f"Student with ID {id} updated successfully in tree.")
                    else:
                        print(f"No person found with ID {id} in tree.")
                    end = timeit.default_timer()
                    rt_bst[6] = end - start

                    # Update student record in linked list
                    start = timeit.default_timer()
                    linked_list.update(id, new_name, new_address)
                    end = timeit.default_timer()
                    rt_ll[6] = end - start

                    print(f"Student with ID {id} updated successfully in list.")
                    print('Runtime (LL, BST): %g, %g' % (rt_ll[6], rt_bst[6]))
                    break
                current = current.next
            else:
                print(f"No person found with ID {id}.")

        elif choice == "6":
            print("Ending...\n")
            break

        else:   # error checking
            print("Invalid choice. Please enter a number between 1 and 6")
    

    # DISPLAY RUNTIME CALCULATIONS
    print("Runtime Calculations (in seconds):")
    print('%-30s %-15s %-15s' % ("Function", "Linked List", "Binary Search Tree"))
    print("-----------------------------------------------------------------")
    for a, b, c in zip(rt, rt_ll, rt_bst):
        print('%-30s %-15g %-15g' % (a, b, c))

main()
