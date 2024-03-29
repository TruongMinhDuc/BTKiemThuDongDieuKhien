import re

def passwordCheck(password):
   if(len(password) < 8 or len(password) > 30):
       return False
   if(not password.isalnum()):
       return False
   if not re.search("[A-Z]", password):
       return False
   return True

        
inputPassword = input()
if passwordCheck(inputPassword):
    print("Mat khau hop le")
else:
    print("Mat khau khong hop le")