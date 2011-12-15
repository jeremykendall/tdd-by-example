from testcase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        
    def setUp(self):
        self.log = "setUp "
        
    def testMethod(self):
        self.log = self.log + "testMethod "
        
    def testBrokenMethod(self):
        raise Exception
        
    def tearDown(self):
        self.log = self.log + "tearDown "
