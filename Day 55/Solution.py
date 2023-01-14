class Solution(object):
    def romanToInt(self, s):
        walker, runner = 0, 1
        returnedInt = 0
        romanDict = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        
        while runner < len(s):
            if romanDict[s[walker]] >= romanDict[s[runner]]:
                returnedInt += romanDict[s[walker]]                
                walker += 1
                runner += 1
            else:
                returnedInt += (romanDict[s[runner]] - romanDict[s[walker]])
                walker += 2
                runner += 2
                
        if runner == len(s):
            returnedInt += romanDict[s[runner-1]]
        return returnedInt
