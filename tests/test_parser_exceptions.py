import unittest

from pysqljson import exceptions, Parser


class TestExceptions(unittest.TestCase):
    def test_pass_parse_string(self):
        with self.assertRaises(Exception) as cm:
            parser = Parser.Parser()
            parser.parse(None, {'test': 2}, [])
        expt = cm.exception
        self.assertEqual(expt.args[0], exceptions.ERROR_PASS_PARSE_STRING.args[0])

    def test_pass_parse_list(self):
        with self.assertRaises(Exception) as cm:
            parser = Parser.Parser()
            parser.parse(None, '{"test": 2}', 5)
        expt = cm.exception
        self.assertEqual(expt.args[0], exceptions.ERROR_PASS_PARSE_LIST.args[0])

    def test_pass_parse_prop(self):
        with self.assertRaises(Exception) as cm:
            parser = Parser.Parser()
            parser.parse(None, '{"test": 2}', [5])
        expt = cm.exception
        self.assertEqual(expt.args[0], exceptions.ERROR_ALLOWED_PROPS_MUST_BE_STRING.args[0])


if __name__ == '__main__':
    unittest.main()