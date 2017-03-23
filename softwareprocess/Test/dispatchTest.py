import unittest

import softwareprocess.dispatch as SM


class dispatchTest(unittest.TestCase):

    def setUp(self):
        self.nominalOpAdjustValues = {'observation' : '30d1.5' , 'height' : '19.0', 'pressure' : '1000', 'horizon' : 'artificial', 'op': 'adjust', 'temperature': '85'}
        pass

    def tearDown(self):
        pass

    #Happy path for stubbed out code
    def test100_000_OpPredictReturnsADictionary(self):
        self.assertIsInstance(SM.dispatch({'op' : 'predict'}), dict )

    # Some Sad paths, that came with the base code
    def test100_910_NoValuesGiven(self):
        self.assertEquals(SM.dispatch() , {'error': 'parameter is missing'})
    def test100_911_IsNotADictionary(self):
        self.assertEquals(SM.dispatch("123123"), {'error': 'parameter is not a dictionary'})
    def test100_912_NotOp(self):
        self.assertEquals(SM.dispatch( {'notop' : 'doesnt matter'}) , {'error': 'no op  is specified', 'notop':'doesnt matter'})

    # Added Sad paths

    def test200_910_OpAdjustButNoInformationGiven(self):
        self.assertEquals(SM.dispatch({'op' : 'adjust'}) , {'error' : 'mandatory information is missing'})

    # Added Happy paths

    def test200_100_OpAdjustReturnsAnAltitude(self):
        self.assertIsInstance(SM.dispatch(self.nominalOpAdjustValues) , dict)
        self.assertEquals('altitude' in SM.dispatch(self.nominalOpAdjustValues) , True)

