#!/usr/bin/env python
# coding: utf-8

# Q1. Create a python program to sort the given list of tuples based on integer value using a
# lambda function.
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# In[1]:


a =[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]


# In[2]:


b =[('mateen',15515151),('abdul',122555545),('nagthan',44154515)]


# In[3]:


sort1 =sorted(b,key =lambda x:x[1])


# In[4]:


print(sort1)


# #Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
# lambda and map functions.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In[5]:


squares =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda a:a*a,squares))


# #Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions 
# Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

# In[6]:


lst =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
str_lst =tuple(map(lambda x: str(x),lst))

print(str_lst)


# # Q4. Write a python program using reduce function to compute the product of a list containing numbers
# from 1 to 25.

# In[10]:


from functools import reduce
a =1
b =[]
while a <= 25:
    b.append(a)
    a+=1


numbers =reduce(lambda x,y : x*y,b)
print(numbers)


# In[13]:


# Q5. Write a python program to filter the numbers in a given list that 
# are divisible by 2 and 3 using the
# filter function.
 # [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]


# In[1]:


lst =[12,54,2151,2151,12,12,111,1215121558,151214844,1121227]
divisible_by_2_and_3 = lambda x:x % 2 ==0 and x % 3 ==0
filtered_lst =list(filter(divisible_by_2_and_3,lst))

print(filtered_lst)


# In[2]:


# Q6. Write a python program to find palindromes in the given list of 
# strings using lambda and filter
 # function.
# ['python', 'php', 'aba', 'radar', 'level']


# In[8]:


lst = ['python', 'php', 'aba', 'radar', 'level']
is_palindrome = lambda s:s ==s[::-1]

palindrome_lst =list(filter(is_palindrome,lst))

print(palindrome_lst)


# In[ ]:




