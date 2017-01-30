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
        l1_len = self.listNodeLength(l1)
        l2_len = self.listNodeLength(l2)
        if l1_len > l2_len:
            long_list = l1
            short_list = l2
        else:
            long_list = l2
            short_list = l1
        for i in range(abs(l1_len - l2_len)):
            zero_node = ListNode(0)
            zero_node.next = short_list
            short_list = zero_node
        l, carry = self._addTwoNumber(short_list, long_list)
        if carry > 0:
            node = ListNode(carry)
            node.next = l
            l = node
        return l

    def _addTwoNumber(self, l1, l2):
        if l1 is None and l2 is None:
            return None, 0
        l, carry = self._addTwoNumber(l1.next, l2.next)
        val = carry + l1.val + l2.val
        carry = val // 10
        node = ListNode(carry % 10)
        node.next = l
        return node, carry

    def listNodeLength(self, l):
        node = l
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length
