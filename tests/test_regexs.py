import unittest

from pysqljson import regexs


class TestRegexs(unittest.TestCase):
    def test_match(self):
        self.assertTrue(regexs._match('dwa', 'dwa'))
        self.assertTrue(regexs._match('d.*', 'dwa'))

    def test_and(self):
        self.assertTrue(regexs.regex_and('&&'))
        self.assertFalse(regexs.regex_and('&'))
        self.assertFalse(regexs.regex_and('!!'))
        self.assertFalse(regexs.regex_and('asd'))

    def test_or(self):
        self.assertTrue(regexs.regex_or('||'))
        self.assertFalse(regexs.regex_or('&'))
        self.assertFalse(regexs.regex_or('%@'))
        self.assertFalse(regexs.regex_or('asd'))

    def test_eq(self):
        self.assertTrue(regexs.regex_eq('='))
        self.assertFalse(regexs.regex_eq('&'))
        self.assertFalse(regexs.regex_eq('%@'))
        self.assertFalse(regexs.regex_eq('asd'))

    def test_neq(self):
        self.assertTrue(regexs.regex_neq('!='))
        self.assertFalse(regexs.regex_neq('&'))
        self.assertFalse(regexs.regex_neq('%@'))
        self.assertFalse(regexs.regex_neq('asd'))

    def test_lt(self):
        self.assertTrue(regexs.regex_lt('<'))
        self.assertFalse(regexs.regex_lt('&'))
        self.assertFalse(regexs.regex_lt('%@'))
        self.assertFalse(regexs.regex_lt('asd'))

    def test_le(self):
        self.assertTrue(regexs.regex_le('<='))
        self.assertFalse(regexs.regex_le('&'))
        self.assertFalse(regexs.regex_le('%@'))
        self.assertFalse(regexs.regex_le('asd'))

    def test_gt(self):
        self.assertTrue(regexs.regex_gt('>'))
        self.assertFalse(regexs.regex_gt('&'))
        self.assertFalse(regexs.regex_gt('%@'))
        self.assertFalse(regexs.regex_gt('asd'))

    def test_ge(self):
        self.assertTrue(regexs.regex_ge('>='))
        self.assertFalse(regexs.regex_ge('&'))
        self.assertFalse(regexs.regex_ge('%@'))
        self.assertFalse(regexs.regex_ge('asd'))

    def test_in(self):
        self.assertTrue(regexs.regex_in('in'))
        self.assertFalse(regexs.regex_in('&'))
        self.assertFalse(regexs.regex_in('%@'))
        self.assertFalse(regexs.regex_in('asd'))

    def test_like(self):
        self.assertTrue(regexs.regex_like('like'))
        self.assertFalse(regexs.regex_like('&'))
        self.assertFalse(regexs.regex_like('%@'))
        self.assertFalse(regexs.regex_like('asd'))

    def test_bt(self):
        self.assertTrue(regexs.regex_bt('..'))
        self.assertFalse(regexs.regex_bt('&'))
        self.assertFalse(regexs.regex_bt('%@'))
        self.assertFalse(regexs.regex_bt('asd'))


if __name__ == '__main__':
    unittest.main()
