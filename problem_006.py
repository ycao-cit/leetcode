#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao16@uw.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
ZigZag conversion
URL: https://leetcode.com/problems/zigzag-conversion/
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                x = i
                while (x < len(s)):
                    ans += s[x]
                    x += 2 * numRows - 2
            else:
                x = i
                y = 2 * numRows - 2 - x
                while (y < len(s)):
                    ans += s[x] + s[y]
                    x += 2 * numRows - 2
                    y += 2 * numRows - 2
                if x < len(s):
                    ans += s[x]
        return ans
