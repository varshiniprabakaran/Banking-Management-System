class ItemNotFoundError(Exception):
    pass
class OutOfStockError(Exception):
    pass
class PaymentFailedError(Exception):
    pass
menu={
    "parotta":{"price":15,"stock":40},
    "chicken rice":{"price":120,"stock":50},
    "briyani":{"price":200,"stock":25},
    "full meals":{"price":300,"stock":20}
}
def check_item(item,quantity):
    if item not in menu:
        raise ItemNotFoundError(f"{item} is not available!")
    if  menu[item]["stock"]<quantity:
        raise OutOfStockError(f"{menu[item]['stock']} left for {item}!")
    return True
def process_payment(amount):
    print("Your total bill is Rs.",amount)
    user=input("Enter 'yes' to complete payment or 'no' to fail:")
    if user.lower()!="yes":
        raise PaymentFailedError("Payment failed!")
    else:
        print("Payment successful!")
def place_order():
    item = input("Enter the item you want to order: ").lower()
    quantity = int(input("Enter quantity: "))
    try:
        check_item(item,quantity)
        amount=menu[item]["price"]*quantity
        process_payment(amount)
        menu[item]["stock"]-=quantity
        print("Order placed successfully!")
    except ItemNotFoundError as order:
        print(order)
    except OutOfStockError as order:
        print(order)
    except PaymentFailedError as order:
        print(order)
    finally:
        print("Thank you for using our food delivery system\n")
while True:
    place_order()
    again = input("Do you want to order again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break