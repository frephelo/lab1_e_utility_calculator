
def calculate_consumption(appliances):
    total = 0
    for x in appliances:
        daily = a["wattage"] * a["qty"] * a["hours"]
        monthly = (daily * 30) / 1000               
        total += monthly

    return round(total)