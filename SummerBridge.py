#!/usr/bin/env python
# coding: utf-8

# In[ ]:


3 + 7


# In[ ]:


print("hello")


# In[ ]:


print(7)


# In[ ]:


name = "Kyle"
age = 42


# In[ ]:


print(age)


# In[ ]:


# this is a comment. it won't run. use lots of comments
# you can echo values without using print in this notebook
name


# # Variables and Values

# In[ ]:


#variables can be used in calculations
print(age)
age = age + 3
print(age)


# In[ ]:


# order fo operations matters
first = 1
second = first * 5
first = 2
print (first)
print(second)


# In[ ]:


# values have types. types effect what you can do with them
print(5-3)
#print("hello" - "h")


# In[ ]:


print(len("hello"))
#print(len(6))


# ## challenge
# explain what each operator does
# 
# print(5 // 3)
# print(5 / 3)
# print(5 % 3)

# In[ ]:


print(5 // 3)
# how many times 3 goes into 5. floor operator. main divisor


# In[ ]:


print(5 / 3)
# just division


# In[ ]:


print(5 % 3)
# remainder after 3 goes into 5. complement of first one. "weirdly useful" if trying to count things


# # getting help

# In[ ]:


# rounding numbers is built in
round(3.14159)


# In[ ]:


round(3.14159, 2)


# In[ ]:


help(round)


# In[ ]:


# ndigits=none means optional, default is 0 if left blank
round(3.14159,ndigits=2)
# same exact thing


# In[ ]:


# all functions return a new value
rounded_pi = round(3.14159, 2)
print(rounded_pi)


# ## challenge
# 
# what order do the operations happen?
# 
# radiance = 1.0
# 
# radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5)

# In[ ]:


help(max)
help(min)


# In[ ]:


radiance = 1.0
radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))
print(radiance)


# In[ ]:


# break down these operations
radiance = 1.0
min_arg_2 = 1.1 * radiance - 0.5
print("min arg 2:", min_arg_2)
min_result = min(radiance, min_arg_2)
print("min result:", min_result)
radiance = max(2.1, 2.0 + min_result)
print("radiance:", radiance)


# # A brief interlude with git

# In[ ]:




