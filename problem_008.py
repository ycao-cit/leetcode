#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao16@uw.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
String to Integer
URL: https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0
        i = 0
        sign = +1
        if str[0] in ("-", "+"):
            i = 1
            if str[0] == "-":
                sign = -1
        ans = 0
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        while (i < len(str)):
            if not str[i].isdigit():
                break
            digit = int(str[i])
            if ((sign > 0) and ((MAX_INT - digit) // 10 < ans)):
                return MAX_INT
            if ((sign < 0) and ((MIN_INT + digit - 1) // 10 + 1 > ans)):
                return MIN_INT
            ans = ans * 10 + sign * int(str[i])
            i += 1
        return ans
