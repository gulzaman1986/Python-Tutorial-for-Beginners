#!/usr/bin/env python
# coding: utf-8

# the character’s which is to be perceive as an identifiers python does not allow some character’s like @, $, and % within identifiers. you see at the bottom syntaxError

# In[32]:


print("Hellow Word1")


# In[1]:


val2@ = 35 


# import is a keyword which is used to import modules, library or a framework into code, you see that if we are trying to used keyword as an identifiers we got a syntaxError 

# In[2]:


import=900


# before "myvariable" you see a number (1) when we run the cell it's give SyntaxError, so what we understand,we understand that we can not use an indentifer proceeds by any number

# In[3]:


1myvariable= 200


# In[5]:


a = 100

if a == 100:
    print ('a is equal to = 100') # correct indentation


# if we not indented the code properly then we get "IndentationError"

# In[6]:


a = 100
if a == 100:
print ('a is equal to = 100')


# In[7]:


for a in range(0,8): print(a)
# this type indentation work but not help in the readibility of code


# In[22]:


my_variable_name = 200
# here we assign through equal operator (=) value 200, the name of the variable is my_variable_name


# In[23]:


id(my_variable_name)  
# here we want to retrive the identity (id) of our variable, identity is an object which have propertie
##always be an interger
## Guranteed to be unique
## will always be constant for the same object during its lifetime, in the output cell you see id


# In[24]:


hex(id(my_variable_name))
# here we want to get the hexadecimal memory address of a variable


# In[25]:


bin(id(my_variable_name))# the binary address of the memory in the output cell


# In[26]:


oct(id(my_variable_name))# the octal address of the memory in the output cell


# In[27]:


decimal(id(my_variable_name))


# In[29]:


int = 30 # Integer variable
float = 2.57 # Float Variable
str = "My EBooks library" # String variable
print(int)
print(float)
print(str)


# In[31]:


int,float,str  = 2.57,30,"My EBooks library"

print(int)  # Here you see we separate multiple variables through comma, one thing which is more  
print(float) # important is we assign the values to the variable regardless there sequence
print(str) # i mean at first position we take integer type if we assign the interger value at 
           # 2rd (that is  30) number it will also work 


# In[4]:


#function abc()
int max(inta, intb)
int return
int a =10
int b = 20
return = max(a,b)
print("the max value is:"."return")


# number variables

# In[6]:


var_first = 10
var_second = 20


# In[10]:


hex(id(var_second)) # you see we retrive the exadecimal memory addres for variable "var_second"


# In[11]:


del var_second # You can also delete the reference to a number object by using the del statement


# In[12]:


print(var_second) # at both cases you will get Error after Delete, 
#this mean delete command delete refereence to the memory of a variable


# In[13]:


hex(id(var_second))


# In[16]:


import sys
var1 = 10 # Integer data type
print(var1)
print(type(var1)) # type of object
print(sys.getsizeof(var1)) # size of integer object in bytes
print(var1, " is Integer?", isinstance(var1, int)) # var1 is an instance of int 


# In[17]:


var2 = 88.78 # Float data type
print(var2)
print(type(var2)) # type of object
print(sys.getsizeof(var2)) # size of float object in bytes
print(var2, " is float?", isinstance(var2, float)) # Var2 is an instance of float


# In[18]:


var3 = 100 + 200j # Complex data type
print(var3)
print(type(var3)) # type of object
print(sys.getsizeof(var3)) # size of float object in bytes
print(var3, " is complex?", isinstance(var3, complex)) # var3 is an instance of complex data type


# In[1]:


print("Hello! I am print command")


# In[6]:


print("123 + 456")# you see by default print command accept every inside double quotes as a string


# # List
# a data structure which contain different data type items unlike array. The items of the list are separated by comma and enclosed within square brackets [ ]. The values present in the list can be access using the operation known as slice and the operator used for slicing is colon (:) like array list also have starting index ‘0’ and end at -1. Furthermore, arithmetic operators Plus (+) used for concatenation asterisk (*) use to multiply or repeat the items of the list. For example  

# In[5]:


list0 = [ 1,2,3,4,5,6,7,8,9,10 ]
# integer list


# In[6]:


list0


# In[7]:


list1 = ['sunday','monday','friday','satureday']
#string list


# In[8]:


list1


# In[9]:


list2= [ 1,2,3,4,5,6,7,8,9,10,'sunday','monday','friday','satureday' ]
#string and Integer list


# In[10]:


list2


# In[15]:


print (list2) # Prints complete list


# In[17]:


print (list2[0]) # Prints first element of the list


# In[18]:


print (list[1:3]) # Prints elements starting from 2nd till 3rd


# In[19]:


print (list[2:]) # Prints elements starting from 3rd element


# # List Slicing- 
# The values present in the list can be access using the operation known as slice and the operator used for slicing is colon (:) like array list also have starting index ‘0’ and end at -1.
# 

# In[42]:


lists_slice = [1,2,3,4,5,6,7,8,9,10]
lists_slice


# In[43]:


lists_slice[0:5] # list  all elements from index '0' to index '3' 


# In[44]:


lists_slice[2:7] # list all elements from index '2' to index '5'


# In[45]:


lists_slice[:3] # Return first three items


# In[46]:


lists_slice[-3:] # Return last three items


# In[47]:


lists_slice[-1] # Return last item of the list


# In[48]:


lists_slice[:] # Return whole list


# # Add , Remove & Change Items-
# for add an item to list in python we use function append () append function only add item at the end of the list, unlike append () function insert () function is use to insert item on which index you want take two arguments index and item name on that particular index. Remove () function is use to remove items form the list by specifying the items name itself furthermore this function remove items from anywhere from the lists.
# Pop () function is used to remove items from anywhere of the list but the difference between pop () and remove () is pop remove item by specifying the index while remove () function remove items by specifying items name from the list.
# 

# In[54]:


lists_slice1 = ['one','two','three','four','five','six','seven','eight','nine','ten']


# In[55]:


lists_slice1.append('15')


# In[56]:


lists_slice1


# In[58]:


lists_slice1.insert(6,'fifty')


# In[60]:


lists_slice1


# In[62]:


lists_slice1.remove('one') # Remove item "ONE"
lists_slice1


# In[64]:




lists_slice1.remove(3) 
lists_slice1 


# In[65]:


lists_slice1.pop(8) # Remove item at index location 8
lists_slice1


# # Python Dictionary- 
# Dictionary is another data structure in Python dictionary have two parameters that is key and values, in pandas in data structure of series we performed all the required operation through index and value, but in dictionary the naming convention is changed form index values into key and values. Dictionary are enclosed by curly braces ({}) and values can be assigned and accessed using square braces [] for example. 

# In[20]:


mydict = {'Day1':'Sunday','Day2':'Monday','Day3':'Thuseday'}


# In[21]:


print(mydict)


# In[23]:


print (mydict['Day1']) # Prints value for 'Day1' key


# In[32]:


mydict['Day3'] # Prints value for Day3 


# In[33]:


print (mydict) # Prints complete dictionary


# In[35]:


print (mydict.keys()) # Prints all the keys


# In[36]:


print (mydict.values()) # Prints all the values


# # String:
# is a combination of characters while enclosing string in quotes may single, double or triple quotes produce same result. 

# In[37]:


str1 = "HELLO PYTHON"
print(str1)


# In[38]:


mystr = 'Hello World' # Define string using single quotes
print(mystr)


# In[39]:


mystr = "Hello World" # Define string using double quotes
print(mystr)


# In[40]:


mystr = '''Hello
World ''' # Define string using triple quotes
print(mystr)


# In[41]:


mystr = """Hello
World""" # Define string using triple quotes
print(mystr)


# In[42]:


mystr = ('Python '
'For '
'Everyone')
print(mystr)


# In[44]:


mystr2 = 'Python '
mystr2 = mystr2*5
mystr2


# In[45]:


len(mystr2) # Length of string


# # String Indexing:
# string internally store in system memory in array form, during accessing the elements of a string we use indexes, index have two types forward (positive) index backward (negative)indexes, we can access the elements through both types let try to do so.

# In[46]:


mystr


# In[47]:


mystr[0]


# In[51]:


mystr


# In[50]:


mystr[len(mystr)-1]


# In[52]:


mystr[-1]


# In[53]:


mystr[0:7]


# # String concatenation:
# concatenation of string  in Python is differnet form other programming language noramlly we do concatenation through dot operator in other programming language but in python we do concatenation of string through arithematic operators for example if we concat ABC with XYZ then we use ABC + XZY= ABCXYZ 

# In[1]:


s1 = "Hello"
s2 = "Python!"
s3 = s1 + s2
print(s3)


# In[2]:


# Insert space between strings, in the code you see single time space in double quotes " " 
s1 = "Hello"
s2 = "Python!"
s3 = s1 + " " + s2
print(s3)


# # String Membership-
# membership of string mean that you check the presence of a particular string or substring in the statements, to do so in python we use In as an membership operator. on checking you will get a boolean result, if the string present you will get 'True' and if the string not exist then you will get 'False'. 

# In[5]:


stringmember = "Python for Every one"
print ('Every' in stringmember)


# In[6]:


stringmember = "Python for Every one"
print ('Hello' in stringmember)


# # String Partitioning-
# The partition() method searches for a specified string and splits the string into
# - The first element contains the part before the argument string.
# - The second element contains the argument string.
# - The third element contains the part after the argument string.
# 

# In[8]:


strpartition = "A Beginner Level Python Programming Tutorial and Book"
A = strpartition.partition("and")
print(A)


# In[ ]:


The rpartition() method searches for the last occurence of the specified string a
containing three elements.
- The first element contains the part before the argument string.
- The second element contains the argument string.
- The third element contains the part after the argument string.


# In[11]:


strpartition = "A Beginner Level Python Programming Tutorial and Book"
A = strpartition.rpartition("Book")
print(A)


# # String Functions
# 1. strip() -- Removes white space from begining & end
# 2. rstrip() -- Removes all whitespaces at the end of the string
# 3. lstrip()-- Removes all whitespaces at the begining of the string
# 4. strip('*') -- Removes all '*' characters from begining & end of the string
# 5. rstrip('*') -- Removes all '*' characters at the end of the string
# 6. lstrip('*') -- Removes all '*' characters at the begining of the string
# 7. lower() -- Return whole string in lowercase
# 8. upper() -- Return whole string in uppercase
# 9. replace("Heee" , "Hooo") -- Replace substring "Heee" with "Hooo"
# 10. replace(" " , "") -- Remove all whitespaces using replace function
# 11. count("one") -- Number of times substring "one" occurred in string.
# 12. count("two") -- Number of times substring "two" occurred in string.
# 13. startswith("one") -- Return boolean value True if string starts with "one"
# 14. endswith("three") -- Return boolean value True if string ends with "three"
# 15. mystr4.split() -- Split String into substrings

# In[12]:


strfunction = "If you read a book second or even a third time, things won’t improve much, according to research"


# In[13]:


strfunction


# In[14]:


strfunction.strip()


# In[15]:


strfunction.rstrip()


# In[16]:


strfunction.lstrip()


# In[20]:


strfunction = "*****If you read******* a book second or even a third time, things won’t improve much, according to research***"


# In[22]:


strfunction.rstrip('*')


# In[23]:


strfunction.lstrip('*')


# In[24]:


mystr = "This all changes if you read less and do more, and this is the ultimate goal of my book."
mystr


# In[25]:


mystr.lower()


# In[26]:


mystr.upper()


# In[29]:


mystr.replace("Th" , "Ah")


# In[30]:


mystr.replace(" " , "")


# In[31]:


mystr1 = "one two Three one two two three"
mystr1


# In[32]:


mystr1.count("one")


# In[33]:


mystr1.count("two")


# In[34]:


mystr1.startswith("one")


# In[35]:


mystr1.endswith("three")


# In[38]:


mystr2 = "This all changes if you read less and do more, and this is the ultimate goal of my book"
mystr2


# In[40]:


mylist = mystr2.split()


# In[41]:


mylist


# # Python - 
# Decision Making/ Conditional statements- decision making is anticipation of conditions set by the programmer furthermore the execution of the program take action according to the conditions. Conditional statements evaluate multiple expression and return a Boolean result in term of TRUE and FALSE. Following is the flow of execution diagram of decision making statements.

# In[10]:


myvar = 200
if (myvar == 200) : 
    print ("values of expression is 200")
    print ("value of expression is not detected!")


# # 1.	If else – 
# an if statement can be followed by an optional else statement, which execute when the Boolean expression is FALSE. If the condition tested true, something happened. If the condition tested false, nothing happened.

# In[19]:



if marks == 80:
    print ("Obtained A Garde.")
    if marks != 80:
        print('Not obtained A Grade.')


# in the above code we have two if statement one testing for Grade A and another testing for not Grade A
# the code works and disply accordingly but it's look like un-professional if the variable 'marks' is not assigned to 80 then of course it not 80. so there is no reason to test for not marks. so to overcome this logic we can represent this code is an professional way.

# In[21]:


if marks == 80:
    print ("Obtained A Garde.")
else:
    print('Not obtained A Grade.') 


# Finally, there's elif. It's short for else if. If no test has been successful yet,                indent
# an elif tries something else.
# 

# In[26]:


if mango == 'fresh':
    buy_it_on = 100
    elif mango_not_fresh == 'Buy it on low price':
        low_price = 10
        else:
            low-price = 0


# In[28]:


if donut_condition == "fresh":
    buy_score = 10
    elseif donut_price == "low":
        buy_score = 5
        else:
            buy_score = 0


# # Programming Error- 
# in the context of computer programming, the terms “bugs” and “errors” are often used interchangeably, but they actually have slightly different meanings.
# 
# Bug – a bug is a flaw in the code that causes it to behave unexpectedly or not as intended. Bugs can be caused by a variety of factors, such as coding mistakes, hardware or software issues, or user input.
# 
# 
# Error-
# an errors, on the other hand is a mistake made by the programmer that result in incorrect code. This could be due to a misunderstanding of the requirements, a typographical error, or a logical error.
# Analogy to better under the difference between error and bugs-  an analogy that can be used to explain the difference between bugs and errors is that of a chef preparing a meal.  If the chef accidentally adds too much salt to the dish, that would be an error- a mistake made by the chef that resulted in an incorrect dish. However, if the dish is spoiled because there was a fly in the kitchen that landed in the food, that would be a bug - an unexpected problem caused by an external factor.
# Here are some common types of programming errors:
# 
# 1.	Syntax errors- These occur when the programmer makes a mistake in the syntax of the programming language, such as forgetting a semicolon or using the wrong variable name.
# 2.	Logical error- These occur when the program runs without any syntax errors, but produce unexpected or incorrect result. This can happen when the programmer doesn’t correctly anticipate all the possible scenarios that might arise in the program.
# 3.	Runtime error- These occur when that program is running and encounters a problem that causes it to crash or stop functioning properly. This can be cause by variety of factors, such as memory allocation issue, input/output error, or division by zero errors.
# 

# In[1]:


This code is supposed to calculate the average of three numbers
# However, there's a logical error in it

num1 = 10
num2 = 20
num3 = 30

average = (num1 + num2 + num3) / 2   # There's a logical error here

print("The average is:", average)


# In[2]:


if x == 5
print ('x is equal to 5')


# In[3]:


a = 10
b = 0
c = a/b


# In[4]:


# Loop through a list of fruits and print each one
fruits = ["apple", "banana", "cherry", "durian"]

for fruit in fruits:
    print(fruit)


# In this example, the for loop iterates through the fruits list and assigns each value to the fruit variable. The print(fruit) statement is executed for each item in the list, printing each fruit to the console.

# In[5]:


# A while loop that prints the numbers 0 through 4

count = 0  # Initialize the counter variable

while count < 5:  # Loop while count is less than 5
    print(count)  # Print the current value of count
    count += 1   # Increment count by 1


# This code initializes a variable called count to 0, and then uses a while loop to repeatedly print the current value of count and increment it by 1, until count reaches 5.

# In[6]:


# Example of the continue and break statements in Python

# This loop will print out all the numbers from 1 to 10, except for 7
for i in range(1, 11):
    if i == 7:
        # If i equals 7, we skip this iteration and move on to the next one
        continue
    print(i)

# This loop will print out all the even numbers from 1 to 10, and then stop
for i in range(1, 11):
    if i % 2 == 1:
        # If i is odd, we skip this iteration and move on to the next one
        continue
    print(i)
    if i == 6:
        # If i equals 6, we break out of the loop completely
        break


# In the first loop, we use the continue statement to skip over the number 7 and move on to the next iteration of the loop. This means that the number 7 will not be printed, but all the other numbers from 1 to 10 will be.
# 
# In the second loop, we use the continue statement to skip over all the odd numbers and only print out the even numbers. We also use the break statement to exit the loop completely when we reach the number 6. This means that the loop will print out the numbers 2, 4, and 6, and then stop.

# # Function- 
# A function in Python is a block of organized and reusable code that performs a specific task.
# 
# Here's an example of a simple function in Python that takes two arguments and returns their sum:

# In[7]:


def add_numbers(x, y):
    return x + y


# In[ ]:


# To use this function, you can call it with two arguments and assign the result to a variable:


# In[8]:


result = add_numbers(3, 5)
print(result) # Output: 8


# In this example, the add_numbers() function takes two arguments x and y, adds them together with the + operator, and then returns the result using the return keyword. The function can be called with any two numerical values and will always return their sum.

# # Print and Return

# In[9]:


def multiply_numbers(x, y):
    result = x * y
    print(f"The product of {x} and {y} is {result}") # using print statement to show the output
    return result # using return statement to pass the value back to the calling function

# calling the function and storing the return value in a variable
product = multiply_numbers(5, 3)

# printing the return value
print(f"The return value is {product}")


# In this example, we define a function called multiply_numbers that takes two arguments x and y. Inside the function, we calculate the product of x and y and then use the print statement to display the output to the user. We also use the return statement to pass the value of the product back to the calling function.
# 
# When we call the function with the arguments 5 and 3, the print statement inside the function displays the output "The product of 5 and 3 is 15" to the user, and the return statement passes the value 15 back to the calling function. We then store the return value in a variable called product and use the print statement again to display the return value to the user, which in this case is "The return value is 15".

# Variables Scope- 
# Variables scope in Python refers to the region where a particular variable is accessible. Variable defined inside a function are considered local and can only be accessed within that function. Variables defined outside of any function are considered global and can be accessed from anywhere in the program. If there is a variable with the same name defined both locally and globally, the local variable takes precedence within the function.

# In[12]:


x = 10  # global variable

def myglob():
    y = 20  # local variable
    print("Inside myglob(): x =", x)  # accessing global variable
    print("Inside myglob(): y =", y)  # accessing local variable

myglob()
print("Outside myglob(): x =", x)  # accessing global variable
print("Outside myglob(): y =", y)  # will result in NameError, y is not defined outside of myglob()


# In this example, x is a global variable and is accessible inside the myglob() function, whereas y is a local variable and can only be accessed inside the myglob() function. When we call myglob(), it will print the values of x and y inside the function. When we try to print x and y outside the function, we can access x since it is a global variable, but we will get a NameError for y since it only exists inside the myglob() function.

# # Defalut arguments
# Default Argument- Default arguments in Python allow you to define a function with parameters that have a default value. When the function is called, if a value is not provided for that parameter, the default value is used.
#  Here is an example:
# 

# In[14]:


def greet(name="World"):
    print(f"Hello, {name}!")

greet()  # prints "Hello, World!"
greet("Alice")  # prints "Hello, Alice!"


# In this example, the greet function has a single parameter, name, which has a default value of "World". When the function is called without an argument, the default value is used. When it's called with an argument, that argument is used instead of the default value.

# In[2]:


import django
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world!")


# In[7]:


import pandas as pd
df = pd.read_excel('Excelfile.xlsx')


# In[8]:


df


# In[9]:


column = df['STATION']


# In[10]:


column


# In[11]:


filtered_df = df[df['TAVG'] > 10]


# In[12]:


filtered_df


# In[13]:


mean = df['TAVG'].mean()


# In[14]:


mean


# In[21]:


df.to_excel('Excelfile.xlsx', index=False)


# In[23]:


df


# In[24]:


import openpyxl


# In[25]:


# Create a workbook object
workbook = openpyxl.Workbook()


# In[26]:


# Select a worksheet
worksheet = workbook.active


# In[27]:


# Write data into the worksheet
worksheet['A1'] = 'Hello'
worksheet['B1'] = 'World!'


# In[28]:


# Save the workbook
workbook.save('example.xlsx')


# In[30]:


import tkinter as tk


# In[31]:


root = tk.Tk() # creates a new instance of a Tkinter window
root.title("My Application") # sets the title of the window
# create a label widget
my_label = tk.Label(root, text="Hello, World!")
my_label.pack() # add the label to the window

root.mainloop() # start the event loop


# In[33]:


x = 10
y = 5
# Addition
z = x + y
print(z)  # Output: 15
# Subtraction
z = x - y
print(z)  # Output: 5
# Multiplication
z = x * y
print(z)  # Output: 50
# Division
z = x / y
print(z)  # Output: 2.0
# Floor Division
z = x // y
print(z)  # Output: 2
# Modulo
z = x % y
print(z)  # Output: 0
# Exponentiation
z = x ** y
print(z)  # Output: 100000


# Typecasting vs conversion

# In[34]:


# Implicit type conversion
x = 5
y = 3.14
z = x + y   # x is implicitly converted to a float

# Explicit type conversion
a = "10"
b = int(a)  # convert string to integer explicitly

# Typecasting
c = 3.14
d = int(c)  # typecast float to integer


# Boolean operators

# In[35]:


x = 10
y = 5

# and operator
if x > 5 and y < 10:
    print("Both conditions are True")

# or operator
if x > 10 or y < 5:
    print("At least one condition is True")

# not operator
if not(x > 10):
    print("x is not greater than 10")


# Logical and Comparison operators

# In[36]:


x = 5
y = 10
z = 15

if x < y and y < z:
    print("x is less than y, and y is less than z")
else:
    print("x is not less than y, or y is not less than z")


# In[37]:


import pandas as pd
# create a dictionary with sample data
data = {'Name': ['Bilal', 'Emma'],
        'Age': [32, 28],
        'City': ['New York', 'London']}
# create a DataFrame from the dictionary
df = pd.DataFrame(data)
# print the DataFrame
print(df)


# In Python, the membership operators in and not in are used to check if a value is present or absent in a sequence, such as a list, tuple, or string.
# 
# The in operator returns True if the value is present in the sequence, and False otherwise. For example:

# In[38]:


my_list = [1, 2, 3, 4, 5]
3 in my_list
True
6 in my_list
False


# The not in operator returns True if the value is not present in the sequence, and False otherwise. For example:

# In[39]:


my_list = [1, 2, 3, 4, 5]
3 not in my_list
False
6 not in my_list
True


# So, in summary, the in operator checks if a value is present in a sequence, while the not in operator checks if a value is absent from a sequence.

# # Introduction to Turtle in python.
# Turtle is a built-in Python library that allows you to create graphics and draw shapes using a virtual "turtle" that moves around the screen. It was originally developed for teaching programming to children but has since been used for a wide range of applications.
# 
# Here is a simple example of how to use Turtle in Python:
# 

# In[40]:


import turtle
# Create a Turtle object
my_turtle = turtle.Turtle()
# Draw a square
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
# Exit the turtle window when clicked
turtle.exitonclick()


# In this example, we first import the Turtle library and create a Turtle object called my_turtle. We then use a for loop to draw a square by moving the turtle forward 100 pixels and turning right 90 degrees four times. Finally, we call the exitonclick() method to keep the turtle window open until the user clicks on it.
# 
# There are many more methods available in the Turtle library for drawing different shapes, changing colors and pen sizes, and controlling the turtle's movement. To learn more about Turtle, you can refer to the official documentation or explore online tutorials and examples.

# # Turtle Basic commands such as Forward(), Back(), Left(), right()

# In the Turtle library of Python, the commands you mentioned are used to move a virtual "turtle" on a graphical canvas. Here's a brief explanation of each of these commands:
# 
# forward(distance): Moves the turtle forward in the direction it is facing by the specified distance. The distance parameter is a number that specifies the distance to move, in pixels.
# backward(distance): Moves the turtle backward, in the opposite direction it is facing, by the specified distance.
# left(angle): Turns the turtle to the left by the specified angle, in degrees.
# right(angle): Turns the turtle to the right by the specified angle, in degrees.
# Here's an example code snippet that demonstrates the use of these commands to draw a square:

# In[41]:


import turtle
# Create a turtle object
t = turtle.Turtle()
# Move the turtle forward 100 pixels
t.forward(100)
# Turn the turtle to the left by 90 degrees
t.left(90)
# Move the turtle forward 100 pixels
t.forward(100)
# Turn the turtle to the left by 90 degrees
t.left(90)
# Move the turtle forward 100 pixels
t.forward(100)
# Turn the turtle to the left by 90 degrees
t.left(90)
# Move the turtle forward 100 pixels
t.forward(100)
# Exit the turtle graphics window when clicked
turtle.exitonclick()


# This code creates a Turtle object, moves it forward 100 pixels, turns it left by 90 degrees, and repeats this process to draw a square. Finally, it exits the Turtle graphics window when you click on it.
# 
# I hope this helps! Let me know if you have any further questions.

# In[ ]:




