from time import sleep
from utils import *

def beamSearch(cipherList, N=10000):
	bestSoFarHistories = [None for _ in range(N)]
	bestSoFarHistories[0] = []
	bestSoFarVals = [None] * N
	bestSoFarVals[0] = 0.0

	for i in range(len(cipherList)):
		newBestSoFarHistories = [None for _ in range(N)]
		newBestSoFarVals = [float('inf')] * N
		for n in range(N):
			history = bestSoFarHistories[n]
			if history is not None:
				choices = getAllChoices(history, cipherList)
				for c in choices:
					newObjVal = objFunc(history, c, cipherList) + bestSoFarVals[n]
					if newObjVal < max(newBestSoFarVals):
						idx = newBestSoFarVals.index(max(newBestSoFarVals))
						newBestSoFarVals[idx] = newObjVal
						newBestSoFarHistories[idx] = list(history) + [c]
		bestSoFarHistories = newBestSoFarHistories
		bestSoFarVals = newBestSoFarVals
		print(i, min(bestSoFarVals), sum([el==float('inf') for el in bestSoFarVals]) / N)
		print("".join([cipherList[h] for h in bestSoFarHistories[bestSoFarVals.index(min(bestSoFarVals))]]))
	bestIdx = bestSoFarVals.index(min(bestSoFarVals))

	return bestSoFarVals[bestIdx], bestSoFarHistories[bestIdx]


if __name__ == '__main__':
	alphabet = "abcdefghiklmnopqrstuvxyz"
	di = {}
	for l in alphabet:
		di[l] = letter2num(l)
	print(di)
	#text_ = "facioliberosexliberislibrislibraque"
	text_ = "facileprinceps"
	CIPHER = []
	while len(text_) > 0:
		l_ = text_[0]
		CIPHER = CIPHER + [l_ for _ in range(text_.count(l_))]
		text_ = text_.replace(l_, "")
	print("".join(CIPHER))
	print(beamSearch(CIPHER))
