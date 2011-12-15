import xunit

class TestCaseTest(xunit.TestCase):
    def testRunning(self):
        test= xunit.WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
        
TestCaseTest("testRunning").run()    