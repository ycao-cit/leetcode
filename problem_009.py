#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao16@uw.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
Palindrome Number
URL: https://leetcode.com/problems/palindrome-number/
"""


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        i = 10
        j = 10
        while (x // j >= 10):
            j *= 10
        while (j >= i):
            if not (x % i == x // j):
                return False
            x = (x % j) // i
            j /= 100
        return True
