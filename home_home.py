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
        self.__base_service = 0


