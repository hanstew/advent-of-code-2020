import re
from collections import namedtuple
from typing import Callable

from util import get_input_lines

PassInfo = namedtuple("PassInfo", ["min", "max", "letter", "password"])


def parse_input_lines(input_lines: list) -> list:
    """
    Parse lines from input file to return PassInfo.

    "1-3 a: abcde"

    becomes...

    PassInfo.min: 1
    PassInfo.max: 3
    PassInfo.letter: a
    PassInfo.password: abcde
    """

    pass_info_list = []

    for line in input_lines:
        pattern = re.match(r"(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)", line)

        pass_info_list.append(
            PassInfo(
                min=int(pattern.group("min")),
                max=int(pattern.group("max")),
                letter=pattern.group("letter"),
                password=pattern.group("password"),
            )
        )

    return pass_info_list


def elf_password_check(pass_info: PassInfo) -> bool:
    """
    Check that a password matches the elf password policy.
    """

    # Count the number of times the letter appears in password.
    true_count = pass_info.password.count(pass_info.letter)

    # Check if this value is between the expected minimum
    # and maximum times the letter should appear in password.
    check_passed = pass_info.min <= true_count <= pass_info.max

    return check_passed


def corp_password_check(pass_info: PassInfo) -> bool:
    """
    Check that a password meets the Official Toboggan Corp
    policy.
    """

    # Remember that elves don't use index 0.
    pos1 = pass_info.min - 1
    pos2 = pass_info.max - 1

    truth_list = [
        pass_info.password[pos1] == pass_info.letter,
        pass_info.password[pos2] == pass_info.letter
    ]

    if all(truth_list) or not any(truth_list):
        return False
    else:
        return True


def count_valid_passwords(pass_info_list: list, policy_check: Callable) -> int:
    """
    Inpect list of password info to see how many meet the password
    policies.
    """
    counter = 0

    for pass_info in pass_info_list:
        if policy_check(pass_info):
            counter += 1

    return counter


if __name__ == "__main__":
    input_lines = get_input_lines()
    password_lines = parse_input_lines(input_lines=input_lines)

    ans1 = count_valid_passwords(password_lines, elf_password_check)
    ans2 = count_valid_passwords(password_lines, corp_password_check)

    print("{} passwords meet elf password policy\n"
          "{} passwords meet the Official Toboggan Corporate Policy"
          .format(ans1, ans2))
