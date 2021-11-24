class Item:
    __slots__ = ['__name', '__code', '__price']

    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        self.__price = 0

class Home_Avatar:
    __slots__ = ['__garden_options', '__indoor_options', '__bathroom_options', '__base_service']

    def __init__(self, garden_options, indoor_options, bathroom_options):
        self.__garden_options = garden_options
        self.__indoor_options = indoor_options
        self.__bathroom_options = bathroom_options
        self.__base_service = 50

garden_option = {'3 pack garden flower (p)': 5.0, 'Hanging light wire (l)': 10.0, 'garden bench (b)': 35.0, 'None and Next (n)': 0.0}
indoor_option = {'Small table lamp (t)': 5.0, 'City picture frame (f1)': 7.0, '4x5 entry rug (r)': 35.0, 'None and Next (n)': 0.0}
bathroom_option = {'Weighing scale (w)': 2.0, 'Towel (a)': 3.0, 'Brush holder (y)': 6.0, 'None and Next': 0.0}
