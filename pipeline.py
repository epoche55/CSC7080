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
		value = int(line.split('=', 1)[1])
		R[register] = value
	elif (line[0] == 'M') and (line[1] != 'U'):
		line = line.replace('M', '')
		register = int(line.split('=', 1)[0])
		value = int(line.split('=', 1)[1])
		M[register] = value
	
	instruction = line.split()
	print instruction






	# for x in xrange(len(line)):
	# 	if line[x] == 'R':
	# 		field1 = line[x:x+1]
	# 		print field1

	return instruction

def ALU(instex):
	if (instex[0] == "ADD"):

		arg1 = int(instex[1].split('R', 1)[1])
		arg2 = int(instex[2].split('R', 1)[1])
		arg3 = int(instex[3].split('R', 1)[1])

		print arg1 , arg2 , arg3

		R[arg1] = R[arg2] + R[arg3]

		# if instruction[1][0] == 'R':
		# 	arg1 = instruction[1].split('R', 1)[1]
		# else
		# 	arg1 = int(instruction[1])
		# if instruction[2][0] == 'R':
		# 	arg2 = instruction[2].split('R', 1)[1]
		# else
		# 	arg2 = int(instruction[2])
		# if instruction[3][0] == 'R':
		# 	arg3 = instruction[3].split('R', 1)[1]
		# else
		# 	arg3 = int(instruction[3])
		

		
		
	# elif (instruction[0] == "ADDI"):
	# elif (instruction[0] == "SUB"):
	# elif (instruction[0] == "SUBI"):
	# elif (instruction[0] == "MUL"):
	# elif (instruction[0] == "MULI"):
	# elif (instruction[0] == "DIV"):
	# elif (instruction[0] == "DIVI"):
	# elif (instruction[0] == "AND"):
	# elif (instruction[0] == "ANDI"):
	# elif (instruction[0] == "OR"):
	# elif (instruction[0] == "ORI"):
	# elif (instruction[0] == "NOT"):
	# elif (instruction[0] == "NOTI"):
	# elif (instruction[0] == "LD"):
	# elif (instruction[0] == "LDI"):
	# elif (instruction[0] == "ST"):
	# elif (instruction[0] == "STI"):
	# elif (instruction[0] == "BRZ"):
	# elif (instruction[0] == "BRNZ"):
	# elif (instruction[0] == "BRG"):
	# elif (instruction[0] == "BRL"):
	# elif (instruction[0] == "JMP"):
	# elif (instruction[0] == "PRINT"):


	return 0

def MEM():
	return 0


def WB():
	return 0


code = [line for line in open('test2.txt')]

R = [None]*100
R[0] = 0
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
	inst = DE(line, funcLine)
	ALU(inst)
	number += 1

print R
print M
