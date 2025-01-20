# Create a VendingMachine class to organise the method of collecting all of the data and functionality linked to a vending machine.
class VendingMachine:

    # Initialising the vending machine using the constructor method.
    def __init__(self):

        # Create a dictionary to keep track of the types of goods that are offered in the vending machine.
        self.items = {
            
            # Each category contains items with their price and stock quantity.
            "Hot Beverages": {"Coffee": [5.00, 8], "Tea": [2.00, 10], "Hot Chocolate": [8.50, 5]},
            "Snacks": {"Chips": [1.50, 5], "Chocolate": [2.00, 8], "Jelly": [6.25, 15]},
            "Cold Drinks": {"Water": [1.00, 15], "Soda": [2.75, 7], "Red Bull": [13.50, 20]}
        }

        # Variable that monitors the user's current machine balance.
        self.balance = 0.0

    # Describes the display_menu function, which shows the vending machine's inventory of available items arranged by type.
    def display_menu(self):
        print("\nWelcome to the Vending Machine! Here is the menu:")

        # Repeat for every category and its items.
        for category, products in self.items.items():
            print(f"\n{category}:")

            # Review each product's details, including price and stock.
            for product, (price, stock) in products.items():

                # Show the current stock level; if it is zero, display 'Out of Stock'. If not, show the cost and amount available.
                stock_status = "Out of Stock" if stock == 0 else f"${price:.2f} ({stock} left)"
                print(f"  {product}: {stock_status}")
                
    def select_item(self):

        # A way to let the consumer choose what they want to buy.
        while True:

            # Request that the user input the desired item's name.
            choice = input("\nEnter the name of the item you want to buy: ").strip().capitalize()

            # To determine the user's preference, loop through the categories and their offerings.
            for category, products in self.items.items():
                if choice in products:

                    # Get the chosen item's price and stock level.
                    price, stock = products[choice]
                    if stock > 0:

                        # Return the item's details if it is in stock.
                        return choice, price, category
                    else:

                        # If the item is out of stock, let the user know.
                        print(f"Sorry, {choice} is out of stock.")
                        return None, None, None
                    
            # Ask the user to try again if the input is incorrect.
            print("Invalid selection. Please choose an item from the menu.")

    def insert_money(self, price):

        # How to manage the user's money entry for the chosen item and show the user the item's price.
        print(f"The price of your item is ${price:.2f}.")

        # Continue until the user's balance is enough to pay for the item.
        while self.balance < price:
            try:

                # Request money from the user and convert it to a float.
                money = float(input(f"Insert money (Current balance: ${self.balance:.2f}): "))
                if money <= 0:

                    # Make sure the user enters an amount that is positive.
                    print("Please insert a positive amount.")
                else:

                    # To the user's balance, add the money that was inserted.
                    self.balance += money
            except ValueError:

                # Adaptably handle non-numeric input.
                print("Invalid input. Please enter a numeric value.")
    
    # Technique for giving the user the chosen item.
    def dispense_item(self, item, price):

        # Take the cost of the item out of the user's balance.
        self.balance -= price

        # Find and update the stock of the chosen item by iterating through the categories.
        for category, products in self.items.items():
            if item in products:

                # Cut the dispensed item's stock quantity by one.
                products[item][1] -= 1
        
        # As the item is being distributed, let the user know.
        print(f"Dispensing {item}. Enjoy!")

        # To give the user their remaining balance back, utilise the return_change method.
        self.return_change()
    
    def return_change(self):

        # How to give the user their money back if there is any left over.
        if self.balance > 0:

            # Notify the user of the amount being returned.
            print(f"Returning change: ${self.balance:.2f}")

            # Put the balance back to zero.
            self.balance = 0.0

    def suggest_item(self, category):

        # How to recommend a different product from a different category.
        print("\nSuggestion:")

        # Go over each category and its products one by one.
        for other_category, products in self.items.items():
            if other_category != category:

                # Ignore the item's current category that was purchased.
                for product, (price, stock) in products.items():
                    if stock > 0:

                        # Provide the first item from a different category that is available.
                        print(f"  {product} (${price:.2f})")
                        return
                    
    def start(self):

        # How to begin the vending machine operation.
        while True:

            # Display the menu to the user.
            self.display_menu()

            # Let the user choose an item.
            item, price, category = self.select_item()
            if item:

                # If a valid item is selected, handle the money insertion process.
                self.insert_money(price)

                # Give the chosen thing out.
                self.dispense_item(item, price)

                # Provide a substitute product from a different category.
                self.suggest_item(category)