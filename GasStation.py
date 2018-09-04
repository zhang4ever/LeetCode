#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : GasStation.py
# @Time    : 2018-09-04 18:42
# @Author  : zhang bo
# @Note    : Gas Station
"""
"""
题目描述：There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
示例：Input: gas  = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3
思路：首先必须要保证gas的总量>=cost的总量；从一个gas>cost的位置出发，此时的油箱里的gas的剩余量remain为gas-cost，依次用remain+=(gas-cost),
    如果某个环节的gas的remain<0,则需要重新选择开始的位置。整个过程的时间复杂度是O(n)
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return
        if sum(gas) < sum(cost):
            return -1
        remain = 0
        start = -1
        for i in range(len(gas)):
            if gas[i] >= cost[i] and start == -1:  # 选择该位置为start
                start = i
                remain = gas[i] - cost[i]
            else:  # 起点以后的位置
                remain += (gas[i] - cost[i])
                if remain < 0:  # 此时油量剩余不够，重新选择起始位置
                    start = -1
                    remain = 0
        return start


if __name__ == '__main__':
    solution = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(solution.canCompleteCircuit(gas, cost))
