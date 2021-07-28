import unittest
import appid
import wolf


class Wolftest(unittest.TestCase):
    test = wolf.wolframAlpha()
    appID = appid.appID

    def testConverter(self):
        self.assertEqual(self.test.stringConverter("Hi Dude?"),"Hi+Dude%3F")

    def testAssembler(self):
        self.assertEqual(self.test.questionAssembler("Hi+Dude%3F"), "http://api.wolframalpha.com/v1/simple?appid={}&i=Hi+Dude%3F".format(self.appID))

    def testRequest(self):
        pass

    def testFile(self):
        pass

    def testAll(self):
        pass