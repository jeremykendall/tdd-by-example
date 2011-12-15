import xunit

class TestCaseTest(xunit.TestCase):
    def testTemplateMethod(self):
        test= xunit.WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
        
    def testResult(self):
        test= xunit.WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())
        
    def testFailedResult(self):
        test = xunit.WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())
        
    def testFailedResultFormatting(self):
        result = xunit.TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())
        
# Kent starts Chapter 23 by mentioning how ratty this looks (I cheated 
# and looked ahead), but I don't see where he ever showed us that he was
# printing the summaries like he is below.  I updated it early because I wanted
# to see it.  Nice :-)
print TestCaseTest("testTemplateMethod").run().summary()
print TestCaseTest("testResult").run().summary()
print TestCaseTest("testFailedResultFormatting").run().summary()
print TestCaseTest("testFailedResult").run().summary()