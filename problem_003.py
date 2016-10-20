#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao@astro.caltech.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
Longest Substring Without Repeating
URL:
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup_table = {}
        max_length = 0
        curr_length = 0
        for i in range(len(s)):
            j = lookup_table.get(s[i])
            if j is None:
                lookup_table[s[i]] = i
                curr_length += 1
            else:
                max_length = max(curr_length, max_length)
                for k in range(i - curr_length, j + 1):
                    del lookup_table[s[k]]
                curr_length = i - j
        max_length = max(curr_length, max_length)
        return max_length
