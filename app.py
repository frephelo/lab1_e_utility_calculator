print("E-UTILITY BILL CALCULATOR")
customers = []
appliances = []
#customer function
def register_customer():
    print("\n--- Register Customer ---")
    cid = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")

    customers.append({"id": cid, "name": name})
    print("Customer registered successfully.\n")

def list_customers():
    print("\n--- Customer List ---")
    if not customers:
        print("No customers found.\n")
        return
    for c in customers:
        print(f"ID: {c['id']}   Name: {c['name']}")
    print()



# APPLIANCE FUNCTION
def register_appliance():
    print("\n--- Register Appliance ---")
    name = input("Appliance Name: ")
    watt = float(input("Power Rating (Watts): "))
    hours = float(input("Hours used per day: "))
    days = int(input("Days used per month: "))

    appliances.append({
        "name": name,
        "watt": watt,
        "hours": hours,
        "days": days
    })

    print("Appliance registered successfully.\n")

def list_appliances():
    print("\n--- Appliance List ---")
    if not appliances:
        print("No appliances registered.\n")
        return

    for a in appliances:
        print(f"{a['name']} - {a['watt']}W, {a['hours']} hrs/day, {a['days']} days/month")
    print()


# BILL CALCULATION (Your Tier + Extra Charge)
def calculate_bill(total_consumption):
    bill_amount = 0.0

    # Tier-based billing
    if total_consumption <= 50:
        bill_amount = total_consumption * 0.273
    elif total_consumption <= 100:
        bill_amount = total_consumption * 0.767
    elif total_consumption <= 200:
        bill_amount = total_consumption * 1.625
    elif total_consumption <= 300:
        bill_amount = total_consumption * 2
    elif total_consumption <= 400:
        bill_amount = total_consumption * 2.2
    elif total_consumption <= 500:
        bill_amount = total_consumption * 2.405
    else:
        bill_amount = total_consumption * 2.481

    # EXTRA CHARGES BASED ON CONSUMPTION
    if total_consumption <= 50:
        bill_amount += 10 
    else:
        bill_amount += 42    

    return bill_amount


# CALCULATE CONSUMPTION
def calculate_consumption():
    print("\n--- Monthly Consumption ---")
    
    if not appliances:
        print("No appliance data available.\n")
        return None

    total_kwh = 0

    for a in appliances:
        kwh = (a["watt"] / 1000) * a["hours"] * a["days"]
        total_kwh += kwh

    print(f"Total Monthly Consumption: {total_kwh:.2f} kWh")
    return total_kwh


# MAIN BILL MENU
def calculate_bill_menu():
    kwh = calculate_consumption()
    if kwh is None:
        return

    bill = calculate_bill(kwh)

    print(f"Total Monthly Bill: {bill:.2f} ETB\n")

# MAIN MENU

def main():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Customer")
        print("2. Appliance")
        print("3. Consumption & Bill")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            print("\n1. Register Customer")
            print("2. List Customers")
            sub = input("Choose: ")
            if sub == "1":
                register_customer()
            else:
                list_customers()
        elif choice == "2":
            print("\n1. Register Appliance")
            print("2. List Appliances")
            sub = input("Choose: ")
            if sub == "1":
                register_appliance()
            else:
                list_appliances()

        elif choice == "3":
            calculate_bill_menu()

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option. Try again.\n")

main()