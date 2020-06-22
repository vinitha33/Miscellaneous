import unittest
import Ques8, Ques9, Ques10, Ques11, Ques12
class TestStringMethods(unittest.TestCase):

    def test_long_alpha(self):
        str1 = "abcaklmoeeffd"
        res = "aklmo"
        res1 = "abcaklmo"

        self.assertEqual(Ques8.long_alpha(str1), res)
        self.assertNotEqual(Ques8.long_alpha(str1), res1)

    def test_count_occur(self):
        num = 5
        res = 1
        res1 = 2

        self.assertEqual(Ques9.count_occur(num), res)
        self.assertNotEqual(Ques9.count_occur(num), res1)

    def test_asc_vow(self):
        str1 = "I am reading a book"
        res = "reading book a am I"
        res1 = "book reading I am a"

        self.assertEqual(Ques10.asc_vow(str1), res)
        self.assertNotEqual(Ques10.asc_vow(str1), res1)

    def test_mat_mul_spiral(self):
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
                [54, 90, 114],
                [138, 84, 69]]


        self.assertNotEqual(Ques11.mat_mul_spiral(x, y), res)

        self.assertEqual(Ques11.mat_mul_spiral(x, y), res1)

    def test_maxi_pali(self):
        str1 = "cabbagemalayalamadam"
        res = 9
        res1 = 4

        self.assertEqual(Ques12.max_pali(str1), res)
        self.assertNotEqual(Ques12.max_pali(str1), res1)




if __name__ == '__main__':
    unittest.main()