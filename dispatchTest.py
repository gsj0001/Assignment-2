import unittest
import dispatch as SM
import math

class dispatchTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Some Sad paths, that came with the base code
    def test100_910_NoValuesGiven(self):
        self.assertEquals(SM.dispatch() , {'error': 'parameter is missing'})
    def test100_911_IsNotADictionary(self):
        self.assertEquals(SM.dispatch("123123"), {'error': 'parameter is not a dictionary'})
    def test100_912_NotOp(self):
        self.assertEquals(SM.dispatch( {'notop' : 'doesnt matter'}) , 'no op  is specified')
