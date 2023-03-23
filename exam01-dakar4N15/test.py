import unittest
from simplematrix import *


class Test01_Add2x2_Valid(unittest.TestCase):
    def test_list_int(self):
        a = [[5,2],[8,7]]
        b = [[3,1],[6,4]]
        c = matrix_math(matrix_a = a, matrix_b = b, mode = "add")
        self.assertEqual(c, [[8, 3], [14, 11]])

class Test02_Add3x3_Valid(unittest.TestCase):
    def test_list_int(self):
        a = [[9,5,2],[8,2,7],[6,3,1]]
        b = [[2,3,1],[6,9,4],[5,2,0]]
        c = matrix_math(matrix_a = a, matrix_b = b, mode = "add")
        self.assertEqual(c, [[11, 8, 3], [14, 11, 11], [11, 5, 1]])

class Test03_Subtract2x2_Valid(unittest.TestCase):
    def test_list_int(self):
        a = [[5,2],[8,7]]
        b = [[3,1],[6,4]]
        c = matrix_math(matrix_a = a, matrix_b = b, mode = "subtract")
        self.assertEqual(c, [[2, 1], [2, 3]])

class Test04_Subtract3x3_Valid(unittest.TestCase):
    def test_list_int(self):
        a = [[9,5,2],[8,2,7],[6,3,1]]
        b = [[2,3,1],[6,9,4],[5,2,0]]
        c = matrix_math(matrix_a = a, matrix_b = b, mode = "subtract")
        self.assertEqual(c, [[7, 2, 1], [2, -7, 3], [1, 1, 1]])

class Test05_MatrixA_NotSquare(unittest.TestCase):
    def test_list_int(self):
        a = [[5,2],[8,7,9]]
        b = [[3,1],[6,4]]
        c = matrix_math(matrix_a = a, matrix_b = b, mode = "add")
        self.assertEqual(c, False)

class Test06_MatrixA_NotInt(unittest.TestCase):
    def test_list_int(self):
        a = [[5,2.1],[8,7]]
        b = [[3,1],[6,4]]
        c = matrix_math(matrix_a = a, matrix_b = b, mode = "add")
        self.assertEqual(c, False)

class Test07_MatrixB_NotSquare(unittest.TestCase):
    def test_list_int(self):
        a = [[5,2],[8,7]]
        b = [[3,1],[6,4,9]]
        c = matrix_math(matrix_a = a, matrix_b = b, mode = "add")
        self.assertEqual(c, False)

class Test08_MatrixB_NotInt(unittest.TestCase):
    def test_list_int(self):
        a = [[5,2],[8,7]]
        b = [[3,1.1],[6,4]]
        c = matrix_math(matrix_a = a, matrix_b = b, mode = "add")
        self.assertEqual(c, False)

class Test09_MatrixA_MatrixB_NotSameSize(unittest.TestCase):
    def test_list_int(self):
        a = [[5,2],[8,7]]
        b = [[2,3,1],[6,9,4],[5,2,0]]
        c = matrix_math(matrix_a = a, matrix_b = b, mode = "add")
        self.assertEqual(c, False)


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
