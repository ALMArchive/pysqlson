import unittest

from pysqljson import utilities


class TestUtilities(unittest.TestCase):
    def test_num(self):
        self.assertTrue(utilities.is_num(2))
        self.assertFalse(utilities.is_num(''))
        self.assertFalse(utilities.is_num([]))

    def test_str(self):
        self.assertTrue(utilities.is_str(''))
        self.assertFalse(utilities.is_str(2))
        self.assertFalse(utilities.is_str([]))

    def test_list(self):
        self.assertTrue(utilities.is_list([]))
        self.assertFalse(utilities.is_list(2))
        self.assertFalse(utilities.is_list(''))

    def test_dict(self):
        self.assertTrue(utilities.is_dict({}))
        self.assertFalse(utilities.is_dict([]))
        self.assertFalse(utilities.is_dict(2))
        self.assertFalse(utilities.is_dict(''))

    def test_includes(self):
        self.assertTrue(utilities.includes([1, 2, 3], 1))
        self.assertTrue(utilities.includes(['a', 'b', 'c'], 'a'))
        self.assertFalse(utilities.includes([1, 2, 3], 4))
        self.assertFalse(utilities.includes(['a', 'b', 'c'], 'd'))


if __name__ == '__main__':
    unittest.main()
