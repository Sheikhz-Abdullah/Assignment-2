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