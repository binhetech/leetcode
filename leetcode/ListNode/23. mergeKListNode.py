#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : leetcode 
# @file : 23. mergeKListNode.py
# @Author : binhe
# @time : 2025/2/26 17:01
# @Software: PyCharm

"""
问题： 合并K个有序链表

代码逻辑的逐步解释
- 处理空输入:
    如果输入链表列表 lists 为空（len(lists) == 0），直接返回 None。
- 分治过程:
    merge 函数通过递归将输入链表列表分成左右两部分，直到每部分只剩下一个链表。
    每次递归调用将范围缩小，直到 left == right，此时直接返回该链表。
- 合并两个链表:
    mergeTwoList 使用一个虚拟头节点来构建合并后的链表。
    比较两个链表的当前节点值，将较小的节点连接到结果链表。
    如果一个链表的所有节点都已处理完毕，直接将另一个链表的剩余部分连接到结果链表。
代码的核心思想
- 分治法：将大问题分解为小问题，递归求解后合并结果。
- 归并排序思想：每次合并两个已排序的链表，直到所有链表合并完成。

时间和空间复杂度
- 时间复杂度：O(N log k)，其中 N 是所有链表中的总节点数，k 是链表的数量。
    每次合并两个链表的时间复杂度为 O(N)，分治法的递归层数为 O(log k)。
- 空间复杂度：O(log k)，主要来自于递归调用的栈空间。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        pass

    def merge_lists(self, lists):
        if not lists:
            return None
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, a, b):
        # 递归
        if a == b:
            return lists[a]
        c = a + (b - a) // 2
        sa = self.merge(lists, a, c)
        sb = self.merge(lists, c + 1, b)
        return self.merge_two(sa, sb)

    def merge_two(self, a, b):
        # 合并2个有序链表
        head = ListNode(0)
        h = head
        while a and b:
            if a.val >= b.val:
                # 从小到大排序
                h.next = b
                b = b.next
            else:
                h.next = a
                a = a.next
            h = h.next
        if a:
            h.next = a
        if b:
            h.next = b
        return head.next


# 构建链表1: 1 -> 4 -> 5
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

# 构建链表2: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# 构建链表3: 2 -> 6
list3 = ListNode(2)
list3.next = ListNode(6)

# 构建链表列表
lists = [list1, list2, list3]

# 测试代码
solution = Solution()
merged_list = solution.merge_lists(lists)

# 验证合并结果
result = []
current = merged_list
while current:
    result.append(current.val)
    current = current.next

# 输出验证结果
print(result)  # 应输出 [1, 1, 2, 3, 4, 4, 5, 6]
