class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        romanDict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        for i in range(len(s) - 1):
            if romanDict[s[i]] < romanDict [s[i+1]]:
                ans -= romanDict[s[i]]
            else:
                ans+= romanDict[s[i]]
        
        return ans + romanDict[s[-1]] 
            

a = Solution()
b = Solution()
c = Solution()

respostaA = a.romanToInt("III")
respostaB = b.romanToInt("LVIII")
respostaC = c.romanToInt("MCMXCIV")

print(respostaA)
print(respostaB)
print(respostaC)
