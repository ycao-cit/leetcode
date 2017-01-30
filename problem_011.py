#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao16@uw.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
Container With Most Water
URL: https://leetcode.com/problems/container-with-most-water/
"""


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = 0
        while (j > i):
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                k = i
                while (k < j and height[k] <= height[i]):
                    k += 1
                i = k
            else:
                k = j
                while (k > i and height[k] <= height[j]):
                    k -= 1
                j = k
        return max_area
