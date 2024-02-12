# imagine you are holding an e-commerce platform discuss how you would use lists to manage a user's shopping cart , Explain how could you add items to the cart , remove , calculaare total cost of the the items in the cart and also empty the cart
def create_cart():
    return []

def add_item_to_cart(cart, item_name, item_price, item_quantity):
    cart.append({
        'name': item_name,
        'price': item_price,
        'quantity': item_quantity
    })

def remove_item_from_cart(cart, item_name):
    for item in cart:
        if item['name'] == item_name:
            cart.remove(item)
            break

def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item['price'] * item['quantity']
    return total_cost

def empty_cart(cart):
    cart.clear()

# Example usage:
cart = create_cart()
add_item_to_cart(cart, 'Apple', 1.0, 3)
add_item_to_cart(cart, 'Banana', 0.5, 5)
print(f'Total cost: {calculate_total_cost(cart)}')
remove_item_from_cart(cart, 'Apple')
print(f'Total cost after removing apples: {calculate_total_cost(cart)}')
empty_cart(cart)
print(f'Total cost after emptying cart: {calculate_total_cost(cart)}')