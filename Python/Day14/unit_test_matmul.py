import unittest
import Ques5

class TestStringMethods(unittest.TestCase):
    def test_pali(self):
        A = [[1, 2],
             [3, 4]]

        B = [[5, 6],
             [7, 8]]

        res = [[19, 22],
                [43, 50]]

        res1 = [[5, 7],
                [6, 8]]


        self.assertEqual(Ques5.mat_mul(A, B), res)

        self.assertNotEqual(Ques5.mat_mul(A, B), res1)


if __name__ == '__main__':
    unittest.main()