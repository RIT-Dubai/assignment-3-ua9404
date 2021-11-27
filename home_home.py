class Item:
# encapsulates item state
    __slots__ = ['__name', '__code', '__price']

    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        self.__price = 0

class Home_categories:
# this class is used as the basket for shopping
    __slots__ = ['__garden_options', '__indoor_options', '__bathroom_options', '__base_service']

    def __init__(self, garden_options, indoor_options, bathroom_options):
        self.__garden_options = garden_options
        self.__indoor_options = indoor_options
        self.__bathroom_options = bathroom_options
        self.__base_service = 50

garden_option = {"p": ('3 pack garden flower', 5.0), "l": ('Hanging light wire', 10.0), "b": ('garden bench', 35.0), "n": ('None and Next', 0.0)}
indoor_option = {"t": ('Small table lamp', 5.0), "f": ('City picture frame', 7.0), "r": ('4x5 entry rug', 35.0), "n": ('None and Next (n)', 0.0)}
bathroom_option = {"w": ('Weighing scale', 2.0), "a": ('Towel', 3.0), "y": ('Brush holder', 6.0), "n": ('None and Next (n)', 0.0)}

# The below function prints a welcome address to the users
def print_welcome():
    print("Welcome to Home Ideas Center, where all orders include a new home feeling!")
    print("For your new Home space ... ")

print_welcome()


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
    print(" use 'G.O' for garden_options ", " use 'I.O for indoor_options ", " use 'B.O for bathroom_options")

select_options()


# this function will allow selected items to be added to a basket and then have their price calculated
def selected_items():
    basket = 0
    selected_item = input()
    while selected_item is not "n":
        if selected_item == "G.O":
         print_garden_options()
        elif selected_item == "p":
            price = garden_option["p"][1]
            print(" you added the 3 pack garden flower to the basket for $5.0", basket)
            basket = basket + price
        elif selected_item == "l":
            price = garden_option["l"][1]
            print("you added Hanging light wire to the basket for $10.0", basket)
            basket = basket + price
        elif selected_item == "b":
            price = garden_option["b"][1]
            print("you added garden bench to the basket for $35.0", basket)
            basket = basket + price
        print(basket + 50)
        break

    while selected_item is not "n":
        if selected_item == "I.O":
            print_indoor_options()
        elif selected_item == "t":
            price = indoor_option["t"][1]
            print("you added Small table lamp to the basket for $5.0", basket)
            basket = basket + price
        elif selected_item == "f":
            price = indoor_option["f"][1]
            print("you added City picture frame to the basket for $7.0", basket)
            basket = basket + price
        elif selected_item == "r":
            price = indoor_option["r"][1]
            print("you added 4x5 entry rug to the basket for $35.0", basket)
            basket = basket + price
        print(basket + 50)
        break

    while selected_item is not "n":
        if selected_item == "B.O":
           print_bathroom_options()
        elif selected_item == "w":
            price = bathroom_option["w"][1]
            print("you added Weighing Scale to the basket for $2.0", basket)
            basket = basket + price
        elif selected_item == "a":
            price = bathroom_option["a"][1]
            print("you added Towel to the basket for $3.0", basket)
            basket = basket + price
        print(basket + 50)
        break

selected_items()
