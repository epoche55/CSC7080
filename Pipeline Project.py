import re
import pickle
import string



def IF(newCode, num):
	## check if last line is reached
	if num >= len(newCode):
		return "NONE"
	return newCode[num]

def DE(instex, lineNum):
	# parse instructions
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

	#split instruction into list	
	instruction = instex.split()

	code = 0
	arg1 = 0
	arg2 = 0
	arg3 = 0
	
	if len(instruction) > 0:
		if (instruction[0] == "ADD"):		
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])
			
			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			if Rflag[arg3] == 1:
				print "RAW for R[%d]" % arg3

			# R[arg1] = R[arg2] + R[arg3]
			# temp = R[arg2] + R[arg3]
			# dataforwarding = temp
			code = 1
		elif (instruction[0] == "ADDI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			# temp = R[arg2] + arg3
			# R[arg1] = R[arg2] + arg3
			code = 2
		elif (instruction[0] == "SUB"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			if Rflag[arg3] == 1:
				print "RAW for R[%d]" % arg3
			# temp = R[arg2] - R[arg3]
			# M[arg1] = R[arg2] - R[arg3]
			code = 3
		elif (instruction[0] == "SUBI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			# temp = R[arg2] - arg3
			
			# R[arg1] = R[arg2] - arg3
			code = 4
		elif (instruction[0] == "MUL"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			if Rflag[arg3] == 1:
				print "RAW for R[%d]" % arg3
			# temp = R[arg2] * R[arg3]
			# R[arg1] = R[arg2] * R[arg3]
			code = 5
		elif (instruction[0] == "MULI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			# temp = R[arg2] * arg3
			# R[arg1] = R[arg2] * arg3
			code = 6
		elif (instruction[0] == "DIV"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			if Rflag[arg3] == 1:
				print "RAW for R[%d]" % arg3
			# temp = R[arg2] / R[arg3]
			# R[arg1] = R[arg2] / R[arg3]
			code = 7
		elif (instruction[0] == "DIVI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			# temp = R[arg2] / arg3
			# R[arg1] = R[arg2] / arg3
			code = 8
		elif (instruction[0] == "AND"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			if Rflag[arg3] == 1:
				print "RAW for R[%d]" % arg3
			# temp = R[arg2] and R[arg3]
			# R[arg1] = R[arg2] and R[arg3]
			code = 9
		elif (instruction[0] == "ANDI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			# temp = R[arg2] and arg3
			# R[arg1] = R[arg2] and arg3
			code = 10
		elif (instruction[0] == "OR"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			if Rflag[arg3] == 1:
				print "RAW for R[%d]" % arg3
			# temp = R[arg2] or R[arg3]
			# R[arg1] = R[arg2] or R[arg3]
			code = 11
		elif (instruction[0] == "ORI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2

			# temp = R[arg2] or arg3
			# R[arg1] = R[arg2] or arg3
			code = 12
		elif (instruction[0] == "NOT"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			# temp = ~R[arg2] 
			# R[arg1] = ~R[arg2] 
			code = 13
		elif (instruction[0] == "NOTI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1

			# temp = ~arg2
			# R[arg1] = ~arg2
			code = 14
		elif (instruction[0] == "LD"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2

			# temp =M[R[arg2]]  
			# R[arg1] = M[R[arg2]] 
			code = 15
		elif (instruction[0] == "LDI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			if Rflag[arg1] == 1:
				print "WAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2

			# temp = M[R[arg2]+arg3]
			# R[arg1] = M[R[arg2]+arg3]
			code = 16
		elif (instruction[0] == "ST"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "RAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2

			# temp = R[arg1]
			# M[R[arg2]] = R[arg1]
			code = 17
		elif (instruction[0] == "STI"):
			arg1 = int(instruction[1].split('R', 1)[1])
			arg2 = int(instruction[2].split('R', 1)[1])
			arg3 = int(instruction[3])

			if Rflag[arg1] == 1:
				print "RAW for R[%d]" % arg1
			if Rflag[arg2] == 1:
				print "RAW for R[%d]" % arg2
			# temp = R[arg1]
			# M[R[arg2] + arg3] = R[arg1]
			code = 18
		elif (instruction[0] == "BRZ"):
			arg1 = int(instruction[1].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "RAW for R[%d]" % arg1
			###arg2 = int(instruction[2])
			# if R[arg1] == 0:
			# 	number = funcLine
			code = 19
		elif (instruction[0] == "BRNZ"):
			arg1 = int(instruction[1].split('R', 1)[1])

			if Rflag[arg1] == 1:
				print "RAW for R[%d]" % arg1
			###arg2 = int(instruction[2])
			# if R[arg1] != 0: 
			# 	number = funcLine
			code = 20 
		elif (instruction[0] == "BRG"):
			arg1 = int(instruction[1].split('R', 1)[1])
			if Rflag[arg1] == 1:
				print "RAW for R[%d]" % arg1
			####arg2 = int(instruction[2])
			# if R[arg1] > 0: 
			# 	number = int(instruction[2])
			code = 21
		elif (instruction[0] == "BRL"):
			arg1 = int(instruction[1].split('R', 1)[1])
			if Rflag[arg1] == 1:
				print "RAW for R[%d]" % arg1
			####arg2 = int(instruction[2])
			# if R[arg1] < 0: 
			# 	number = int(instruction[2])
			code = 22
		elif (instruction[0] == "JMP"):
			arg1 = int(instruction[1])
			if Rflag[arg1] == 1:
				print "RAW for R[%d]" % arg1
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

	if (code >= 1 and code <= 16):	
		Rflag[arg1] = 1
		# print "Rflag = %s" % Rflag

	return (code, arg1, arg2, arg3)

def ALU(opcode, arg1, arg2, arg3, number, dataforwarding):
	temp = 0
	result = 0
	if (opcode == 1):	# ADD
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding + R[arg3]
		elif Rflag[arg3] == 1:
			print "ALU RAW for R[%d]" % arg3
			result =  R[arg2] + dataforwarding
		else:
			result = R[arg2] + R[arg3]
		# R[arg1] = R[arg2] + R[arg3]
		dataforwarding = result
	elif (opcode == 2):		# ADDI
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding + R[arg3]
		else:
			result = R[arg2] + arg3
		dataforwarding = result
		# R[arg1] = R[arg2] + arg3
	elif (opcode == 3):	# SUB
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding - R[arg3]
		elif Rflag[arg3] == 1:
			print "ALU RAW for R[%d]" % arg3
			result =  R[arg2] - dataforwarding
		else:
			result = R[arg2] - R[arg3]
		dataforwarding = result
		# M[arg1] = R[arg2] - R[arg3]
	elif (opcode == 4): # SUBI
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding - R[arg3]
		else:
			result = R[arg2] - arg3
		dataforwarding = result
		# R[arg1] = R[arg2] - arg3
	elif (opcode == 5):		# MUL
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding * R[arg3]
		elif Rflag[arg3] == 1:
			print "ALU RAW for R[%d]" % arg3
			result =  R[arg2] * dataforwarding
		else:
			result = R[arg2] * R[arg3]
		dataforwarding = result
		# R[arg1] = R[arg2] * R[arg3]
	elif (opcode == 6):		# MULI
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding * R[arg3]
		else:
			result = R[arg2] * arg3
		dataforwarding = result
		# R[arg1] = R[arg2] * arg3
	elif (opcode == 7):		# DIV
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding / R[arg3]
		elif Rflag[arg3] == 1:
			print "ALU RAW for R[%d]" % arg3
			result =  R[arg2] / dataforwarding
		else:
			result = R[arg2] / R[arg3]
		dataforwarding = result
		# R[arg1] = R[arg2] / R[arg3]
	elif (opcode == 8): 	#DIVI
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding / R[arg3]
		else:
			result = R[arg2] / arg3
		dataforwarding = result
		# R[arg1] = R[arg2] / arg3
	elif (opcode == 9):		# AND
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding and R[arg3]
		elif Rflag[arg3] == 1:
			print "ALU RAW for R[%d]" % arg3
			result =  R[arg2] and dataforwarding
		else:
			result = R[arg2] and R[arg3]
		dataforwarding = result
		# R[arg1] = R[arg2] and R[arg3]
	elif (opcode == 10):		# ANDI
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding and R[arg3]
		else:
			result = R[arg2] and arg3
		dataforwarding = result
		# R[arg1] = R[arg2] and arg3
	elif (opcode == 11):	# OR
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding or R[arg3]
		elif Rflag[arg3] == 1:
			print "ALU RAW for R[%d]" % arg3
			result =  R[arg2] or dataforwarding
		else:
			result = R[arg2] or R[arg3]
		dataforwarding = result
		# R[arg1] = R[arg2] or R[arg3]
	elif (opcode == 12):		# ORI
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = dataforwarding or R[arg3]
		else:
			result = R[arg2] or arg3
		dataforwarding = result
		# R[arg1] = R[arg2] or arg3
	elif (opcode == 13):		# NOT
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = ~dataforwarding
		else:
			result = ~R[arg2] 
		dataforwarding = result
		# R[arg1] = ~R[arg2] 
	elif (opcode == 14):		# NOTI
		result = ~arg2
		dataforwarding = result
		# R[arg1] = ~arg2
	elif (opcode == 15):		# LD
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = M[R[dataforwarding]]
		else:
			result =M[R[arg2]]  
		dataforwarding = result
		# R[arg1] = M[R[arg2]] 
	elif (opcode == 16):		# LDI
		if Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			result = M[R[dataforwarding]+arg3]
		else:
			result = M[R[arg2]+arg3]
		dataforwarding = result
		# R[arg1] = M[R[arg2]+arg3]
	elif (opcode == 17):	# ST
		
		if Rflag[arg1] == 1:
			print "ALU RAW for R[%d]" % arg1
			M[R[arg2]] = R[dataforwarding]
		elif Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			M[R[dataforwarding]] = R[arg1]
		else:
			M[R[arg2]] = R[arg1]
		# result = R[arg1]
	elif (opcode == 18):	# STI
		if Rflag[arg1] == 1:
			print "ALU RAW for R[%d]" % arg1
			M[R[arg2] + arg3] = R[dataforwarding]
		elif Rflag[arg2] == 1:
			print "ALU RAW for R[%d]" % arg2
			M[R[dataforwarding] + arg3] = R[arg1]
		else:
			M[R[arg2] + arg3] = R[arg1]
		# result = R[arg1]
	elif (opcode == 19):		# BRZ
		if Rflag[arg1] == 1:
			if R[dataforwarding] == 0:
				number = funcLine
		else:
			if R[arg1] == 0:
				number = funcLine
			# result = funcLine
	elif (opcode == 20):		# BRNZ
		if Rflag[arg1] == 1:
			if R[dataforwarding] != 0:
				number = funcLine
		else:
			if R[arg1] != 0:
				number = funcLine
			# result = funcLine
	elif (opcode == 21):		# BRG
		if Rflag[arg1] == 1:
			if R[dataforwarding] > 0:
				number = funcLine
		else:
			if R[arg1] > 0:
				number = funcLine
			# result = funcLine
	elif (opcode == 22):		# BRL
		if Rflag[arg1] == 1:
			if R[dataforwarding] < 0:
				number = funcLine
		else:
			if R[arg1] < 0:
				number = funcLine
			# result = funcLine
	elif (opcode == 23):		# JMP
		if Rflag[arg1] == 1:
			number = dataforwarding
		else:
			number = arg1
		# result = arg1
	print "R = %s" % R
	return (opcode, arg1, arg2, arg3, result, number, dataforwarding)

def MEM(opcode, arg1, arg2, arg3, result):
	# write to registers

	if (opcode >= 1 and opcode <= 16):	
		R[arg1] = result
		dataforwarding = result
		Rflag[arg1] = 0	
		# print "Rflag = %s" % Rflag
	return (opcode, arg1, arg2, arg3, result)

def WB(opcode, arg1, arg2, arg3, result):
	# write to memory
	if (opcode == 17):	# ST
		M[R[arg2]] = result
	elif (opcode == 18):	# STI
		M[R[arg2] + arg3] = result
	return 0


code = [line for line in open('test2.txt')]

dataforwarding = 0
R = [None]*100
R[0] = 0
M = [None]*100
Rflag = [None]*100
Mflag = [None]*100
for i in xrange(0, len(Rflag)):
    Rflag[i] = 0
    Mflag[i] = 0
    R[i] = 0
    M[i] = 0

function = []
newCode = []

print "R = %s" % R
print "M = %s" % M

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
ALUdf = dataforwarding

#begin pipeline
# 1
line = IF(newCode, number)
number += 1
clock += 1
print "clock = %d" % clock

# 2
line2 = IF(newCode, number)
DEop, DEarg1, DEarg2, DEarg3 = DE(line, funcLine)
number += 1
clock += 1
print "clock = %d" % clock

# 3
line3 = IF(newCode, number)
DEop2, DEarg12, DEarg22, DEarg32 = DE(line2, funcLine)
ALUop, ALUarg1, ALUarg2, ALUarg3, ALUresult2, numJump, ALUdf2 = ALU(DEop, DEarg1, DEarg2, DEarg3, number, ALUdf)
clock += 1
if numJump != number:
	number = numJump
else:
	number += 1
print "clock = %d" % clock

# 4
line = IF(newCode, number)
DEop3, DEarg13, DEarg23, DEarg33 = DE(line3, funcLine)
ALUop1, ALUarg11, ALUarg21, ALUarg31, ALUresult21, numJump, ALUdf3 = ALU(DEop2, DEarg12, DEarg22, DEarg32, number, ALUdf2)
MEMop, MEMarg1, MEMarg2, MEMarg3, MEMresult = MEM(ALUop, ALUarg1, ALUarg2, ALUarg3, ALUresult2)
clock += 1
if numJump != number:
	number = numJump
else:
	number += 1
print "clock = %d" % clock

while number < len(newCode)-1:
	# 1
	line1 = IF(newCode, number)
	DEop1, DEarg11, DEarg21, DEarg31 = DE(line, funcLine)
	ALUop, ALUarg1, ALUarg2, ALUarg3, ALUresult, numJump, ALUdf4 = ALU(DEop3, DEarg13, DEarg23, DEarg33, number, ALUdf3)
	MEMop2, MEMarg12, MEMarg22, MEMarg32, MEMresult2 = MEM(ALUop1, ALUarg11, ALUarg21, ALUarg31, ALUresult21)
	WB(MEMop, MEMarg1, MEMarg2, MEMarg3, MEMresult)
	clock += 1
	if numJump != number:
		number = numJump
	else:
		number += 1
	print "clock = %d" % clock	

	# 2
	line2 = IF(newCode, number)
	DEop2, DEarg12, DEarg22, DEarg32 = DE(line1, funcLine)
	ALUop2, ALUarg12, ALUarg22, ALUarg32, ALUresult2, numJump, ALUdf5 = ALU(DEop1, DEarg11, DEarg21, DEarg31, number, ALUdf4)
	MEMop3, MEMarg13, MEMarg23, MEMarg33, MEMresult3 = MEM(ALUop, ALUarg1, ALUarg2, ALUarg3, ALUresult)
	WB(MEMop2, MEMarg12, MEMarg22, MEMarg32, MEMresult2)
	clock += 1
	if numJump != number:
		number = numJump
	else:
		number += 1
	print "clock = %d" % clock

	# 3
	line3 = IF(newCode, number)
	DEop3, DEarg13, DEarg23, DEarg33 = DE(line2, funcLine)
	ALUop3, ALUarg13, ALUarg23, ALUarg33, ALUresult3, numJump, ALUdf6 = ALU(DEop2, DEarg12, DEarg22, DEarg32, number, ALUdf5)
	MEMop4, MEMarg14, MEMarg24, MEMarg34, MEMresult4 = MEM(ALUop2, ALUarg12, ALUarg22, ALUarg32, ALUresult2)
	WB(MEMop3, MEMarg13, MEMarg23, MEMarg33, MEMresult3)
	clock += 1
	if numJump != number:
		number = numJump
	else:
		number += 1
	print "clock = %d" % clock

	# 4
	line4 = IF(newCode, number)
	DEop4, DEarg14, DEarg24, DEarg34 = DE(line3, funcLine)
	ALUop4, ALUarg14, ALUarg24, ALUarg34, ALUresult4, numJump, ALUdf7 = ALU(DEop3, DEarg13, DEarg23, DEarg33, number, ALUdf6)
	MEMop5, MEMarg15, MEMarg25, MEMarg35, MEMresult5 = MEM(ALUop3, ALUarg13, ALUarg23, ALUarg33, ALUresult3)
	WB(MEMop4, MEMarg14, MEMarg24, MEMarg34, MEMresult4)
	clock += 1
	if numJump != number:
		number = numJump
	else:
		number += 1
	print "clock = %d" % clock
	
	# 5
	line = IF(newCode, number)
	opcode3, arg13, arg23, arg33 = DE(line4, funcLine)
	op2, inst12, inst22, inst32, result2, numJump, ALUdf3 = ALU(DEop4, DEarg14, DEarg24, DEarg34, number, ALUdf7)
	MEMop2, MEMarg12, MEMarg22, MEMarg32, MEMresult2 = MEM(ALUop4, ALUarg14, ALUarg24, ALUarg34, ALUresult4)
	WB(MEMop5, MEMarg15, MEMarg25, MEMarg35, MEMresult5)
	clock += 1
	if numJump != number:
		number = numJump
	else:
		number += 1
	print "clock = %d" % clock

print 
print "R = %s" % R
print "M = %s" % M
