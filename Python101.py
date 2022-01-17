#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Hello World!
print("Hello World!")


# In[ ]:


#Creating Variables
myNumber = 10
myText = "Hello"


# In[ ]:


#Using Variables
print(myNumber)
print(myText)


# In[ ]:


#Typecasting
value = "10"
number = int(value)


# In[ ]:


#Arithmetic Operators
addition = 10+10
subtraction = 9-1
multiplication = 2*4
division = 10/2
modules = 10%8
exponent = 10**2
floorDivision = 10//6

print("Addition:", addition)
print("Subtraction:",subtraction)
print("Multiplication:",multiplication)
print("Division:",division)
print("Modules:",modules)
print("Exponent:",exponent)
print("Floor Division:",floorDivision)


# In[ ]:


#Assignment Operators
assign = 0
print(assign)
assign += 14
print(assign)
assign -= 7
print(assign)
assign *= 2
print(assign)
assign /= 2
print(assign)
assign %= 5
print(assign)
assign **= 5
print(assign)
assign //= 2.6
print(assign)


# In[ ]:


#Comparison Operators
print(20==10)
print(20==20)
print(20!=10)
print(20!=20)
print(20>10)
print(20>20)
print(20<10)
print(20<20)
print(20>=20)
print(20>=10)
print(20<=20)
print(20<=10)


# In[ ]:


#Logical Operators
print(True or True)
print(True or False)
print(False or False)
print(True and True)
print(False and False)
print(True and False)
print(not True)
print(not False)


# In[ ]:


#Input function
name = input ("Please enter your name")
areaCode = input ("Area Code")
phoneNumber = input ("Phone Number")

number = areaCode + phoneNumber

print("Name:",name)
print("Phone Number:",number)


# In[ ]:


#Typecast input function
number1 = input("Enter first number:")
number2 = input("Enter second number:")
number1 = int(number1)
number2 = int(number2)
sum = number1 + number2
print("Results:", sum)


# In[ ]:


#Conditions IF,ELIF,ELSE
import random

number = int (random.randrange(1,10))

if number < 7 :
    print ( "Your number is less than 7" )
elif number > 7 :
    print ( "Your number is greater than 7" )
else :
    print ( "Your number is 7" )
print(number)


# In[ ]:


#Nested IF statements
import random

number = int (random.randrange(1,10))

if number % 2 == 0:
    if number == 0:
        print("Your number is even but zero")
    else:
        print("Your number is even")
else:
    print("Your number is odd")


# In[ ]:


#Loops

print("-----[While Loop]-----")
#While
number=0

while number<10:
    number+=1
    print(number)
    
print("-----[Endless Loop]-----")
#Endless
#while True:
    #print ("This will print forever")

print("-----[For Loop]-----")
#For
numbers=[10,20,30,40]

for number in numbers:
    print(number)

    


# In[ ]:


#Range Function
for x in range(100):
    print(x)
    
for x in range (20,80):
    print(x)


# In[ ]:


#Break Statement
number=0

while number<10:
    number+=1
    if number==5:
        break
    print(number)


# In[ ]:


#Continue Statement
number=0

while number <10:
    number+=1
    if number==7:
        continue
    print(number)


# In[ ]:


#Pass Statement
if number==10:
    pass
else:
    pass

while number<10:
    pass


# In[ ]:


#lists
age=[34,23,7,5,1,33]
names=["Jack","Jill","Jon","Jane","Jim","Jub"]
mixed=["Jack",34,154.5,False]

print(age[0:2])
print(names[:6])
print(mixed[0:])

#Modifying Elements

names[0]="Jax"
mixed[0]="Jax"
mixed[3]=True


print(names[0:])
print(mixed[0:])


# In[ ]:


#List Operations
numbers=[0,1,2,3,4,5,6,7,8,9,10]+[100,101]
numbers1=[7,7,7]*3

print(numbers)
print(numbers1)

#List Functions
print("List:",numbers)
print("Length of list:",len(numbers))
print("Max value:",max(numbers))
print("Minumum Value",min(numbers))
#numbers(5)
numbers.append(777)
print("Appended element to list:",numbers)

print("Counts amount of times element appears:",numbers1.count(7))
print("Index at point element occurs",numbers.index(777),numbers)
print("Removed and returned last element:",numbers.pop())

numbers.reverse()
print("Reversed list:", numbers)

numbers.sort()
print("Sorted list:", numbers)


# In[ ]:


#Tuples (can't be modified)
tpl=(10,20,30)


# In[ ]:


#Dictionaries
dct={"Name":"Jax",
     "Age":34,
     "Height":6.1}

print(dct)
print(dct["Name"])

#Dictionary Functions
print("Length of dictionary:",len(dct))
print("Dictionary displayed as string:",str(dct))
print("Returned copy of dictionary:",dct.copy())
print("Returned new dictionary with same key but empty elements:",dct.fromkeys("EMPTY"))
print("Returned value of given key 'Name':",dct.get("Name"))
print("Returns only if dictionary has ceratin key 'Name':", dct.__contains__('Name'))
print("Returned dictionary items as tuples:",dct.items())
print("Returned list of all keys:",dct.keys())

dct2={"Wieght":155,
      "Blood type":"AB+"}
dct.update(dct2)
print("Added second dictionary to existing one:",dct)
print("Returned list of all values:", dct.values())
print("Cleared elements of dictionary:",dct.clear(),"|",dct2.clear())


# In[ ]:


#Memborship operators
lst1 = [10,20,30,40,50]

print(20 in lst1)
print(60 in lst1)
print(60 not in lst1)

for x in lst1:
    print(x)


# In[ ]:


#Defining functions
def hello():
    print("Hello")
    
hello()


# In[ ]:


#Parameters
def print_sum(nmbr1,nmbr2):
    print(nmbr1+nmbr2)
    
print_sum(20,3)


# In[ ]:


#Returning values
def add(nmbr1,nmbr2):
    return nmbr1+nmbr2

nmbr3=add(7,7)
print(nmbr3)


# In[ ]:


#Default parameters
def say(text="Default text"):
    print(text)
    
say('Howdy world')


# In[ ]:


#Variable parameters
def print_sum(*nmbrs):
    result=0   
    for x in nmbrs:
        result+=x
    print(result)
    
print_sum(10,20,30,40)


# In[ ]:


#Scopes

#Variable doesnt exist example
#def function():
#    nmbr=10
#    print(nmbr)
#    
#print(nmbr)

#---------------------
#Variable is global example
#number=10
#
#def function():
#    print(number)
#    
#function()

#----------------------

nmbr=10

def function():
    global nmbr
    nmbr+=10
    print(nmbr)
    
function()


# In[ ]:


#Exception Handling

#Try except
try:
    print(10/0)
except ZeroDivisionError:
    print("Code for divide by zero error...")
except:
    print("Code for other exceptions...")
    

try:
    text="Hello"
    number=int(text)
except ValueError:
    print("Code for ValueError...")
except:
    print("Code for other exceptions...")
    
#Else Statements
try:
    print(7/0)
except:
    print("!ERROR!")
else:
    print("VALID")
    
#Finally statements 
try:
    print(5/0)
except:
    print("!ERROR!")
finally:
    print("EXECUTED")


# In[ ]:


#File operations

#Opening and closing
file=open('myfile.txt','r')
print(file.read())
file.close()

#Opening using With closes stream afterwards
with open('myfile.txt','r')as file:
    print(file.read(5))

#Access modes
# r   | reading
# r+  | reading and writing (no truncating)
# rb  | reading binary
# rb+ | reading and writing binary (no truncating)
# w   | writing
# w+  | reading and writing (no truncating)
# wb  | writing binary
# wb+ | reading and writing binary file (no truncating)
# a   | appending
# a+  | reading and appending
# ab  | appending binary file
# ab+ | reading and appending binary file

#Writing into files
file=open('myfile.txt','w')
print(file.write('Howdy file!'))
file.flush()
file.close()

#Writing using With
with open('myfile.txt','w') as file:
    print(file.write("Hello file!"))
    
#Appending to file
with open('myfile.txt','a') as file:
    print(file.write('Append file!'))


# In[ ]:


#Importing modules
import os
from os import *

#Deleting and renaming
remove('myfile.txt')
#rename('myfile.txt','testfile.txt')

#Directory operations
#mkdir('newdir')
#rename('testfile.txt','newdir/myfile.txt')
#chdir('newdir')
#chdir('..')
#rmdir('newdir')


# In[ ]:


#String functions
#https://www.w3schools.com/python/python_ref_string.asp

#Sequences
text="Hello World!"
print(text[:5])
print(text[6:11])

for x in text:
    print(x)
    
#Escape characters
print(text,'\t',text,'\n',text )


# In[ ]:


#String formatting
name,age='Jon',25
print('%s is his name,'%name)
print('he is %d years old.'%age)

# %c    | characters
# %s    | string
# %d or %i  | integer
# %f    | float
# %e    | exponential notation

print('\n')

print('Their name is {} and are {} years old.'
      .format(name,age))


# In[ ]:


#Case manipulating functions
testStrng='Python is cool, with it you can do cool things!'

print('Normal:',testStrng)
print('Converted to lowercase:',testStrng.lower())
print('Converted to uppercase:',testStrng.upper())
print('Converted to titlecase:',testStrng.title())
print('Converted first letter to uppercase:',testStrng.capitalize())
print('Swapped case of all letters:',testStrng.swapcase())
#Count function
print('Using count function to check for word "cool":',testStrng.count('cool'))
#Find function
print('Using find function to find index for "do":',testStrng.find('do'))
#Replace function
print('Replace string "cool" with "awesome":',testStrng.replace('cool','awesome'))


# In[ ]:


#Join function
names=['Jax','Jon','Jen','Jub']
sep='-'
print('Names using the Join function:',sep.join(names))

#Split function
names1='Jax,Jon,Jen,Jib'
name_list=names1.split(',')
print('Name list with Split function:',name_list)


# In[ ]:


#Triple Quotes
print('''Hello World! We are using a multi-line comment!
Using "Triple Quotes"!
Python is WOW much cool!
No escape characters are needed in order to write a new empty line!''')


# In[ ]:




