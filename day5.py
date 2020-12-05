from util import get_input_lines


def binary_space_partition(space_binary: str, lower_letter: str, upper_letter: str, total_seats: int):

    possible_seats = list(range(0, total_seats))

    for letter in space_binary:
        midpoint = len(possible_seats) // 2

        if letter == lower_letter:
            possible_seats = possible_seats[:midpoint]

        elif letter == upper_letter:
            possible_seats = possible_seats[midpoint:]

        if len(possible_seats) == 1:
            return possible_seats[0]


def get_seat_id(space_binary: str) -> int:

    row = binary_space_partition(
        space_binary=space_binary[:7],
        lower_letter="F",
        upper_letter="B",
        total_seats=128
    )

    col = binary_space_partition(
        space_binary=space_binary[7:],
        lower_letter="L",
        upper_letter="R",
        total_seats=8
    )

    return (row * 8) + col


def get_all_seats(input_lines: list) -> list:
    seats = []

    for line in input_lines:
        seats.append(int(get_seat_id(line)))

    seats.sort()

    return seats


def compare_lists(seats: list):
    min = seats[0]
    max = seats[-1]

    all_seats = list(range(min, max))

    for seat in all_seats:
        if seat not in seats:

            # Interval between seat IDs is 8.
            if seat + 8 in seats and seat - 8 in seats:
                return seat

    else:
        print("Can't find a seat!")


def get_my_seat(input_lines: list) -> int:
    seats = get_all_seats(input_lines)
    my_seat = compare_lists(seats)

    return my_seat


def get_highest_seat(input_lines: list) -> int:

    max = 0

    for line in input_lines:
        id = get_seat_id(line)
        if id > max:
            max = id

    return max


if __name__ == "__main__":
    input_lines = get_input_lines()

    ans1 = get_highest_seat(input_lines)
    ans2 = get_my_seat(input_lines)

    print("ans 1 is {}\n"
          "ans 2 is {}\n".format(ans1, ans2)
          )


