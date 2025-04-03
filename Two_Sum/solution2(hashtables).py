class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numsSet = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsSet:
                return [numsSet[complement],i]
            numsSet[nums[i]] = i
            


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
resposta4 = d.twoSum(nums4,target4)

print(resposta1)
print(resposta2)
print(resposta3)
print(resposta4)