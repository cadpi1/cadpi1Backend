import re

def determineSessionTypeFromUKCGradeString(gradeInput):
    sportPattern = re.compile("[0-9][a-c\+].*?")
    boulderingPattern = re.compile('(^[0-9][A-C].*?|.*?V[0-9].*?)')
    tradPattern = re.compile('(.*?(D|S|VS|HVS|E[0-9]).*?|.*?5\.[0-9]*.*?)')
    if(boulderingPattern.search(gradeInput)):
        return 'Bouldering'
    if(tradPattern.search(gradeInput)):
        return 'Trad'
    if(sportPattern.search(gradeInput)):
        return 'Sport'
    return 'Other'

