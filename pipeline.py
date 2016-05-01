import re
import pickle
import string


def IF(newCode):
	return newCode

def DE(line, lineNum):


	return 0

def ALU():
	return 0

def MEM():
	return 0


def WB():
	return 0


code = [line for line in open('test2.txt')]

R = []
M = []
function = []
newCode = []

for string in code:
	rest = string.split('//', 1)[0]
	newCode.append(rest)


lineNum = 0
for line in newCode:
	for char in line:
	    if ':' == char:
	    	former = line.split(':', 1)[0]
	    	funcLine = lineNum
	        rest = line.split(':', 1)[1]
	        newCode[lineNum] = rest
	lineNum += 1

print newCode

for line in newCode:
	line = IF(line)
	instruction = DE(line, funcLine)
