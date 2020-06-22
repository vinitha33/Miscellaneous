import unittest
import Ques4
class TestStringMethods(unittest.TestCase):
    def test_pali(self):
        x = [[1, 2],
             [3, 4]]

        y = [[5, 6],
             [7, 8]]

        res = [[6, 8],
               [10, 12]]

        res1 = [[5, 4],
                [7, 9]]


        self.assertNotEqual(Ques4.mat_add(x, y), res1)

        self.assertEqual(Ques4.mat_add(x, y), res)


if __name__ == '__main__':
    unittest.main()