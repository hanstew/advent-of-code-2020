from util import get_input_lines
from day1 import get_product


def count_trees(input_line_list: list, slope: int, down_slope: int = 1) -> int:
    """
    Count number of trees (represented by "#") for a
    given slope in a pattern.
    """
    tree_count = 0
    index = slope

    for linenum, line in enumerate(input_line_list[1:]):

        # If our slope requires us to drop more than
        # one row at a time, this will sort it.
        linenum = linenum + 1
        if not (linenum % down_slope == 0):
            continue

        # Count the trees :).
        if line[index] == "#":
            tree_count += 1

        # Reset index if we fall off the right
        # edge of the pattern.
        index += slope
        if index >= len(line):
            index = index - len(line)

    return tree_count


def part2(input_line_list):
    """
    Get the number of trees for various slopes
    and return the product.
    """
    trees_per_ride = [
        count_trees(input_line_list, 1),
        count_trees(input_line_list, 3),
        count_trees(input_line_list, 5),
        count_trees(input_line_list, 7),
        count_trees(input_line_list, 1, 2)
    ]

    tree_product = get_product(trees_per_ride)

    return tree_product


if __name__ == "__main__":
    input_lines = get_input_lines()

    ans1 = count_trees(input_lines, 3)
    ans2 = part2(input_lines)

    print("Trees in part 1: {}\n"
          "Trees in part 2: {}\n"
          "Watch out!! :o"
          .format(ans1, ans2))
