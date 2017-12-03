def greedy(treasure_list, trunk_size):
    to_take = []
    treasure_list.sort(key=lambda x: x.value/x.size, reverse=True)
    for treasure in treasure_list:
        if treasure.size < trunk_size:
            to_take.append(treasure)
            trunk_size -= treasure.size
    return to_take
