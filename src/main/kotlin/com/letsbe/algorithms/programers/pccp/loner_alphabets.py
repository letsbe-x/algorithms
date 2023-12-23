import unittest
from collections import Counter, defaultdict

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

	for ch, (count, idx_list) in alphabet_cnt_dict.items():
		if count > 1:
			if not all(idx_list[idx] + 1 == idx_list[idx + 1] for idx in range(len(idx_list) - 1)):
				loner_alphabet_list.append(ch)

	# print(loner_alphabet_list)
	answer = "".join(sorted(loner_alphabet_list)) if loner_alphabet_list else "N"
	return answer

def solution2(input_string):
	char_counts = Counter(input_string)
	loner_alphabets = []

	for char, count in char_counts.items():
		if count > 1:
			positions = defaultdict(list)
			for idx, ch in enumerate(input_string):
				positions[ch].append(idx)

			if not all(positions[char][idx] + 1 == positions[char][idx + 1] for idx in range(len(positions[char]) - 1)):
				loner_alphabets.append(char)

	return "".join(sorted(loner_alphabets)) if loner_alphabets else "N"


class TestCase(unittest.TestCase):
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

	def test_something2(self):
		self.assertEqual("de", solution2("edeaaabbccd"))
		self.assertEqual("e", solution2("eeddee"))
		self.assertEqual("N", solution2("string"))
		self.assertEqual("bz", solution2("zbzbz"))
