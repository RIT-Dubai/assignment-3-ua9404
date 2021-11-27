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
