#!/usr/bin/env python
# coding: utf-8

# # Operators

# In[1]:


print(5+6)
print(5*6)
print(2**4)
print(4/3)
print(7//3)
print(4%2)


# # Variables

# In[2]:


x=4
print(type(x))
print(4)
x,y,z=3.1417, 67,5
print(x+y)
print(type(x))
z=True #First letter should be zero in declaring v
print(z)
print(type(z))
t=str(56)
print(t)
print(type(t))


# # Strings

# In[3]:


a='py'

b='charm'
print (a + b) # + will join the two strings
print (a,b)
print (a*5)
#print (a + 5) # Type Error: must be str, not int
print (a + str (5))
t = "Let's learn Python";
print(t)


# # Lists

# In[4]:


# Initialize list x
x = [1, 2, 3, 4]

# Note: Lists are not arrays because arrays consist of a single data type,
# whereas lists may contain variables of different data types.

# Take input from the user and convert it to an integer
x = int(input("Enter a number: "))  # input() function always inputs a string,
                                    # int() function is used to convert the string to an integer

# Initialize other variables
y = 3.14
z = "HELLO"

# Create a list with mixed data types
li = [x, y, z, 4]

# Print the list
print(li)

# List indexes
# From left to right: 0 -> 1 -> 2 -> 3
# From right to left: -1 -> -2 -> -3 -> -4

# Accessing the third element of the list
print(li[2])

# Slicing
# list[start:end:optional step size]; start is inclusive and end is exclusive

# Different ways to slice the list
print(li[1:3])       # Slicing from index 1 to 2 (end is exclusive)
print(li[0:4:2])     # Slicing from index 0 to 3 with a step size of 2
print(li[:])         # Slicing the entire list
print(li[0:])        # Slicing from index 0 to the end
print(li[1:3])       # Slicing from index 1 to 2 (end is exclusive)
print(li[0:4:2])     # Slicing from index 0 to 3 with a step size of 2

# More slicing examples
print(li[:])         # Slicing the entire list
print(li[0:])        # Slicing from index 0 to the end
print(li[:3])        # Slicing from the start to index 2 (end is exclusive)
print(li[2][1:4])    # Slicing the string element at index 2 from 1 to 3 (end is exclusive)

# Deleting an element from a list
del li[2]  # Delete the element at index 2
print(li)

# Copying lists
w = [1, 2, 3, 4]
x = w       # The assignment copies the reference to the original list
y = w[:]    # Slicing creates a new list

# Modifying the lists
x[0] = 6    # This changes the first element of list w (and x since they are the same)
y[1] = 9    # This changes the second element of list y (a copy of w)

# Print the modified lists
print(w)    # The original list w is changed because x is just a reference to w
print(y)    # The copied list y is changed independently


# # Indentation

# In[5]:


x = 2
if x == 10:
    print("this is inside if block")
    print("this is also inside if block")
print("this will print always")


# # Boolean operations

# In[6]:


#If statement
x = 2
y = 5

# Comparison operators
if x < y:
    print("x is less than y")

if y >= 4:
    print("y is greater than or equal to 4")

# Logical operators
if x == 2 and y > 4:
    print("x is 2 and y is greater than 4")

if not x == 10:
    print("x is not equal to 10")

if x == 2 or y < 4:
    print("x is 2 or y is less than 4")


# In[7]:


number = 23

if number == 24:
    print('number is equal to 24')
elif number < 24:
    print('number is less than 24')
else:
    print('number is higher than 24')


# # The while statements

# In[8]:


number = 23
while number < 50:
    print(number)
    number += 1
else:
    print("wow there is an else for while statement as well")


# # The for statement

# In[9]:


# Indentation
for i in range(10):
    if i == 6:
        break
    print(i)

print("----")

for i in range(3, 10):
    if i == 6:
        continue
    print(i)

print("----")

for i in range(1, 10, 3):
    print(i)


# # Functions

# In[10]:


# Function to print the maximum of two numbers
def print_max(a, b=0):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# Calling the function with different arguments
print_max(3, 4)
x = 5
y = 7
print_max(x, y)

# Keyword arguments example
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

# Calling the function with different keyword arguments
func(3, 7)
func(25, c=24)
func(c=50, a=100)

# Function to return the maximum of two numbers
def max(x, y):
    if x > y:
        return x
    else:
        return y

# Calling the function and printing the result
m = max(3, 5)
print(m)


# # Task1
# 
# x = [1, 2, 3, 4, 5], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]
# 
# a. Write python code using python indexing and slicing for the following output. Use only one print statement for each:  
# 
# i. [31, 32, 33, 34, 35]
# 
# ii. 23
# 
# iii. [22,23]
# 
# iv. [1, 3, 5]
# 
# b. Declare y = [0, 0, 0], now using for loop write average of first list in list ‘x’ on first index of list y and so on. 
# 
# The print(y) should give the output: [3.0, 23.0, 33.0]

# # a.

# In[11]:


x = [[1, 2, 3, 4, 5], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]


# In[12]:


x


# In[13]:


x[2]


# In[14]:


x[1][2]


# In[15]:


x[1][1:3]


# In[16]:


x[0][0], x[0][2], x[0][4]


# In[17]:


x[0][::2]


# # b.

# In[18]:


y=[0,0,0]


# In[19]:


for i in range(len(x)):
    y[i] = sum(x[i]) / len(x[i])  # Calculate the average and assign it to y

# Print the list y with averages
print(y) 


# # Task2
# 
# x = [1, 3, 5, 6, 7, 8, 6, 1, 2, 3]
# 
# y = [0, 0, 0, 0, 0, 0, 0, 0]
# 
# a. Write python code using while loop that write average of first three items on first index of y and so on. The print(y) should give the following output
# 
# Output : [3.0, 4.666666666666667, 6.0, 7.0, 7.0, 5.0, 3.0, 2.0]
# 
# b. Define a function that takes list length as argument and returns the average. Then calculate the average of x and y.

# # a.

# In[20]:


x = [1, 3, 5, 6, 7, 8, 6, 1, 2, 3]
y = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(8):
    for j in range(3):
   
        y[i] += x[i+j]

print(y)


# In[21]:


for i in range(8):
    y[i] /= 3
    print(y)
                


# # b.

# In[22]:


x = [1, 3, 5, 6, 7, 8, 6, 1, 2, 3]
y = [0, 0, 0, 0, 0, 0, 0, 0]

# Function to calculate average of a list
def calculate_average(lst):
    return sum(lst) / len(lst) if len(lst) > 0 else 0

# Calculate averages
average_x = calculate_average(x)
average_y = calculate_average(y)

print("Average of x:", average_x)
print("Average of y:", average_y)

