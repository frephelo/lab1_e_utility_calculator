def register_appliance(appliances):
    print(" Register Appliance ")
    name = input("Enter Appliance name: ")
    wattage = float(input("Enter Wattage : "))
    qty = int(input("Quantity: "))
    hours_per_day = float(input("Usage hours per day: "))

    app = {
        "name": name,
        "wattage": wattage,
        "qty": qty,
        "hours": hours_per_day
    }
    appliances.append(app)

    print("Appliance registered successfully.\n")


def list_appliances(appliances):
    print("" Appliance List")
    for a in appliances:
        print(f"{a['qty']}x {a['name']} | {a['wattage']}W | {a['hours']} hrs/day")