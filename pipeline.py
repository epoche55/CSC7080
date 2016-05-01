import re
import pickle
import string


def IF(newCode, num):
	return newCode[num]

def DE(line, lineNum):

	line = line.replace('\t', '')
	line = line.lstrip(' ') 

	if line[0] == 'R':
		line = line.replace('R', '')
		register = int(line.split('=', 1)[0])
		value = line.split('=', 1)[1]
		R[register] = value
	elif (line[0] == 'M') and (line[1] != 'U'):
		line = line.replace('M', '')
		register = int(line.split('=', 1)[0])
		value = line.split('=', 1)[1]
		M[register] = value
	elif(line[0] == 'A') and (line[1] == 'D') and (line[2] == 'D') and (line[3] == 'I')
	elif(line[0] == 'A') and (line[1] == 'D') and (line[2] == 'D')




	# for x in xrange(len(line)):
	# 	if line[x] == 'R':
	# 		field1 = line[x:x+1]
	# 		print field1

	return line

def ALU():
	return 0

def MEM():
	return 0


def WB():
	return 0


code = [line for line in open('test2.txt')]

R = [None]*100
M = [None]*100
function = []
newCode = []

for string in code:
	rest = string.split('//', 1)[0]
	newCode.append(rest)

newCode = filter(None, newCode)

lineNum = 0
for line in newCode:
	for char in line:
	    if ':' == char:
	    	former = line.split(':', 1)[0]
	    	funcLine = lineNum
	        rest = line.split(':', 1)[1]
	        newCode[lineNum] = rest
	lineNum += 1

# print newCode

number = 0
for line in newCode:
	line = IF(newCode, number)
	line = DE(line, funcLine)
	print line

	number += 1

print R
print M
