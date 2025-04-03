class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
        
        return []

a = Solution()
nums1 = [2,7,11,15]
target1 = 9
resposta1 = a.twoSum(nums1,target1)

b = Solution()
nums2 = [3,2,4]
target2 = 6
resposta2 = b.twoSum(nums2,target2)

c = Solution()
nums3 = [3,3]
target3 = 6
resposta3 = c.twoSum(nums3,target3)

d = Solution()
nums4 = [3,3,9]
target4 = 12
resposta4 = c.twoSum(nums4,target4)


print(resposta1)
print(resposta2)
print(resposta3)
print(resposta4)