from testresult import TestResult

class TestSuite:
    def __init__(self):
        self.tests= []
        
    def add(self, test):
        self.tests.append(test)
        
    def run(self, result):
        for test in self.tests:
            test.run(result)