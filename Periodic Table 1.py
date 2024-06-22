class element:
    def __init__(self, sym, name, no, typ, row, col):
        self.symbol = sym
        self.name = name
        self.atomic_number = no
        self.elem_type = typ
        self.row = row
        self.column = col


def viewElement(element, n):
    print("Name: " + element.name)
    if n == 2 or n == 3:
        print("Symbol: " + element.symbol)
    if n == 2 or n == 4:
        print("Atomic Number: " + str(element.atomic_number))
    if n == 2 or n == 5:
        print("Type: " + element.elem_type)
    if n == 2 or n == 6:
        print("Row: " + str(element.row))
    if n == 2 or n == 7:
        print("Column: " + str(element.column))

    print("\n")



if __name__ == "__main__":
    elem_dict = {}

    while 1:
        print("\n Main Menu \n")
        print("1. Add an Element")
        print("2. View an Element")
        print("3. View all Element Names")
        print("4. View all Atomic Numbers")
        print("5. View all Types")
        print("6. View all Row Numbers")
        print("7. View all Column Number")
        print("8. Exit")
        choice = int(input("Enter your Choice: "))

        if choice == 1:
            sym = input("Enter the symbol: ")
            name = input("Enter the element name: ")
            atom = int(input("Enter the atomic number: "))
            typ = input("Enter the element type: ")
            row = int(input("Enter the row number: "))
            col = int(input("Enter the column number: "))

            if sym not in elem_dict.keys():
                e1 = element(sym, name, atom, typ, row, col)
                elem_dict[sym] = e1
                print(sym + " added\n")
            else:
                print("Element already present")

        elif choice == 2:
            sym = input("Enter the symbol: ")
            viewElement(elem_dict[sym], 2)


        elif choice == 3:
            for i in elem_dict.keys():
                viewElement(elem_dict[i], 3)

        elif choice == 4:
            for i in elem_dict.keys():
                viewElement(elem_dict[i], 4)

        elif choice == 5:
            for i in elem_dict.keys():
                viewElement(elem_dict[i], 5)

        elif choice == 6:
            for i in elem_dict.keys():
                viewElement(elem_dict[i], 6)

        elif choice == 7:
            for i in elem_dict.keys():
                viewElement(elem_dict[i], 7)

        elif choice == 8:
            print("Exiting")
            break
        else:
            print("Wrong entry, Please re-enter\n")
