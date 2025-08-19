import unittest

class TestCases(unittest.TestCase):
    def test_age_65(self):
        print("Trying input 65: function returns --", qualifyForMedicare(65))
        self.assertTrue(qualifyForMedicare(65))

    def test_age_64(self):
        print("Trying input 64: function returns --", qualifyForMedicare(64))
        self.assertFalse(qualifyForMedicare(64))

    def test_age_72(self):
        print("Trying input 72: function returns --", qualifyForMedicare(72))
        self.assertTrue(qualifyForMedicare(72))

    def test_age_18(self):
        print("Trying input 18: function returns --", qualifyForMedicare(18))
        self.assertFalse(qualifyForMedicare(18))


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
