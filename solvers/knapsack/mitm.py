from itertools import chain, combinations


def meet_in_the_middle(treasure_list, trunk_size):
    def superset(iterable):
        # very handy, gives a set of all possible sets from a set
        xs = list(iterable)
        return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))
    first_half = treasure_list[:len(treasure_list)//2]
    second_half = treasure_list[len(treasure_list)//2:]
    to_take = []
    max_total_value = 0
    first_half_superset = list(superset(first_half))
    second_half_superset = list(superset(second_half))
    for first_treasure_set in first_half_superset:
        for second_treasure_set in second_half_superset:
            total_set = first_treasure_set + second_treasure_set
            if total_set:
                total_size = sum(treasure.size for treasure in total_set)
                if total_size <= trunk_size:
                    total_value = sum(treasure.value for treasure in total_set)
                    if total_value > max_total_value:
                        to_take = total_set
                        max_total_value = total_value
    return to_take


