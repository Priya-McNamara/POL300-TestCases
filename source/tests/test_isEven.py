import unittest

class TestCases(unittest.TestCase):
    def test(self):
        print("Trying input 0: function returns --", isEven(0))
        self.assertTrue(isEven(0))
        print("Trying input 64: function returns --", isEven(64))
        self.assertTrue(isEven(64))
        print("Trying input 754: function returns --", isEven(754))
        self.assertTrue(isEven(754))
        print("Trying input 33: function returns --", isEven(33))
        self.assertFalse(isEven(33))
        print("Trying input 79: function returns --", isEven(79))
        self.assertFalse(isEven(79))
        print("Trying input 1: function returns --", isEven(1))
        self.assertFalse(isEven(1))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
