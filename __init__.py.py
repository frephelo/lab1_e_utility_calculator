def main():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Customer")
        print("2. Appliance")
        print("3. Consumption & Bill")
        print("4. Exit")

        choice = int(input("Select option: "))

        if choice == 1:
            print("1. Register Customer")
            print("2. List Customers")
            sub = int(input("Choose: "))
            if sub == 1:
                register_customer()
            else:
                list_customers()
        elif choice == 2:
            print("\n1. Register Appliance")
            print("2. List Appliances")
            sub = int(input("Choose: "))
            if sub == 1:
                register_appliance()
            else:
                list_appliances()

        elif choice == 3:
            calculate_bill_menu()

        elif choice == 4:
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option. Try again.\n")


# Run program
main()