from datastructures.treasure import Treasure


class TreasureGenerator(object):

    VALUE_MIN = 15000
    VALUE_MAX = 500000

    SIZE_MIN = 20
    SIZE_MAX = 600

    DEFAULT_TRUNK_SIZE = 800
    TRUNK_SIZE_MULTIPLIER = 5

    def __init__(self, treasure_count, random):
        self.treasure_count = treasure_count
        self.random = random
        self.suggested_trunk_size = self.DEFAULT_TRUNK_SIZE

    def generate_treasure_list(self):
        treasure_list = []
        total_size = 0
        for _ in range(self.treasure_count):
            value = self.random.randint(self.VALUE_MIN, self.VALUE_MAX)
            size = self.random.randint(self.SIZE_MIN, self.SIZE_MAX)
            total_size += size
            treasure_list.append(Treasure(value=value, size=size))
        self.suggested_trunk_size = total_size*self.TRUNK_SIZE_MULTIPLIER/self.treasure_count
        return treasure_list
