
def register_customer():
    print("Register Customer ---")
    cid = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    address = input("Enter Customer Address: ")

    customer = {
        "id": cid,
        "name": name,
        "address": address
    }

    customers_list.append(customer)
    print("Customer registered successfully!\n")


def list_customers():
    print("Customer List")
    if not customers_list:
        print("No customers registered yet")
        return

    for c in customers_list:
        print(f"ID: {c['id']} | Name: {c['name']} | Address: {c['address']}")