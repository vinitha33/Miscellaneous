import unittest
import Ques3
class TestStringMethods(unittest.TestCase):
    def test_pali(self):
        str1 = "abba"
        str2 = "ghfjhg"
        self.assertTrue(Ques3.is_palindrome(str1), True)
        self.assertFalse(Ques3.is_palindrome(str2), False)


if __name__ == '__main__':
    unittest.main()