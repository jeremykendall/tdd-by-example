import xunit

class TestCaseTest(xunit.TestCase):
    def setUp(self):
        self.test= xunit.WasRun("testMethod")
    
    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)
        
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
        
TestCaseTest("testSetUp").run()
TestCaseTest("testRunning").run()