def add_items():
    items=[]
    prices=[]
    quantities=[]
    while True:
        name=input("enter the item's name:")
        price=float(input("enter the item's price:"))
        quantity=int(input("enter the item's quantity: "))
        items.append(name)
        prices.append(price)
        quantities.append(quantity)
        more=input("add one more item(yes/no):")
        if more != "yes":
            break
    return items,prices,quantities
def calculate_bill(prices,quantities):
    total=sum(price*quantity for price,quantity in zip(prices,quantities))
    if total>=500:
        discount=total*0.1
    elif total>=200:
        discount=total*0.05
    else:
        discount=0
    final_amount=total-discount
    return total,discount,final_amount
def show_amount(items,prices,quantities,total,discount,final_amount):
    print("/n--------BILL----------")
    for i in range(len(items)):
        item_total=prices[i]*quantities[i]
        print(f"{items[i]}x{quantities[i]} - {item_total:.2f}")
    print(f"total:rs.{total}")
    print(f"discount:rs.{discount}")
    print(f"final_amount:rs.{final_amount}")
items,prices,quantities=add_items()
total,discount,final_amount=calculate_bill(prices,quantities)
show_amount(items,prices,quantities,total,discount,final_amount)
    




