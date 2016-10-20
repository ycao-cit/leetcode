#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao16@uw.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
Longest Palindromic Substring
URL: https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        index_start = 0
        index_end = 1
        for i in range(len(s)):
            if i > 0:
                idx1, idx2 = self.helper(s, i, i)
                if idx2 - idx1 > index_end - index_start:
                    index_start = idx1
                    index_end = idx2
            if i < len(s) - 1:
                idx1, idx2 = self.helper(s, i, i + 1)
                if idx2 - idx1 > index_end - index_start:
                    index_start = idx1
                    index_end = idx2
        return s[index_start:index_end]

    def helper(self, s, i, j):
        while (i >= 0) and (j <= len(s) - 1) and (s[i] == s[j]):
            i -= 1
            j += 1
        return i + 1, j
