#!/usr/bin/python
# -*- coding: utf-8 -*-
#Coded by Spades

import md5
import hashlib
import os
import time

def main_menu():
	print """\033[0;97m
██╗  ██╗ █████╗ ███████╗██╗  ██╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
███████║███████║███████╗███████║██║     ██████╔╝███████║██║     █████╔╝\033[0;92m
██╔══██║██╔══██║╚════██║██╔══██║██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
██║  ██║██║  ██║███████║██║  ██║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗\033[0;97m
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
========================================================================\033[0;92m
1.MD5 HASH CRACKER
2.SHA1 HASH CRACKER (not working yet)
3.SHA512 HASH CRACKER (not working yet)
------------------------------------------------------------------------
________________________________________________________________________
"""
	kek = raw_input("Enter A Choice:")
	
	if kek == "1":
		main()
	elif kek == "2":
		crack()
def main():
	moo = raw_input("\033[0;92mENTER A HASH:")
	pwfile = raw_input("\033[0;92mENTER A FILE NAME:")

	try:
		pwfile = open(pwfile, "r")

	except:
		print "\033[0;91mPASSWORD FILE NOT FOUND"
	
	for password in pwfile: 
		filemd5 = md5.new(password.strip()).hexdigest()
		print "\033[0;92mTRYING PASSWORD: %s" % (password.strip()) + "\n"
	
		if moo == filemd5:
			print "\033[0;92m\n MATCH FOUND. \n CRACKED PASSWORD HASH IS:\033[0;97m %s" % password
			break
		else:
			print "\033[0;91m\n PASSWORD NOT FOUND \n"

def crack():
	milk = raw_input("\033[0;92mENTER A HASH:")
	passfile = raw_input("\033[0;92mENTER A FILE NAME:")
	
	try:
		passfile = open(passfile, "r")
			
	except:
		print "\033[0;91mPASSWORD FILE NOT FOUND"
		
	for passsha1 in passfile:
		filesha1 = hashlib.sha1(passsha1.strip()).hexdigest()
		print "\033[0;92mTRYING PASSWORD: %s" % (passsha1.strip()) + "\n"
			
		if milk == filesha1:
			print "\033[0;92m\n MATCH FOUND. \n CRACKED PASSWORD HASH IS:\033[0;97m %s" % passsha1
			break
		else:
			print "\033[0;91m\n PASSWORD NOT FOUND \n"

os.system('clear')
main_menu()