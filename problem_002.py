#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Yi Cao <ycao@astro.caltech.edu>
#
# Distributed under terms of the GNU General Public License 3.0 license.

"""
Add Two Numbers
URL: https://leetcode.com/problems/add-two-numbers/
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        carry = 0
        l = None
        while not (carry == 0 and node1 is None and node2 is None):
            if node1 is None:
                val1 = 0
            else:
                val1 = node1.val
            if node2 is None:
                val2 = 0
            else:
                val2 = node2.val
            val = val1 + val2 + carry
            node = ListNode(val % 10)
            node.next = l
            l = node
            carry = val // 10
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
        return l
