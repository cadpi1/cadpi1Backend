import ukcScraperUtils
import unittest

class testDetermineSessionTypeFromUKCGradeString(unittest.TestCase):
    def testSportFrenchGrade(self):
        inputGrade = "4a+"
        expectedOutput = "Sport"
        self.assertSessionType(inputGrade, expectedOutput)

    def testSportFrenchGradeHigher(self):
        inputGrade = "8c+"
        expectedOutput = "Sport"
        self.assertSessionType(inputGrade, expectedOutput)

    def testTradGradeLow(self):
        inputGrade = "S 4a"
        expectedOutput = "Trad"
        self.assertSessionType(inputGrade, expectedOutput)

    def testTradGradeMedium(self):
        inputGrade = "HVS 6b"
        expectedOutput = "Trad"
        self.assertSessionType(inputGrade, expectedOutput)

    def testTradGradeHigh(self):
        inputGrade = "E10 7c"
        expectedOutput = "Trad"
        self.assertSessionType(inputGrade, expectedOutput)

    def testBoulderingGradeLow(self):
        inputGrade = "5A"
        expectedOutput = "Bouldering"
        self.assertSessionType(inputGrade, expectedOutput)

    def testBoulderingGradeHigh(self):
        inputGrade= "8A+"
        expectedOutput = "Bouldering"
        self.assertSessionType(inputGrade, expectedOutput)

    def testPuntyViaFerrata(self):
        inputGrade = "VF4C"
        expectedOutput = "Other"
        self.assertSessionType(inputGrade, expectedOutput)

    def assertSessionType(self, inputStr, expected):
        self.assertEqual(ukcScraperUtils.determineSessionTypeFromUKCGradeString(inputStr), expected)


if __name__ == '__main__':
    unittest.main()