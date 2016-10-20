#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao16@uw.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
Reverse Integer
URL: https://leetcode.com/problems/reverse-integer/
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            sign = +1
        else:
            sign = -1
        x = abs(x)
        ans = 0
        while x > 0:
            ans = ans * 10 + (x % 10)
            x = x // 10
            if (ans < 1000000000 and ans > 214748364 and x > 0) or\
                    (ans == 214748364 and x > 7):
                return 0
        return ans * sign
