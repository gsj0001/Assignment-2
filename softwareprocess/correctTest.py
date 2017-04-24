import unittest

import softwareprocess.correct as SM

class correctTest(unittest.TestCase):
    def test1000_MandatoryInformationMissing(self):
        self.assertEquals(SM.correct({'op':'correct'}), {'error':'mandatory information is missing', 'op':'correct'})