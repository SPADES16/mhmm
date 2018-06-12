#CODED BY SPADES#
import os
import hashlib
import time

def menu():
	print"""           )          (        )                  ) \033[0;91m        
        ( /(   (      )\ )  ( /(  (            ( /(         
        )\())  )\    (()/(  )\()) )\ )    (    )\())        
  __   ((_)\((((_)(   /(_))((_)\ (()/(    )\  ((_)\    __   
 / / _  _((_))\ _ )\ (_))   _((_) /(_))_ ((_)  _((_) _ \ \  
| | (_)| || |(_)_\(_)/ __| | || |(_)) __|| __|| \| |(_) | | \033[0;97m
| |  _ | __ | / _ \  \__ \ | __ |  | (_ || _| | .` | _  | | 
 \_\(_)|_||_|/_/ \_\ |___/ |_||_|   \___||___||_|\_|(_)/_/  
 ==========================================================\033[0;91m 
<===================TYPE 1 FOR MD5=========================>
<===================TYPE 2 FOR SHA1========================>
<===================TYPE 3 FOR SHA512======================>\033[0;97m
<==========================================================>
"""

	Name = raw_input("ENTER CHOICE:")
	if Name == "1":
		def hashing_method(passwd_hash):
			hash1 = hashlib.md5(passwd_hash)
			print "\033[0;97mYOUR HASHED PASSWORD IS:\033[0;91m ",hash1.hexdigest()
			
		def main():
			print "THIS SCRIPT WILL HASH PASSWORD USING MD5"
			passwd_hash = raw_input("ENTER PASSWORD TO HASH:\033[0;91m ")
			hashing_method(passwd_hash)
			
		if __name__ == '__main__':
			   main()
	elif Name == "2":
		def hashing_method(passwd_hash):
			hash2 = hashlib.sha1(passwd_hash)
			print "\033[0;97mYOUR HASHED PASSWORD IS:\033[0;91m ",hash2.hexdigest()
			
		def main():
			print "THIS SCRIPT WILL HASH PASSWORD USING SHA1"
			passwd_hash = raw_input("ENTER PASSWORD TO HASH:\033[0;91m ")
			hashing_method(passwd_hash)
			
		if __name__ == '__main__':
			   main()
			   
	elif Name == "3":
		def hashing_method(passwd_hash):
			hash3 = hashlib.sha512(passwd_hash)
			print "\033[0;97mYOUR HASHED PASSWORD IS:\033[0;91m ",hash3.hexdigest()
			
		def main():
			print "THIS SCRIPT WILL HASH PASSWORD USING SHA512"
			passwd_hash = raw_input("ENTER PASSWORD TO HASH:\033[0;91m ")
			hashing_method(passwd_hash)
			
		if __name__ == '__main__':
			   main()
			   
os.system('cls')
menu()

while True:
	time.sleep(8)
	os.system('cls')
	menu()
  