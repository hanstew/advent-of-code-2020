import unittest
import day1
import day2


class TestDays(unittest.TestCase):

    def test_day1_module(self):
        mylist = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(day1.product_of_2020_x(mylist, 2), 514579)
        self.assertEqual(day1.product_of_2020_x(mylist, 3), 241861950)

    def test_day2_module(self):
        passinfo = [
            day2.PassInfo(
                min=1,
                max=3,
                letter="a",
                password="abcde"
            ),
            day2.PassInfo(
                min=1,
                max=3,
                letter="b",
                password="cdefg"
            ),
            day2.PassInfo(
                min=2,
                max=9,
                letter="c",
                password="ccccccccc"
            )
        ]

        self.assertEqual(day2.count_valid_passwords(passinfo, day2.elf_password_check), 2)
        self.assertEqual(day2.count_valid_passwords(passinfo, day2.corp_password_check), 1)


if __name__ == "__main__":
    unittest.main()
