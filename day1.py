# import time

from util import get_input_lines
import itertools

# Not needed.
def filter_costs(cost_list: list) -> list:
    """
    Remove any costs greater than 2020.
    """
    new_list = [int(x) for x in cost_list if int(x) <= 2020]
    return new_list

# Easy but impractical.
def get_2020(cost_list: list) -> int:
    """
    A simple but not too efficient way
    to get the answer :D.
    """
    for x in cost_list:
        for y in cost_list:
            for z in cost_list:
                if sum([x, y, z]) == 2020:
                    # pduct = math.prod([x, y, z])
                    pduct = get_product([x, y, z])
                    return pduct
                else:
                    continue

def get_product(args: (tuple, list)) -> int:
    """
    Get product of a list/tuple of ints.
    """
    product = args[0]

    for arg in args[1:]:
        product *= arg

    return product

# A little better :)
def product_of_2020_x(cost_list: list, x: int) -> int:
    """
    Get the x values from a list that sum to 2020
    and return the product.
    """
    # Get all possible combinations of the list
    # repeated x times.
    combos = itertools.combinations(cost_list, x)
    for combo in combos:
        if sum(combo) == 2020:
            # python 3.8+
            # pduct = math.prod(combo)

            pduct = get_product(combo)

            return pduct
    else:
        raise Exception("No combos add to 2020... "
                        "Elves on the mulled wine again?")


if __name__ == "__main__":

    cost_list = get_input_lines()
    cost_list = filter_costs(cost_list)

    # start = time.time()
    # p2 = get_2020(cost_list)
    # p3 = get_2020(cost_list)
    # end = time.time()
    # print("Time for get_2020: {}".format(end - start))

    # start = time.time()
    p2 = product_of_2020_x(cost_list, 2)
    p3 = product_of_2020_x(cost_list, 3)
    # end = time.time()
    # print("Time for product_of_2020_x: {}".format(end - start))

    print("Answer 1 is {}\n"
          "Answer 2 is {}\n"
          "Happy accounting :D".format(p2, p3))
