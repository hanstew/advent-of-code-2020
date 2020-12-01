import unittest
import day1


class TestDays(unittest.TestCase):

    def test_day1_module(self):
        mylist = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(day1.product_of_2020_x(mylist, 2), 514579)
        self.assertEqual(day1.product_of_2020_x(mylist, 3), 241861950)


if __name__ == "__main__":
    unittest.main()
