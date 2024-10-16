import math
from math import pi
from math import sqrt


absolute = -5.999
floor_test= 198.42

result1 =   math.fabs(absolute)
result2 = math.fabs(floor_test)
print(result1," is the abs valur of", absolute)
print (result2,"is the abs value of", floor_test)
  


  #file handlers
print("fries,chapo,drink : \n")




#json practise
import json
filename = 'userName.json'
name = ''

#check history of file\
try:
    with open(filename, 'r') as r:
        name =json.load(r)
except IOError:
    print("first-time login")     
# if the user was found in the history file ,welcome them back
if name !="":
    print("first-time login" + name +"!" )
else: 
    #if the user was not found in the file ask user fot the name
    name= input("hello what is your name?")
    print("welcomr, " + name +"!")
# Save the user's name to the history file
try:
    with open(filename, 'w') as f:
        json.dump(name, f)
except IOError:
    print("There was a problem writing to the history file.")
 #end of json practise