#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MedianOfTwoSortedArrays.py
# @Time    : 2018-09-10 23:02
# @Author  : zhang bo
# @Note    : Median of Two Sorted Arrays
"""
"""
题目描述：There are two sorted arrays nums1 and nums2 of size m and n respectively.Find the median of the two sorted arrays.
示例：nums1 = [1, 3], nums2 = [2]；The median is 2.0
    nums1 = [1, 2], nums2 = [3, 4];The median is (2 + 3)/2 = 2.5
限制条件：The overall run time complexity should be O(log (m+n)).

"""
class Solution:
    # 思路1:最常规的解法，就是先将两个数组进行合并，合并后在根据元素的个数的奇偶来确定中位数,时间O(m+n)， 空间O(m+n)
    def findMedianSortedArrays1(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m == 0:
            return self.getMedianOfArray(nums2)
        if n == 0:
            return self.getMedianOfArray(nums1)
        nums = [0] * (m+n)
        count = 0
        i, j = 0, 0
        while count < (m+n):
            if i == m:
                while j != n:
                    nums[count] = nums2[j]
                    count += 1
                    j += 1
                break
            if j == n:
                while i != m:
                    nums[count] = nums1[i]
                    count += 1
                    i += 1
                break
            if nums1[i] < nums2[j]:
                nums[count] = nums1[i]
                count += 1
                i += 1
            else:
                nums[count] = nums2[j]
                count += 1
                j += 1

        return self.getMedianOfArray(nums)

    # 思路2:不需要真的去排序，只是要找到中位数的位置即可,时间O(m+n), 空间O(1)
    def findMedianSortedArrays2(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0 or nums1 == nums2:
            return self.getMedianOfArray(nums1) or self.getMedianOfArray(nums2)
        left = right = min(nums1[0], nums2[0])
        i, j = 0, 0  # 指向nums1和nums2的指针
        for _ in range((m + n)//2+1):
            left = right
            if i < m and (j >= n or nums1[i] < nums2[j]):
                right = nums1[i]
                i += 1
            else:
                right = nums2[j]
                j += 1
        print(left, right)
        if (m + n) % 2 == 0:
            return (left + right) / 2
        else:
            return right

    # 思路3:二分的思路，时间O(log(m+n))
    def findMedianSortedArrays3(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if (m+n) % 2 == 1:
            return self.findKthLeastNumSortedArrays(nums1, 0, m-1, nums2, 0, n-1, (m+n)//2)
        else:
            return (self.findKthLeastNumSortedArrays(nums1, 0, m-1, nums2, 0, n-1, (m+n)//2)+\
                self.findKthLeastNumSortedArrays(nums1, 0, m - 1, nums2, 0, n - 1, (m+n)//2+1))*0.5

    # 在两个排序数组中找到第k小的元素
    def findKthLeastNumSortedArrays(self, nums1, st1, end1, nums2, st2, end2, k):
        m, n = end1 - st1 + 1, end2 - st2+1
        if m > n:
            return self.findKthLeastNumSortedArrays(nums2, st2, end2, nums1, st1, end1, k)
        if m == 0:
            return nums2[st2 + k-1]
        if k == 1:
            return min(nums1[st1], nums2[st2])
        i = st1 + min(k//2, m) - 1
        j = st2 + min(k//2, n) - 1
        if nums2[i] >= nums1[j]:
            return self.findKthLeastNumSortedArrays(nums1, i+1, end1, nums2, st2, end2, k-(i-st1+1))
        else:
            return self.findKthLeastNumSortedArrays(nums1, st1, end1, nums2, j+1, end2, k-(j-st2+1))


    def getMedianOfArray(self, array):
        n = len(array)
        if n == 0:
            return
        if n % 2 == 0: # 偶数
            return (array[n//2-1] + array[n//2]) / 2
        else:
            return array[n//2]


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 5]
    nums2 = [3, 4]
    print(solution.findMedianSortedArrays3(nums1, nums2))