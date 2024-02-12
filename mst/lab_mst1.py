# image you are building an e-commerce platform discuss how you would use lists to manage a users shopping cart. Explain how you could add the items to the cart, remove items, and calculate the total cost of the items.

class Item:
    title = ""
    quantity = 0
    price = 0

    def __init__(self, title, quantity, price):
        self.title = title
        self.quantity = quantity
        self.price = price


def add_item(item,items):
    # checking if item is already in cart
    for i in range(len(items)):
        if items[i].title == item.title:
            items[i].quantity += item.quantity
            return
    # if item is not in cart
    items.append(item)

# removes item from cart
def remove_item(itemName,items):
    # checking if item exists in cart
    for item in items:
        if item.title == itemName:
            items.remove(item)

# calculate total price of cart
def calculate_price(items):
    tot = 0
    for item in items:
        tot += item.price * item.quantity
    
    return tot

# create empty cart
def create_cart():
    return []

# function to print cart
def print_cart(items):
    print("---"*15)
    print("Items\t\tQty\tPrice\tTotalPrice")
    print("---"*15)
    for item in items:
        print(f"{item.title}\t\t{item.quantity}\t{item.price}\t{item.price * item.quantity}")
    print("---"*15)


if __name__ == "__main__":
    # creating empty cart
    cart = create_cart()

    # adding elements on cart
    add_item(Item("pen",2,23),cart)
    add_item(Item("pencil",5,20),cart)
    add_item(Item("pencil",10,20),cart)
    add_item(Item("copy",1,200),cart)

    # printing cart
    print("\nThe cart before removing elements")
    print_cart(cart)

    # removing item
    remove_item('pen',cart)

    # printing cart
    print("\nThe cart after removing elements")
    print_cart(cart)

    # printing final price
    print(f"The final price of cart is: {calculate_price(cart)}")