import unittest

testMasteryList = 0, 100, 173, 1000

class TestCatchEmAll(unittest.TestCase):
    def testSum(self):
        testMasteryListSum = 1273
        sumPoints = 0
        for cm in testMasteryList:
            sumPoints += cm
        self.assertEqual(testMasteryListSum, sumPoints, "Should be 1273")
        
    def testSumThreshold(self):
        sumPoints = 0
        threshold = 2
        testMasteryListSum = 100
        for cm in testMasteryList:
            if(len(testMasteryList) - testMasteryList.index(cm) > threshold):
                sumPoints += cm
        self.assertEqual(sumPoints, testMasteryListSum, "Should be 100")
    
    def testFilter(self):
        rank = 150
        filtered = filter(lambda cm: cm < rank, testMasteryList)
        sumFiltered = 0
        for cm in filtered:
            sumFiltered += cm
        self.assertEqual(sumFiltered, 100, "Should be 100")

if __name__ == '__main__':
    unittest.main()