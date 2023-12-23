package com.letsbe.algorithms.leetcode.topinterview150

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class AddTwoNumbersTest {
	@Test
	fun addTwoNumbers() {
		val l1 = AddTwoNumbers.ListNode(2).apply {
			next = AddTwoNumbers.ListNode(4).apply {
				next = AddTwoNumbers.ListNode(3)
			}
		}

		val l2 = AddTwoNumbers.ListNode(5).apply {
			next = AddTwoNumbers.ListNode(6).apply {
				next = AddTwoNumbers.ListNode(4)
			}
		}

		val result = AddTwoNumbers().addTwoNumbers(l1, l2)

		assertEquals(7, result?.`val`)
		assertEquals(0, result?.next?.`val`)
		assertEquals(8, result?.next?.next?.`val`)
	}
}
