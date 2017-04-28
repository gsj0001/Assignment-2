import unittest

import softwareprocess.correct as SM
import math

class correctTest(unittest.TestCase):
    def test1000_MandatoryInformationMissing(self):
        self.assertEquals(SM.correct({'op':'correct'}), {'error':'mandatory information is missing', 'op':'correct'})
    def test1001_LatMissing(self):
        self.assertEquals(SM.correct({'op':'correct', 'long':'95d41.6','altitude':'13d42.3','assumedLat':'-53d38.4','assumedLong':'74d35.3'}),
                                     {'error':'mandatory information is missing', 'op':'correct'})
    def test1002_InvalidLat(self):
        self.assertEquals(SM.correct({'op':'correct', 'lat': '16.0d32.3', 'long':'95d41.6','altitude':'13d42.3','assumedLat':'-53d38.4','assumedLong':'74d35.3'}),
                                     {'op': 'correct', 'lat': '16.0d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                                      'assumedLat': '-53d38.4', 'assumedLong': '74d35.3','error':'invalid lat'})
    def test1003_InvalidAssumedLat(self):
        self.assertEquals(SM.correct({'op':'correct', 'lat': '16d32.3', 'long':'95d41.6','altitude':'13d42.3','assumedLat':'-153d38.4','assumedLong':'74d35.3'}),
                                     {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                                      'assumedLat': '-153d38.4', 'assumedLong': '74d35.3','error':'invalid assumedLat'})
    # def test2000_ValueCheck(self):
    #     self.assertEquals(SM.correct({'op':'correct', 'lat': '16d32.3', 'long':'95d41.6','altitude':'13d42.3','assumedLat':'-53d38.4','assumedLong':'74d35.3'}),
    #                       {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
    #                        'assumedLat': '-153d38.4', 'assumedLong': '74d35.3', 'correctedDistance': '-3950', 'correctedAzimuth': '164d43.1'})

    def test3000_simplifyRadians(self):
        self.assertAlmostEquals(SM.simplifyRadians(24 * math.pi) , 0)

    def test3001_convertRadiansToDegrees(self):
        self.assertAlmostEquals(SM.convertRadiansToDegrees(math.pi), [180, 0.0])

    def test3002_convertStringToRadians(self):
        self.assertAlmostEquals(SM.converStringToRadians('180d0.0'), math.pi)