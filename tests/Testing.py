__author__ = 'Valeria'
import unittest
from radix import *
from timeit import timeit

class TestRadixPerformance(unittest.TestCase):
    def test_perf(self):
        def testtime():
            for i in range(1000):
                cast(i, 16, 32)
        timeit(testtime, number=1000)

class TestRadixMethods(unittest.TestCase):

    def test_to_base_10(self):
        self.assertEqual(to_base_10('cfa7291', 25), '3080188976')

    def test_from_base_10(self):
        self.assertEqual(from_base_10('1465324', 15), '1de284')

    def test_cast(self):
        self.assertEqual(cast('51330od', 26, 36), 'privet')

    def test_from_base_10_exception(self):
        with self.assertRaises(Exception):
            from_base_10('a453', 12)

    def test_to_base_10_exception(self):
        with self.assertRaises(Exception):
            to_base_10('a453', 9)

    def test_cast_exception(self):
        with self.assertRaises(Exception):
            cast('9453', 9, 5)

if __name__ == '__main__':
    unittest.main()