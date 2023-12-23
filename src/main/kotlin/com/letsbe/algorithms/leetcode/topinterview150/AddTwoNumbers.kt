package com.letsbe.algorithms.leetcode.topinterview150

/**
 * https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150
 */
class AddTwoNumbers {
	fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
		var carry = 0
		var l1 = l1
		var l2 = l2
		val dummyHead = ListNode(0)
		var p = dummyHead
		while (l1 != null || l2 != null || carry != 0) {
			val sum = (l1?.`val` ?: 0) + (l2?.`val` ?: 0) + carry
			carry = sum / 10
			p.next = ListNode(sum % 10)
			p = p.next!!
			l1 = l1?.next
			l2 = l2?.next
		}
		return dummyHead.next
	}

	class ListNode(var `val`: Int) {
		var next: ListNode? = null
	}
}

fun main() {
	val l1 = AddTwoNumbers.ListNode(2)
	l1.next = AddTwoNumbers.ListNode(4)
	l1.next!!.next = AddTwoNumbers.ListNode(3)

	val l2 = AddTwoNumbers.ListNode(5)
	l2.next = AddTwoNumbers.ListNode(6)
	l2.next!!.next = AddTwoNumbers.ListNode(4)

	val result = AddTwoNumbers().addTwoNumbers(l1, l2)
	println("${result?.`val`} ${result?.next?.`val`} ${result?.next?.next?.`val`}")
}
