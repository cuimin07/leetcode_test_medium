'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''

#答：【双指针】
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sums = nums[start] + nums[end] + nums[i]
                if abs(target - sums) < abs(target - ans):
                    ans = sums
                if sums > target:
                    end -= 1
                elif sums < target:
                    start += 1
                else:
                    return ans
        return ans
