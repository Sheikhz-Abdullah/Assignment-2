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