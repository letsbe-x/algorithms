import unittest

"""
https://school.programmers.co.kr/learn/courses/20847/lessons/255900?language=python3
[PCCP 모의고사 #1] 1번 - 외톨이 알파벳
"""
def solution(input_string):
	alphabet_cnt_dict = {}
	for idx, ch in enumerate(input_string):
		if ch not in alphabet_cnt_dict:
			alphabet_cnt_dict[ch] = [1, [idx]]
		else:
			alphabet_cnt_dict[ch][0] += 1
			alphabet_cnt_dict[ch][1].append(idx)

	# print(alphabet_cnt_dict)
	loner_alphabet_list = []

	for ch in alphabet_cnt_dict:
		count, idx_list = alphabet_cnt_dict[ch]
		if count > 1:
			if not all(idx_list[idx] + 1 == idx_list[idx + 1] for idx in range(len(idx_list) - 1)):
				loner_alphabet_list.append(ch)

	# print(loner_alphabet_list)
	answer = "".join(sorted(loner_alphabet_list)) if loner_alphabet_list else "N"
	return answer

class LonerAlphabetTestCase(unittest.TestCase):
	"""
	input_string	result
	"edeaaabbccd"	"de"
	"eeddee"	"e"
	"string"	"N"
	"zbzbz"	"bz"
	"""
	def test_something(self):
		self.assertEqual("de", solution("edeaaabbccd"))
		self.assertEqual("e", solution("eeddee"))
		self.assertEqual("N", solution("string"))
		self.assertEqual("bz", solution("zbzbz"))
