def intersection_func(set_a: set, set_b: set) -> set:
    return set_a.intersection(set_b)


def intersection_func_by_hand(set_a: set, set_b: set) -> set:
    common_values = set()
    for element in set_a:
        if element in set_b:
            common_values.add(element)
    return common_values


def intersection_oneline(set_a: set, set_b: set) -> set:
    return {element for element in set_a if element in set_b}
