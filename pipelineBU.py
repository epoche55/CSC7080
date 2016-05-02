import re
import pickle
import string

dataforwarding = 0

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
		line = line.replace('[', '')
		line = line.replace(']', '')
		register = int(line.split('=', 1)[0])
		value = int(line.split('=', 1)[1])
		M[register] = value
	
	instruction = line.split()
	print instruction

	return instruction

def ALU(instex, number):
	temp = 0
	arg1 = 0
	if len(instex) > 0:

		if (instex[0] == "ADD"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3].split('R', 1)[1])

			R[arg1] = R[arg2] + R[arg3]
			# temp = R[arg2] + R[arg3]
			dataforwarding = temp
		elif (instex[0] == "ADDI"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3])
			# temp = R[arg2] + arg3
			R[arg1] = R[arg2] + arg3

		elif (instex[0] == "SUB"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3].split('R', 1)[1])

			temp = R[arg2] - R[arg3]
			M[arg1] = R[arg2] - R[arg3]
		elif (instex[0] == "SUBI"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3])
			# temp = R[arg2] - arg3
			
			R[arg1] = R[arg2] - arg3
			
		elif (instex[0] == "MUL"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3].split('R', 1)[1])

			# temp = R[arg2] * R[arg3]
			R[arg1] = R[arg2] * R[arg3]
		elif (instex[0] == "MULI"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3])
			# temp = R[arg2] * arg3
			R[arg1] = R[arg2] * arg3
		elif (instex[0] == "DIV"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3].split('R', 1)[1])

			# temp = R[arg2] / R[arg3]
			R[arg1] = R[arg2] / R[arg3]
		elif (instex[0] == "DIVI"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3])
			# temp = R[arg2] / arg3
			R[arg1] = R[arg2] / arg3
		elif (instex[0] == "AND"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3].split('R', 1)[1])

			# temp = R[arg2] and R[arg3]
			R[arg1] = R[arg2] and R[arg3]
		elif (instex[0] == "ANDI"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3])
			# temp = R[arg2] and arg3
			R[arg1] = R[arg2] and arg3
		elif (instex[0] == "OR"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3].split('R', 1)[1])

			# temp = R[arg2] or R[arg3]
			R[arg1] = R[arg2] or R[arg3]
		elif (instex[0] == "ORI"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3])

			# temp = R[arg2] or arg3
			R[arg1] = R[arg2] or arg3
		elif (instex[0] == "NOT"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])

			# temp = ~R[arg2] 
			R[arg1] = ~R[arg2] 
		elif (instex[0] == "NOTI"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2])

			# temp = ~arg2
			R[arg1] = ~arg2
		elif (instex[0] == "LD"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])

			# temp =M[R[arg2]]  
			R[arg1] = M[R[arg2]] 
		elif (instex[0] == "LDI"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3])

			# temp = M[R[arg2]+arg3]
			R[arg1] = M[R[arg2]+arg3]
		elif (instex[0] == "ST"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])

			# temp = R[arg1]
			M[R[arg2]] = R[arg1]
		elif (instex[0] == "STI"):
			arg1 = int(instex[1].split('R', 1)[1])
			arg2 = int(instex[2].split('R', 1)[1])
			arg3 = int(instex[3])

			# temp = R[arg1]
			M[R[arg2] + arg3] = R[arg1]
		elif (instex[0] == "BRZ"):
			arg1 = int(instex[1].split('R', 1)[1])
			if R[arg1] == 0:
				number = funcLine
		elif (instex[0] == "BRNZ"):
			arg1 = int(instex[1].split('R', 1)[1])
			if R[arg1] != 0: 
				number = funcLine
				# print R[arg1]
		elif (instex[0] == "BRG"):
			arg1 = int(instex[1].split('R', 1)[1])
			if R[arg1] > 0: 
				number = int(instex[2])
		elif (instex[0] == "BRL"):
			arg1 = int(instex[1].split('R', 1)[1])
			if R[arg1] < 0: 
				number = int(instex[2])
		elif (instex[0] == "JMP"):
			number = int(instex[1])
		elif (instex[0] == "PRINT"):
			print instex[1:]


	return (temp, arg1, number)

def MEM(result, regnum):
	# R[regnum] = result
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

print newCode



number = 0
while number < len(newCode)-1:
	line = IF(newCode, number)
	inst = DE(line, funcLine)
	aluResult, regResult, number1 = ALU(inst, number)
	MEM(aluResult, regResult)
	if number1 != number:
		number = number1
	else:
		number += 1






# for line in newCode:
# for number in range(0, len(newCode)-1):
# 	print number
# 	line = IF(newCode, number)
# 	inst = DE(line, funcLine)
# 	aluResult, regResult = ALU(inst)
# 	MEM(aluResult, regResult)
# 	number += 1

# start pipeline
# number = 0
# newCode[number] = IF(newCode, number)

# number += 1
# newCode[number] = IF(newCode, number)
# inst = DE(newCode[number-1], funcLine)

# number += 1
# newCode[number] = IF(newCode, number)
# inst = DE(newCode[number-1], funcLine)
# aluResult, regResult = ALU(inst)

# number += 1
# newCode[number] = IF(newCode, number)
# inst = DE(newCode[number-1], funcLine)
# aluResult, regResult = ALU(inst)
# MEM(aluResult, regResult)

 
# for x in range(number, len(newCode)-1):
# 	newCode[x] = IF(newCode, x)
# 	inst = DE(newCode[x-1], funcLine)
# 	aluResult, regResult = ALU(inst)
# 	MEM(aluResult, regResult)

# 	number += 1

print R
print M
