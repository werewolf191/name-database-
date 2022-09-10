from replit import db
#makes def so i can add or call data later 
def name_dec():
  
 print ("hi waht is your name ")
 name = input ()
 print ("tell me more about you? ")
 dec = input ()
 db[name] = dec


def name_call():
  print("is the name of the person you want call")
  name_call = input ()
  name_see  = db[name_call]
  print(name_call + ": " + name_see) 

#lets yo call your add data later 
#make the code repet as long as you need it 
n =  1
while n == n :
 print("type add to add some one or type call to find some one")
 data_do = input ()
 # sees if is you want to call or add data now 
 if data_do == "add":
  name_dec()
 elif data_do == "call":
  name_call()
 else:
  print ("sory we can't do that")