import unittest

import softwareprocess.predict as SM

class predictTest(unittest.TestCase):

    def test1000_MandatoryInformationMissing(self):
        self.assertEquals(SM.predict({'op':'predict'}), {'error':'mandatory information is missing', 'op':'predict'})