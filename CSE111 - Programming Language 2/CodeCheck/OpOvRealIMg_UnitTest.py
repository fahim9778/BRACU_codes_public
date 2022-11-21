# Create a unit test for the Complex class
# and overload the + operator to add two complex numbers

import unittest, OpOVRealImg

class TestComplex(unittest.TestCase):
    def test_add1(self):
        c1 = OpOVRealImg.Complex(2, 3)
        c2 = OpOVRealImg.Complex(4, 5)
        c3 = c1 + c2
        self.assertEqual(c3.real, 6)
        self.assertEqual(c3.img, 8)

    def test_add2(self):
        c4 = OpOVRealImg.Complex(-2, 3)
        c5 = OpOVRealImg.Complex(4, -5)
        c6 = c4 + c5
        self.assertEqual(c6.real, 2)
        self.assertEqual(c6.img, -2)
    
    def test_add3(self):
        c7 = OpOVRealImg.Complex(0, 0)
        c8 = OpOVRealImg.Complex(0, 0)
        c9 = c7 + c8
        self.assertEqual(c9.real, 0)
        self.assertEqual(c9.img, 0)

if __name__ == '__main__':
    unittest.main()