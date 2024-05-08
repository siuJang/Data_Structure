from doublylist import DoublyList as dl

### MENU
def menu():
    print()
    print("##########################")
    print("  1. CREATE HEAD, TAIL NODE ")
    print("  2. APPEND NODE ")
    print("  3. INSERT NODE ")
    print("  4. MODIFY NODE ")
    print("  5. DELETE NODE ")
    print("  6. PRINT NODES ")
    print("  7. QUIT ")
    print("##########################")
    print()

#### MAIN
print("######################################################")
print(" Hey Guys, A Simple linked list has been created....")
print(" Please select one of the menus below to continue.")
print("#####################################################")

dlist = dl()
choice = "999"

while choice != "7":
    menu()
    choice = input("SELECT MENU? ==>  ")

    if choice == "1":
       dlist.create_ht()
    elif choice == "2":
        print()
        data = input("Enter the data you want to add.. ==> ")
        if data == None:
            print("No data has been entered. Please check the data...")
        else:
            result = dlist.node_append(data)
            if result[0] == 100:
                print(result[1])
            else: print(result[1])

    elif choice == "3":
        find = input("Insert data value ==> ")
        data = input("Enter the data you want to add.. ==> ")
        result = dlist.node_insert(find, data)
        if result[0] == 100:
            print(result[1])
        else: print(result[1])

        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        dlist.order_print()
        pass
    elif choice == "7":
        dlist.reverse_print()
        pass
    elif choice =="8":
        break

    else:
        print(" Wrong menu-number...")