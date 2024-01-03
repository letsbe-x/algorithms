import unittest

"""
https://github.com/xissy/coderpad-interviews/tree/master/p77
Problem 77 [Easy]
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

스냅챗에서 출제된 문제입니다.

중첩될 수 있는 인터벌들을 갖는 리스트가 있습니다. 중첩되는 인터벌들을 하나로 합친 새로운 리스트를 반환하세요.

입력 리스트는 정렬되어 있지 않습니다.

예를 들어, [(1, 3), (5, 8), (4, 10), (20, 25)] 가 주어지면, [(1, 3), (4, 10), (20, 25)] 를 반환해야 합니다.
"""

"""
	O(nlogn) time complexity
	O(n) space complexity
"""
def solution(intervals):

	intervals.sort(key=lambda x: x[0])
	merged_intervals = []

	for interval in intervals:
		if not merged_intervals or merged_intervals[-1][1] < interval[0]:
			merged_intervals.append(interval)
		else:
			merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))

	return merged_intervals

class TestCase(unittest.TestCase):
	"""
	For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
	"""
	def test_solution(self):
		intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
		expected = [(1, 3), (4, 10), (20, 25)]
		self.assertEqual(expected, solution(intervals))

	"""
	For example, given [(20, 25), (4, 10), (5, 8), (1, 3)], you should return [(1, 3), (4, 10), (20, 25)].
	"""
	def test_solution2(self):
		intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
		intervals.reverse()
		expected = [(1, 3), (4, 10), (20, 25)]
		self.assertEqual(expected, solution(intervals))
