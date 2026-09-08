# if and else operator

import getpass

username = "JAMES"
password = "ROSARIO"

Iusername = input("Input your username:  ")
Ipassword = getpass.getpass("Input your password:  ")

if Iusername == username:
     if Ipassword == password:
       print("access granted")
else:
       print("Invalid")