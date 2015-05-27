__author__ = 'Valeria'
import unittest
from radix import *

class TestRadixMethods(unittest.TestCase):

    def test_to_base_10(self):
        self.assertEqual(to_base_10('cfa7291', 25), '3080188976')

    def test_from_base_10(self):
        self.assertEqual(from_base_10('1465324', 15), '1de284')

    def test_new_radix(self):
        self.assertEqual(new_radix('51330od', 26, 36), 'privet')

    def test_from_base_10_exception(self):
        with self.assertRaises(Exception):
            from_base_10('a453', 12)

    def test_to_base_10_exception(self):
        with self.assertRaises(Exception):
            to_base_10('a453', 9)

    def test_new_radix_exception(self):
        with self.assertRaises(Exception):
            new_radix('9453', 9, 5)

if __name__ == '__main__':
    unittest.main()