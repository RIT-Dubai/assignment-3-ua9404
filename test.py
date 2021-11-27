import home_home

# This test will show if the  garden item is printed according to there code
def test_garden_options():
    assert "p" == '3 pack garden flower'
    assert "l" == 'Hanging light wire'
    assert "b" == 'garden bench'
    assert "n" == 'None and Next'

test_garden_options()


# this test will show if the indoor item is printed according to there code
def test_indoor_options():
    assert "t" == 'Small table lamp'
    assert "f" == 'City picture frame'
    assert "r" == '4x5 entry rug'
    assert "n" == 'None and Next'

test_indoor_options()


# this test will show if the bathroom item is printed according to there code
def test_bathroom_options():
    assert "w" == 'Weighing scale'
    assert "a" == 'Towel'
    assert "y" == 'Brush holder'
    assert "n" == "None and Next"

test_bathroom_options()


# test to see if selected categories are responding
def test_selected_item():
    home_home.selected_items()
    selected_item = input()
    assert selected_item == input()
    assert selected_item == "G.O"
    assert selected_item == "I.O"
    assert selected_item == "B.O"

test_selected_item()


# test to see if prices are totaled
def test_price():
    home_home.selected_items()
    basket = 0
    assert home_home.selected_items().price == home_home.garden_option["p"][1]
    assert home_home.selected_items().price == home_home.indoor_option["t"][1]
    assert home_home.selected_items().price == home_home.bathroom_option["w"][1]
    assert home_home.selected_items().price == basket + home_home.selected_items().price

test_price()
