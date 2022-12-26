import numpy as np
import operator
import sys
import os

def createDataSet(name):
	list = os.listdir(name)
	length = len(list)
	matrix = np.zeros((length, 1024))

	labels=[]
	for i in range(length):
		fileName = list[i]
		answer = int(fileName.split('_')[0])
		labels.append(answer)
		matrix[i, :] = changeList(name + '/' + fileName)
	return matrix, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}

	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

	sortedClassCount = sorted(classCount.items(),
		key = operator.itemgetter(1), reverse = True)
	
	return sortedClassCount[0][0]

def changeList(name):
	list = np.zeros((1, 1024))
	with open(name) as fp:
		for i in range(32):
			line = fp.readline()
			for j in range(32):
				list[0, 32 * i + j] = int(line[j])
		return list

trainingName = sys.argv[1]
testName = sys.argv[2]

matrix, labels = createDataSet(trainingName)

list = os.listdir(testName)
length = len(list)

for k in range(1, 21):
	fail = 0
	total = 0

	for i in range(length):
		test = int(list[i].split('_')[0])
		testData = changeList(testName + '/' + list[i])
		classify0Rslt = classify0(testData, matrix, labels, k)
		total += 1

		if test != classify0Rslt:
			fail += 1

	print(int(fail / total * 100)) 

