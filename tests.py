from fibon import fibonacci_number
import unittest


class TestPrintResults(unittest.TestCase):
    def test_check_number_1(self):
        n = 1
        self.assertEqual(fibonacci_number(n),1)

    def test_check_number_8(self):
    	n = 8
    	self.assertEqual(fibonacci_number(n), 21)

    def test_check_number_100(self):
    	n = 100
    	self.assertEqual(fibonacci_number(n),
    	 354224848179261915075)

if __name__ == '__main__':
    unittest.main()