import unittest
import functions

class Test_isAIntTest(unittest.TestCase):
    #tests if isAInt() returns False if input isn't int
    def test_isIntFalse(self):
        actRes = functions.isAInt("a")
        expRes = False
        self.assertEqual(expRes, actRes)

    # tests if isAInt() returns True if input is int
    def test_isIntTrue(self):
        actRes = functions.isAInt(1)
        expRes = True
        self.assertEqual(expRes, actRes)

class Test_isValidChoice(unittest.TestCase):
    #test if int is valid
    def test_isIntValidTrue(self):
        actRes = functions.isValidChoice("1")
        expRes = True
        self.assertEqual(expRes, actRes)
    #test if int isn't valid
    def test_isIntValidFalse(self):
        actRes = functions.isValidChoice("7")
        expRes = False
        self.assertEqual(expRes, actRes)

class Test_isValidName(unittest.TestCase):
    #test if length within valid range
    def test_isValidNameTrue(self):
        actRes = functions.isValidName("a")
        expRes = True
        self.assertEqual(expRes, actRes)

    #test if length not within valid range
    def test_isValidNameFalse(self):
        actRes = functions.isValidName("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaai")
        expRes = False
        self.assertEqual(expRes, actRes)

class Test_isValidPosition(unittest.TestCase):
    #test if position is valid
    def test_isValidPositionTrue(self):
        actRes = functions.isValidPosition("Centre")
        expRes = True
        self.assertEqual(expRes, actRes)
    #test if position isn't valid
    def test_isValidPositionFalse(self):
        actRes = functions.isValidPosition("Wing")
        expRes = False
        self.assertEqual(expRes, actRes)

class Test_isValidInputNumber(unittest.TestCase):
    #test if input is within input range
    def test_isValidInputNumberTrue(self):
        actRes = functions.isValidInputNumber(5, 1, 10)
        expRes = True
        self.assertEqual(expRes, actRes)

    #test if input isn't within input range
    def test_isValidInputNumberFalse(self):
        actRes = functions.isValidInputNumber(11, 1, 10)
        expRes = False
        self.assertEqual(expRes, actRes)

if __name__ == '__main__':
    unittest.main()