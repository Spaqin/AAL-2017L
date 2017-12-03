class Treasure(object):
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "value: {} size: {}, city: {}".format(self.value, self.size, self.city)

    def __init__(self, value=0, size=0, city=None):
        self.value = value
        self.size = size
        self.city = city