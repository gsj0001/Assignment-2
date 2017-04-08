import unittest

import softwareprocess.predict as SM

class predictTest(unittest.TestCase):

    def test1000_MandatoryInformationMissing(self):
        self.assertEquals(SM.predict({'op':'predict'}), {'error':'mandatory information is missing', 'op':'predict'})

    def test1001_BodyUnknown(self):
        self.assertEquals(SM.predict({'op':'predict', 'body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42'}), {'op':'predict', 'body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42', 'error' : 'star not in catalog'})

    def test1002_InvalidDate(self):
        self.assertEquals(SM.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42'}), {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42', 'error': 'invalid date'})

    def test1003_DateNotIncluded(self):
        testDict = SM.predict({'op':'predict', 'body': 'Betelgeuse', 'time': '03:15:42'})
        self.assert(testDict['date'] = '2001-01-01')
