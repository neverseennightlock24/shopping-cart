print("Welcome, user. What can we do for you today?")

items = {'apple': 10,
         'banana': 15,
         'chocolate': 5}

class ShoppingCart:
    
    def __init__(self):
        self.items = []  # the actual items in our cart

    def add(self, itemName):
        if itemName in items:
            self.items.append(itemName)
            print(f"Added {itemName} to your cart.")
        else:
            print(f"Sorry, {itemName} is not available in the store.")

    def remove(self, itemName):
        if itemName in self.items:
            self.items.remove(itemName)
            print(f"Removed {itemName} from your cart.")
        else:
            print(f"Sorry, {itemName} is not in your cart.")

    def view(self):
        if self.items:
            print("Your cart contains:", self.items)
        else:
            print("Your cart is empty.")

    def cost(self):
        x = 0
        for i in self.items:
            x += items[i]

        if x > 5:
            print(f"The cost of your purchases is currently ${x}. Feel free to continue exploring our online store!")
        else:
            print(f"The cost of your purchase is currently ${x}. Feel free to continue exploring our store!")

ab = ShoppingCart()

while True:
    userInput = input("\nPlease choose from the following options:\n"
                      "1. Add an item to your Shopping Cart\n"
                      "2. Remove an item from your Shopping Cart\n"
                      "3. Check cost of cart\n"
                      "4. View items in your cart\n"
                      "5. Exit virtual mall\n")

    if userInput == "1":
        # Add an item
        print("Your choice is 1")
        print("Available items:", items)
        itemName = input("Input the name of the item you want to add: ")
        ab.add(itemName)
    
    elif userInput == "2":
        # Remove an existing item
        print("Your choice is 2")
        itemName = input("Input the name of the item you want to remove: ")
        ab.remove(itemName)

    elif userInput == "3":
        # Find the cart's cost
        print("Your choice is 3")
        ab.cost()

    elif userInput == "4":
        # View items in the cart
        print("Your choice is 4")
        ab.view()

    elif userInput == "5":
        # Exit program
        print("Your choice is 5. Exiting the virtual mall.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
