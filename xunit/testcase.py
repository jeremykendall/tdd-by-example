from testresult import TestResult

class TestCase:
    def __init__(self, name):
        self.name= name
        
    def setUp(self):
        pass
        
    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        
    def tearDown(self):
        pass
