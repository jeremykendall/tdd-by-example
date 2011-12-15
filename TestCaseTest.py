import xunit

class TestCaseTest(xunit.TestCase):
    def testTemplateMethod(self):
        test= xunit.WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
        
TestCaseTest("testTemplateMethod").run()