import xunit

class TestCaseTest(xunit.TestCase):
    def setUp(self):
        self.result = xunit.TestResult()
        
    def testTemplateMethod(self):
        test= xunit.WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)
        
    def testResult(self):
        test= xunit.WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())
        
    def testFailedResult(self):
        test = xunit.WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
        
    def testFailedResultFormatting(self):
        result = xunit.TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())
        
    def testSuite(self):
        suite= xunit.TestSuite()
        suite.add(xunit.WasRun("testMethod"))
        suite.add(xunit.WasRun("testBrokenMethod"))
        result= xunit.TestResult()
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())
        
suite = xunit.TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))
result = xunit.TestResult()
suite.run(result)
print result.summary()
