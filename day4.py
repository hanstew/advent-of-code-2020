import re
from typing import Iterable

from util import get_input_lines

VALID = "VALID"
INVALID = "INVALID"


class Passport:
    def __init__(self, **credentials):
        self.cid = credentials.get("cid", INVALID)
        self.pid = credentials.get("pid", INVALID)
        self.ecl = credentials.get("ecl", INVALID)
        self.hcl = credentials.get("hcl", INVALID)
        self.hgt = credentials.get("hgt", INVALID)
        self.eyr = credentials.get("eyr", INVALID)
        self.iyr = credentials.get("iyr", INVALID)
        self.byr = credentials.get("byr", INVALID)

    def check_required_fields(self):
        """
        Check if all required fields are present.
        """
        required = [
            self.byr,
            self.iyr,
            self.eyr,
            self.hgt,
            self.hcl,
            self.ecl,
            self.pid
        ]

        if INVALID in required:
            return INVALID
        else:
            return VALID

    def validate_credentials(self):
        """
        Check if all required fields contain valid data.
        """
        try:
            # byr
            assert re.match(r"^\d{4}$", self.byr)
            assert 1920 <= int(self.byr) <= 2002

            # iyr
            assert re.match(r"^\d{4}$", self.iyr)
            assert 2010 <= int(self.iyr) <= 2020

            # eyr
            assert re.match(r"^\d{4}$", self.eyr)
            assert 2020 <= int(self.eyr) <= 2030

            # hgt
            height_pattern = re.match(r"^(?P<digits>\d+)(?P<unit>(cm)|(in))$", self.hgt)
            assert height_pattern

            digits = int(height_pattern.group("digits"))
            unit = height_pattern.group("unit")

            if unit == "cm":
                assert 150 <= digits
                assert digits <= 193
            elif unit == "in":
                assert 59 <= digits
                assert digits <= 76

            # hcl
            hcl_pattern = re.match(r"^#[0-9a-f]{6}$", self.hcl)
            assert hcl_pattern

            # ecl
            valid_eye_colours = [
                "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
            ]

            assert self.ecl in valid_eye_colours

            # pid
            pid_pattern = re.match(r"^[0-9]{9}$", self.pid)
            assert pid_pattern

        except AssertionError:
            return INVALID
        else:
            return VALID


def create_passports(input_list: list) -> Iterable:
    """
    Generator to create Passport instances from list
    of input lines.
    """
    credentials = {}

    for line in input_list:

        # Look for key:val patterns.
        line = line.split()
        pattern = re.compile(r"(?P<key>\w+):(?P<val>[\w#]+)")

        if line:
            for detail in line:
                try:
                    key = pattern.match(detail).group("key")
                    val = pattern.match(detail).group("val")
                    credentials.update({key: val})

                except AttributeError:
                    print("No match for {}".format(line))
        else:
            # A blank line means we have all the fields
            # present in this passport.
            passport = Passport(**credentials)
            yield passport
            credentials = {}

    # Remember any final input lines that aren't
    # followed by a blank line.
    if credentials:
        passport = Passport(**credentials)
        yield passport
        credentials = {}


def count_valid_passports(input_lines: list) -> (int, int):
    """
    Count passports with all required fields and
    all passports with valid data.
    """
    required_fields = 0
    valid_data = 0

    for passport in create_passports(input_lines):

        # Part 1
        if passport.check_required_fields() == VALID:
            required_fields += 1

        # Part 2
        if passport.validate_credentials() == VALID:
            valid_data += 1

    return required_fields, valid_data


if __name__ == "__main__":

    input_lines = get_input_lines()

    ans1, ans2 = count_valid_passports(input_lines)

    print("{} passports have all fields present\n"
          "{} passports have valid data\n"
          .format(ans1, ans2))
