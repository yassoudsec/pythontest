import unittest
from library import *

class MyTest(unittest.TestCase):
    
    #debut test puissance
    def test_puissancee(self)
    self.assertFalse(puissance(2,2), 4)
    #fin test

    def test_increment(self):
        self.assertEqual(increment(3), 4)

    def test_sum_val(self):
        self.assertEqual(sum_val(3,5), 8)
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()