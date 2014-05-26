#! /usr/bin/python
import sys
last_word =""
labelset=set()
for line in sys.stdin:
	word,labels_in= line.strip().split()
	if last_word=="":
		last_word = word
	if last_word!=word:
		labelstr = ""
		for label in labelset:
			labelstr+=str(label)+","
		print last_word+"\t"+labelstr.strip(",")
		labelset.clear()
		last_word = word
	labels = labels_in.split(",")
	for label in labels:
		if int(label) not in labelset:
			labelset.add(int(label))
	
labelstr = ""
for label in labelset:
	labelstr+=str(label)+","
print last_word+"\t"+labelstr.strip(",")
labelset.clear()
