#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao16@uw.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
Regular Expression Matching
URL: https://leetcode.com/problems/regular-expression-matching/
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.match_helper(s, p, 0, 0)

    def simplify(self, p):
        if len(p) <= 1:
            return p
        ans = p[:2]
        i = 2
        while (i < len(p)):
            if (i + 1 < len(p) and p[i + 1] == "*" and
               p[i - 1] == "*" and p[i] == p[i - 2]):
                i += 2
            else:
                ans += p[i]
                i += 1

    def match_helper(self, s, p, i, j):
        if i == len(s) and j == len(p):
            return True
        if i < len(s) or j == len(p):
            return False
        if p[j] == ".":
            any_letter = True
        else:
            any_letter = False
        if j + 1 < len(p) and p[j + 1] == "*":
            any_length = True
        else:
            any_length = False
        if not any_length:
            if (i < len(s)) and (any_letter or s[i] == p[j]):
                return self.match_helper(s, p, i + 1, j + 1)
            else:
                return False
        else:
            if self.match_helper(s, p, i, j + 2):
                return True
            while (i < len(s) and (any_letter or s[i] == p[j])):
                if self.match_helper(s, p, i + 1, j + 2):
                    return True
                i += 1
            return False
