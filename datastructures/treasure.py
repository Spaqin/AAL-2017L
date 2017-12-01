class Treasure(object):
    def __str__(self):
        return "value: {} size: {} ratio: {}".format(self.value, self.size, self.ratio)

    def __init__(self, value, size):
        self.value = value
        self.size = size
        self.ratio = value/size