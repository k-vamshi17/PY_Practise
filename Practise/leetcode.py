# Divisible and Non - Divisible sum difference
# Input: n = 10, m = 3
# Output: 19
# Explanation: In the given example:
# - Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
# - Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
# We return 37 - 18 = 19 as the answer.

# n=5
# m=1
# lst=[]
# lst2=[]
# for i in range(1,n+1):
#     if i%m == 0:
#         lst.append(i)
#     else:
#         lst2.append(i)

# print(lst,lst2)
# div=0
# nondiv=0
# for i in lst:
#     div += i
# for i in lst2:
#     nondiv += i

# print(div,nondiv)
# print(nondiv-div)

##-----------------------------------------------------------------------------

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# nums = [2, 7, 11, 15]
# target = 9

# def two_sum(nums, target):
#     lookup = {}
#     i = 0
#     while i < len(nums):
#         complement = target - nums[i]
#         if complement in lookup:
#             return [lookup[complement], i]
#         lookup[nums[i]] = i
#         i += 1

# result = two_sum(nums, target)
# print(result)

#---------------------------------------------------------------- 

# def easytask(x, n, a):
#     seen = set()
#     count = 0
#     for num in a:
#         complement = x - num
#         if complement in seen:
#             count += 1
#         seen.add(num)
#     return count

# def main():
#     x = int(input())
#     n = int(input())
#     a = [int(input()) for _ in range(n)]
#     result = easytask(x, n, a)
#     print(result)

# if __name__ == "__main__":
#     main()