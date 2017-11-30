from Obfuscatr import Obfuscatr
import unittest

class TestObfuscatrCases(unittest.TestCase):

    def test_simple_string_obfuscation(self):
        obf = Obfuscatr()
        self.assertEqual('Person', obf.obfuscate('test'))

    def test_simple_array_obfuscation(self):
        obf = Obfuscatr()
        self.assertEqual('Border', obf.obfuscate(['test','test2']))

    def test_simple_dictionary_obfuscation(self):
        obf = Obfuscatr()
        self.assertEqual('Pine', obf.obfuscate({'test':'test2'}))

    def test_result_is_static(self):
        word = 'Test1'
        result1 = Obfuscatr().obfuscate(word)
        result2 = Obfuscatr().obfuscate(word)
        self.assertEqual(result1, result2)

    def test_more_words(self):
        obf = Obfuscatr()
        obf.words_count = 3
        self.assertEqual('PersonBrightTaboo', obf.obfuscate('test'))

    def test_custom_delimiter(self):
        obf = Obfuscatr()
        obf.words_count = 3
        obf.delimiter = ' * '
        self.assertEqual('Person * Bright * Taboo', obf.obfuscate('test'))

if __name__ == '__main__':
    unittest.main()