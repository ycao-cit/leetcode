#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao@astro.caltech.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
Two sum
URL: https://leetcode.com/problems/two-sum/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[int]
        """
        lookup_table = {}
        for i in range(len(nums)):
            j = lookup_table.get(target - nums[i])
            if j is None:
                lookup_table[nums[i]] = i
            else:
                return j, i
