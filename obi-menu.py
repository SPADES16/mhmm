#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
import hashlib
import time

def main_menu():
	print("""\033[0;91m

 ██████╗ ██████╗ ██╗
██╔═══██╗██╔══██╗██║
██║   ██║██████╔╝██║\033[0;92m
██║   ██║██╔══██╗██║
╚██████╔╝██████╔╝██║
 ╚═════╝ ╚═════╝ ╚═╝\033[0;92m
                    

===================================================\033[0;91m
(1).INTRODUCTION
(2).HASHER
(3).BTC CHECKER
(4).IPTOOLS/DOX TEMPLATE
(5).HASH CRACKER\033[0;92m
==================================================\033[0;91m
""")
	choice = input("Pick one of the above:")
	
	if choice == "1":
		os.system("python3 Introduction.py")
	if choice == "2":
		os.system("python hashgen.py")
	if choice == "3":
		os.system("python3 Btcchecker.py")
	if choice == "4":
		os.system("python error.py")
	if choice == "5":
		os.system("python test.py")
	else:
		print ("error 1: acception unavailable, choice chosen was incorrect.")

os.system("clear")
main_menu()
