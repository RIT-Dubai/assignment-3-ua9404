class Item:
# encapsulates item state
    __slots__ = ['__name', '__code', '__price']

    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        self.__price = 0

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code

    def get_price(self):
        return self.__price

class Home_categories:
# this class is used as the basket for shopping also contains the dictionaries for each category
    __slots__ = ['__garden_options', '__indoor_options', '__bathroom_options', '__base_service']

    def __init__(self, garden_options, indoor_options, bathroom_options):
        self.__garden_options = garden_options
        self.__indoor_options = indoor_options
        self.__bathroom_options = bathroom_options
        self.__base_service = 50

    def get_garden_options(self):
        return self.garden_option

    def get_indoor_options(self):
        return self.indoor_option

    def get_bathroom_options(self):
        return self.bathroom_option

    garden_option = {"p": 5.0, "l": 10.0, "b": 35.0, "n": 0.0}
    indoor_option = {"t": 5.0, "f": 7.0, "r": 35.0, "n": 0.0}
    bathroom_option = {"w": 2.0, "a": 3.0, "y": 6.0, "n": 0.0}


# The below function prints a welcome address to the users
def print_welcome():
    print("Welcome to Home Ideas Center, where all orders include a new home feeling!")
    print("For your new Home space ... ")


# The below function will print out the available options for garden decorations
def print_garden_options():
    print("Garden Options: ")
    print(" 3 pack garden flower (p): $5.0 ")
    print(" Hanging light wire (l): $10.0 ")
    print(" garden bench (b): $35.0 ")
    print(" None and Next (n): $0.0 ")


# The below function will print out the available options for indoor decorations
def print_indoor_options():
    print("Indoor Options: ")
    print(" Small table lamp (t): $5.0 ")
    print(" City picture frame (f): $7.0 ")
    print(" 4x5 entry rug (r): $35.0 ")
    print(" None and Next (n): $0.0 ")


# The below function will print out the available options for bathroom decorations
def print_bathroom_options():
    print("Bathroom Options: ")
    print(" Weighing Scale (w): $2.0 ")
    print(" Towel (a): $3.0 ")
    print(" Brush Holder (y): $6.0 ")
    print(" None and Next (n): $0.0 ")

# This function will allow the user to input a command to select a home category

def select_options():
    print(" Use command to select category to shop: ")
    print(" use 'G.O' for garden_options ", " use 'I.O' for indoor_options ", " use 'B.O' for bathroom_options")


# this function will allow selected items to be added to a basket and then have their price calculated
def selected_items():
    Cart = []
    total_price = 0
    selected_item = input()
    print(" Use command to select category to shop: ")
    print(" use 'G.O' for garden_options ", " use 'I.O for indoor_options ", " use 'B.O for bathroom_options")
    print("Select category: ")
    while selected_item != "n":
        if selected_item == "G.O":
         print_garden_options()
        if "p" in selected_item:
            price = Home_categories.garden_option["p"]
            print(" you added the 3 pack garden flower to the Cart for $5.0", total_price)
            total_price = total_price + price
            Cart.append("p")
        elif "l" in selected_item:
            price = Home_categories.garden_option["l"]
            print("you added Hanging light wire to the Cart for $10.0", total_price)
            total_price = total_price + price
            Cart.append("l")
        elif "b" in selected_item:
            price = Home_categories.garden_option["b"]
            print("you added garden bench to the Cart for $35.0", total_price)
            total_price = total_price + price
            Cart.append("b")
        print(total_price + 50)
        break


    while selected_item != "n":
        if selected_item == "I.O":
            print_indoor_options()
        if "t" in selected_item:
            price = Home_categories.indoor_option["t"]
            print("you added Small table lamp to the Cart for $5.0", total_price)
            total_price = total_price + price
            Cart.append("t")
        elif "f" in selected_item:
            price = Home_categories.indoor_option["f"]
            print("you added City picture frame to the Cart for $7.0", total_price)
            total_price = total_price + price
            Cart.append("f")
        elif "r" in selected_item:
            price = Home_categories.indoor_option["r"]
            print("you added 4x5 entry rug to the Cart for $35.0", total_price)
            total_price = total_price + price
            Cart.append("r")
        print(total_price + 50)
        break


    while selected_item != "n":
        if selected_item == "B.O":
           print_bathroom_options()
        if "w" in selected_item:
            price = Home_categories.bathroom_option["w"]
            print("you added Weighing Scale to the Cart for $2.0", total_price)
            total_price = total_price + price
            Cart.append("w")
        elif "a" in selected_item:
            price = Home_categories.bathroom_option["a"]
            print("you added Towel to the Cart for $3.0", total_price)
            total_price = total_price + price
            Cart.append("a")
        elif "y" in selected_item:
            price = Home_categories.bathroom_option["y"]
            print("you added Brush Holder to the Cart for $6.0", total_price)
            total_price = total_price + price
            Cart.append("y")
        print(total_price + 50)
        break



def main():
    print_welcome()
    select_options()
    selected_items()

main()
