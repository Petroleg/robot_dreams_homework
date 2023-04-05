def symmetric_difference_function(set_a: set, set_b: set) -> set:
    return set_a.symmetric_difference(set_b)


def symmetric_difference_function_by_hand(set_a: set, set_b: set) -> set:
    common_values = set()
    for element in set_a:
        if element not in set_b:
            common_values.add(element)
    for element in set_b:
        if element not in set_a:
            common_values.add(element)
    return common_values


def symmetric_difference_oneline(set_a: set, set_b: set) -> set:
    return set_a - set_b | set_b - set_a

def symmetric_difference_oneline_more(set_a: set, set_b: set) -> set:
    return set_a ^ set_b