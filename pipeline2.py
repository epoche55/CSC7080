import re
import pickle
import string

dataforwarding = 0

def IF(newCode, num):
	return newCode[num]

def DE(instex, lineNum):

	instex = instex.replace('\t', '')
	instex = instex.lstrip(' ') 

	if instex[0] == 'R':
		instex = instex.replace('R', '')
		register = int(instex.split('=', 1)[0])
		value = int(instex.split('=', 1)[1])
		R[register] = value
	elif (instex[0] == 'M') and (instex[1] != 'U'):
		instex = instex.replace('M', '')
		instex = instex.replace('[', '')
		instex = instex.replace(']', '')
		register = int(instex.split('=', 1)[0])
		value = int(instex.split('=', 1)[1])
		M[register] = value
	
	instruction = instex.split()
	# print instruction
	code = 0
	arg1 = 0
	arg2 = 0
	arg3 = 0
#### new stuff
	if len(instruction) > 0:
		if (instruction[0] == "ADD"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])
			print "adding"
			# R[arg1] = R[arg2] + R[arg3]
			# temp = R[arg2] + R[arg3]
			# dataforwarding = temp
			code = 1
		elif (instruction[0] == "ADDI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])
			# temp = R[arg2] + arg3
			# R[arg1] = R[arg2] + arg3
			code = 2
		elif (instruction[0] == "SUB"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			# temp = R[arg2] - R[arg3]
			# M[arg1] = R[arg2] - R[arg3]
			code = 3
		elif (instruction[0] == "SUBI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])
			# temp = R[arg2] - arg3
			
			# R[arg1] = R[arg2] - arg3
			code = 4
		elif (instruction[0] == "MUL"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			# temp = R[arg2] * R[arg3]
			# R[arg1] = R[arg2] * R[arg3]
			code = 5
		elif (instruction[0] == "MULI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])
			# temp = R[arg2] * arg3
			# R[arg1] = R[arg2] * arg3
			code = 6
		elif (instruction[0] == "DIV"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			# temp = R[arg2] / R[arg3]
			# R[arg1] = R[arg2] / R[arg3]
			code = 7
		elif (instruction[0] == "DIVI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])
			# temp = R[arg2] / arg3
			# R[arg1] = R[arg2] / arg3
			code = 8
		elif (instruction[0] == "AND"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			# temp = R[arg2] and R[arg3]
			# R[arg1] = R[arg2] and R[arg3]
			code = 9
		elif (instruction[0] == "ANDI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])
			# temp = R[arg2] and arg3
			# R[arg1] = R[arg2] and arg3
			code = 10
		elif (instruction[0] == "OR"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			# temp = R[arg2] or R[arg3]
			# R[arg1] = R[arg2] or R[arg3]
			code = 11
		elif (instruction[0] == "ORI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			# temp = R[arg2] or arg3
			# R[arg1] = R[arg2] or arg3
			code = 12
		elif (instruction[0] == "NOT"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])

			# temp = ~R[arg2] 
			# R[arg1] = ~R[arg2] 
			code = 13
		elif (instruction[0] == "NOTI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2])

			# temp = ~arg2
			# R[arg1] = ~arg2
			code = 14
		elif (instruction[0] == "LD"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])

			# temp =M[R[arg2]]  
			# R[arg1] = M[R[arg2]] 
			code = 15
		elif (instruction[0] == "LDI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			# temp = M[R[arg2]+arg3]
			# R[arg1] = M[R[arg2]+arg3]
			code = 16
		elif (instruction[0] == "ST"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			# temp = R[arg1]
			# M[R[arg2]] = R[arg1]
			code = 17
		elif (instruction[0] == "STI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])
			# temp = R[arg1]
			# M[R[arg2] + arg3] = R[arg1]
			code = 18
		elif (instruction[0] == "BRZ"):
			arg1 = int(instruction[1].split('R', 1)[1])
			###arg2 = int(instruction[2])
			# if R[arg1] == 0:
			# 	number = funcLine
			code = 19
		elif (instruction[0] == "BRNZ"):
			arg1 = int(instruction[1].split('R', 1)[1])
			###arg2 = int(instruction[2])
			# if R[arg1] != 0: 
			# 	number = funcLine
			code = 20 
		elif (instruction[0] == "BRG"):
			arg1 = int(instruction[1].split('R', 1)[1])
			####arg2 = int(instruction[2])
			# if R[arg1] > 0: 
			# 	number = int(instruction[2])
			code = 21
		elif (instruction[0] == "BRL"):
			arg1 = int(instruction[1].split('R', 1)[1])
			####arg2 = int(instruction[2])
			# if R[arg1] < 0: 
			# 	number = int(instruction[2])
			code = 22
		elif (instruction[0] == "JMP"):
			arg1 = int(instruction[1])
			# number = int(instruction[1])
			code = 23
		elif (instruction[0] == "PRINT"):
			print "\nPRINT"
			if '-' in instruction[1]:
				str1 = instruction[1].split('-', 1)[0]
				str2 = instruction[1].split('-', 1)[1]
				if str1.startswith("R"):
					arg1 = int(str1.split('R', 1)[1])
					arg2 = int(str2.split('R', 1)[1])
					i=0
					for i in xrange(arg1, arg2+1):
						print "R[%d] : %d" % (i, R[i])
				else:
					arg1 = int(str1.split('M', 1)[1])
					arg2 = int(str2.split('M', 1)[1])
					i=0
					for i in xrange(arg1, arg2+1):
						print "M[%d] : %d" % (i, M[i])
			elif instruction[1].startswith("R"):
				arg1 = int(instruction[1].split('R', 1)[1])
				print "R[%d] : %d" % (arg1, R[arg1])
			elif instruction[1].startswith("M"):
				arg1 = int(instruction[1].split('M', 1)[1])
				print "M[%d] : %d" % (arg1, M[arg1])
			code = 24



#########3
	return (code, arg1, arg2, arg3)

def ALU(opcode, arg1, arg2, arg3, number):
	temp = 0
	result = 0
	if (opcode == 1):	# ADD
		# R[arg1] = R[arg2] + R[arg3]
		result = R[arg2] + R[arg3]
		dataforwarding = result
	elif (opcode == 2):		# ADDI
		result = R[arg2] + arg3
		# R[arg1] = R[arg2] + arg3
	elif (opcode == 3):	# SUB
		result = R[arg2] - R[arg3]
		# M[arg1] = R[arg2] - R[arg3]
	elif (opcode == 4): # SUBI
		result = R[arg2] - arg3
		# R[arg1] = R[arg2] - arg3
	elif (opcode == 5):		# MUL
		result = R[arg2] * R[arg3]
		# R[arg1] = R[arg2] * R[arg3]
	elif (opcode == 6):		# MULI
		result = R[arg2] * arg3
		# R[arg1] = R[arg2] * arg3
	elif (opcode == 7):		# DIV
		result = R[arg2] / R[arg3]
		# R[arg1] = R[arg2] / R[arg3]
	elif (opcode == 8): 	#DIVI
		result = R[arg2] / arg3
		# R[arg1] = R[arg2] / arg3
	elif (opcode == 9):		# AND
		result = R[arg2] and R[arg3]
		# R[arg1] = R[arg2] and R[arg3]
	elif (opcode == 10):		# ANDI
		result = R[arg2] and arg3
		# R[arg1] = R[arg2] and arg3
	elif (opcode == 11):	# OR
		result = R[arg2] or R[arg3]
		# R[arg1] = R[arg2] or R[arg3]
	elif (opcode == 12):		# ORI
		result = R[arg2] or arg3
		# R[arg1] = R[arg2] or arg3
	elif (opcode == 13):		# NOT
		result = ~R[arg2] 
		# R[arg1] = ~R[arg2] 
	elif (opcode == 14):		# NOTI
		result = ~arg2
		# R[arg1] = ~arg2
	elif (opcode == 15):		# LD
		result =M[R[arg2]]  
		# R[arg1] = M[R[arg2]] 
	elif (opcode == 16):		# LDI
		result = M[R[arg2]+arg3]
		# R[arg1] = M[R[arg2]+arg3]
	elif (opcode == 17):	# ST
		# result = R[arg1]
		M[R[arg2]] = R[arg1]
	elif (opcode == 18):	# STI
		# result = R[arg1]
		M[R[arg2] + arg3] = R[arg1]
	elif (opcode == 19):		# BRZ
		if R[arg1] == 0:
			number = funcLine
			# result = funcLine
	elif (opcode == 20):		# BRNZ
		if R[arg1] != 0: 
			number = funcLine
			# result = funcLine
	elif (opcode == 21):		# BRG
		if R[arg1] > 0: 
			number = funcLine
			# result = funcLine
	elif (opcode == 22):		# BRL
		if R[arg1] < 0: 
			number = funcLine
			# result = funcLine
	elif (opcode == 23):		# JMP
		number = arg1
		# result = arg1

	return (opcode, arg1, arg2, arg3, result, number)

def MEM(opcode, arg1, arg2, arg3, result):
	# write to registers

	if (opcode >= 1 and opcode <= 16):	
		R[arg1] = result
		dataforwarding = result
	return 0

def WB(opcode, arg1, arg2, arg3, result):
	# write to memory
	if (opcode == 17):	# ST
		M[R[arg2]] = result
	elif (opcode == 18):	# STI
		M[R[arg2] + arg3] = result

	return 0


code = [line for line in open('test2.txt')]

R = [None]*100
R[0] = 0
M = [None]*100
function = []
newCode = []


print "R"
print R
print "M"
print M

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

number = 0
clock = 0
while number < len(newCode)-1:
	print "clock: %d" % (clock)
	line = IF(newCode, number)
	print "code: %s" % line
	opcode, arg1, arg2, arg3 = DE(line, funcLine)
	opcode, arg1, arg2, arg3, result, numJump = ALU(opcode, arg1, arg2, arg3, number)


	MEM(opcode, arg1, arg2, arg3, result)
	WB(opcode, arg1, arg2, arg3, result)
	if numJump != number:
		number = numJump
	else:
		number += 1

	clock += 1

print 
print "R"
print R
print "M"
print M

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

