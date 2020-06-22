import unittest
import prac_Day2
class TestStringMethods(unittest.TestCase):
    def test_pali(self):
        x = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

        y = [[9, 8, 7],
             [6, 5, 4],
             [3, 2, 1]]

        res = [[3, 5, 7],
               [4, 7, 3],
               [6, 6, 8]]

        res1 = [[30, 24, 18],
                [84, 69, 54],
                [138, 114, 90]]


        self.assertNotEqual(prac_Day2.matmul(x, y), res)

        self.assertEqual(prac_Day2.matmul(x, y), res1)


if __name__ == '__main__':
    unittest.main()