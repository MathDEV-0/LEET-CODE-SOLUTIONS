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

        total,prev = 0,0
        

        for i in reversed(s):
            current = romanDict[i]
            if current < prev:
                total -= current
            else:
                total += current
                prev = current

        return total

            

a = Solution()
b = Solution()
c = Solution()

respostaA = a.romanToInt("III")
respostaB = b.romanToInt("LVIII")
respostaC = c.romanToInt("MCMXCIV")

print(respostaA)
print(respostaB)
print(respostaC)
