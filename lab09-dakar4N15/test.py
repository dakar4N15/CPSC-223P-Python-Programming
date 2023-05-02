# Name: William Sutanto
# Date: 4/19/2023
# File Purpose: Lab09 custom test file

import unittest
import io
from si import SimpleInteger

class Test01_add_valid_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test add function with valid integer inputs
        Expected output: 3
        """
        obj = SimpleInteger()
        res = obj.add(1, 2)
        self.assertEqual(3, res)

class Test02_add_invalid_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test add function with invalid float input
        Expected output: None
        """
        obj = SimpleInteger()
        res = obj.add(1.5, 2)
        self.assertEqual(None, res)

class Test03_subtract_valid_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test subtract function with valid integer inputs
        Expected output: -4
        """
        obj = SimpleInteger()
        res = obj.subtract(3, 7)
        self.assertEqual(-4, res)

class Test04_subtract_invalid_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test subtract function with invalid float input
        Expected output: None
        """
        obj = SimpleInteger()
        res = obj.subtract(3.5, 7)
        self.assertEqual(None, res)

class Test05_multiply_valid_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test multiply function with valid integer inputs
        Expected output: 15
        """
        obj = SimpleInteger()
        res = obj.multiply(5, 3)
        self.assertEqual(15, res)

class Test06_multiply_invalid_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test multiply function with invalid float input
        Expected output: None
        """
        obj = SimpleInteger()
        res = obj.multiply(5.5, 3)
        self.assertEqual(None, res)

class Test07_isequal_valid_true_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test isequal function with valid integer inputs that are equal
        Expected output: True
        """
        obj = SimpleInteger()
        res = obj.isequal(7, 7)
        self.assertEqual(True, res)

class Test08_isequal_valid_false_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test isequal function with valid integer inputs that are not equal
        Expected output: False
        """
        obj = SimpleInteger()
        res = obj.isequal(7, 8)
        self.assertEqual(False, res)

class Test09_isequal_invalid_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test isequal function with invalid float input
        Expected output: None
        """
        obj = SimpleInteger()
        res = obj.isequal(7.5, 7)
        self.assertEqual(None, res)

class Test10_isgreaterthan_valid_true_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test isgreaterthan function with valid integer inputs where a is greater than b
        Expected output: True
        """
        obj = SimpleInteger()
        res = obj.isgreaterthan(10, 6)
        self.assertEqual(True, res)

class Test11_isgreaterthan_valid_false_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test isgreaterthan function with valid integer inputs where a is not greater than b
        Expected output: False
        """
        obj = SimpleInteger()
        res = obj.isgreaterthan(10, 10)
        self.assertEqual(False, res)

class Test12_isgreaterthan_invalid_data(unittest.TestCase):
    def test_list_int(self):
        """
        Test isgreaterthan function with invalid float inputs
        Expected output: None
        """
        obj = SimpleInteger()
        res = obj.isgreaterthan(10.5, 6)
        self.assertEqual(None, res)

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)