def calculate_bill(kwh):
    if kwh<=50:
        service_charge = 10
    else:
        service_charge=42    
    cost = 0
    if kwh <= 50:
        cost= kwh * 0.2730
        bill_amount=kwh*cost
    elif kwh <= 100:
        cost = (50 * 0.2730) + ((kwh - 50) * 0.7670)
        bill_amount=kwh*cost
    elif kwh <= 200:
        cost = (50 * 0.2730) + (50 * 0.7670) + ((kwh - 100) * 1.650)
        bill_amount=kwh*cost
    elif kwh<=300:
        cost=(50*0.2730) + (50*0.7670)  + (100*1.650) +((kwh-200)*2.0000)
        bill_amount=kwh*cost
    elif kwh<=400:
        cost=(50*0.273)  + (50*0.7670)  + (100*1.650) + (200*2.0000) + ((kwh-300)*2.2000)
        bill_amount=kwh*cost
    elif kwh<=500:
        cost=(50*0.273)  + (50*0.7670)  + (100*1.650) + (200*2.0000) +  (300*2.2000) + ((kwh-400)*2.4000)
        bill_amount=kwh*cost
    else:
        cost = (50 * 0.2730) + (50 * 0.7670) + (100 * 1.650) + (200 * 2.0000)+(300*2.200) +(400*2.4) + ((kwh-500)*24810)
        bill_amount=kwh*cost
    total = cost + service_charge
    return round(total)