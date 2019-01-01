#!/usr/bin/env python3

'''
	This is a shell program written in python
		By Catherine Wolfe - 2018/2019
'''

import sys, os, subprocess

sp = subprocess
state = 1

def main():
	os.chdir(os.environ['HOME'])
	cashLoop()

def cashLoop():
	while True:
		PS1 = " | " + os.getcwd() + " | > "
		sys.stdout.write(PS1)
		cashRead()
		if state != 1:
			cashExit()

def cashRead():
	evalIn = input()
	eval = evalIn.split(' ')

	if eval[0] == "cd":
		cashCD(eval)
	elif eval[0] == "help":
		print("It's a shell, There aren't many features yet.")
		pass
	elif eval[0] == "exit":
		cashExit()
	else:
		sp.call(eval)

def cashCD(eval):
	currentDir = os.getcwd()

	if len(eval) < 2:
		os.chdir(os.environ['HOME'])
	elif eval[1] == "~":
		os.chdir(os.environ['HOME'])
	elif eval[1] == " ":
		pass
	elif len(eval) > 1 and list(eval[1])[0] == "/":
		 os.chdir(eval[1])
	else:
		os.chdir(currentDir + "/" + eval[1])

def cashExit():
	exit()

main()
