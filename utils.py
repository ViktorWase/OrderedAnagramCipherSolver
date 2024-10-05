from math import log

from LATIN_FREQS import LAT_4_NO_JW

SUM = sum(LAT_4_NO_JW)
LAT_4_NO_JW = [el / SUM for el in LAT_4_NO_JW]


def getAllChoices(history, cipherList):
	# TODO: Behöver den här tester?
	choices = []
	
	if len(history) == len(cipherList):
		return choices		
	assert len(history) < len(cipherList)

	if len(history) == 0:
		choices.append(0)
		return choices

	for i in range(len(history) - 1):
		if history[i] + 1 not in history and history[i] + 1 < len(cipherList) - 1:
			# print("Adding A", history[i]+1)
			choices.append(history[i] + 1)

	if max(history) < len(cipherList) - 1:
		if  max(history)+1 not in choices:
			# print("Adding B", max(history)+1)
			choices.append(max(history) + 1)

		i = max(history) + 1
		if cipherList[max(history)] == cipherList[i]:
			while i < len(cipherList) - 1:
				if cipherList[max(history)] != cipherList[i]:
					# print("Adding C", i)
					choices.append(i)
					break
				i += 1

	# assert max(choices) <= len(cipherList) - 1
	return choices


def letter2num(l):
	di = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'k': 9, 'l': 10, 'm': 11, 'n': 12, 'o': 13, 'p': 14, 'q': 15, 'r': 16, 's': 17, 't': 18, 'u': 19, 'v': 20, 'x': 21, 'y': 22, 'z': 23}
	return di[l]
	l = l.lower()
	alphabet = "abcdefghiklmnopqrstuvxyz"
	alphabet = [x for x in alphabet]
	#print(l)
	assert l in alphabet

	return alphabet.index(l)


def objFunc(history, newIdx, cipherList):
	if len(history) < 3:
		return 0.0

	N = 24
	stat_idx = letter2num(cipherList[history[-3]]) + \
	letter2num(cipherList[history[-2]]) * N + \
	letter2num(cipherList[history[-1]]) * N * N +\
	letter2num(cipherList[newIdx]) * N * N * N
	stat = LAT_4_NO_JW[stat_idx]
	if stat == 0:
		return 1000000  # float('inf')
	return -log(stat)
