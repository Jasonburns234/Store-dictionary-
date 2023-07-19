# Create store dictionaries
freelancers = {'name': 'Freelancing Shop', 'brian': 70, 'black knight': 20, 'biccus diccus': 100, 'grim reaper': 500, 'minstrel': -15}
antiques = {'name': 'Antique Shop', 'french castle': 400, 'wooden grail': 3, 'scythe': 150, 'catapult': 75, 'german joke': 5}
pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}

# Create an empty shopping cart
cart = {}

# Create a list of store dictionaries
shops = [freelancers, antiques, pet_shop]

# Loop through store dictionaries
for shop in shops:
    shop_name = shop['name']

    # Display available items for sale and prompt user to select an item
    items_for_sale = ', '.join(shop.keys())
    buy_item = input(f'Welcome to {shop_name}! Available items for sale: {items_for_sale}\nWhat do you want to buy? (Enter item name or type "exit" to go to the next store or "done" to finish): ').lower()

    # Check if the user wants to exit or finish shopping
    if buy_item == 'exit':
        continue
    elif buy_item == 'done':
        break

    # Check if the selected item is available in the current store
    if buy_item in shop:
        # Update the cart with the selected item and remove it from the store's inventory
        cart[buy_item] = shop.pop(buy_item)
        print(f'{buy_item} added to the cart.')
    else:
        print('That item is not available for sale.')

# Convert the cart keys into a comma-separated string for display purposes
buy_items = ', '.join(cart.keys())

# Print the purchased items
print(f'You purchased: {buy_items}. Today it is all free. Have a nice day of mayhem!')
