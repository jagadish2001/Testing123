#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" Operators in python
    They have Seven Types of Operators in Python
    1.Arithmetic operators
    2.Assignment operators
    3.Comparison operators
    4.Logical operators
    5.Identity operators
    6.Membership operators
    7.Bitwise operators
"""


# In[80]:


# 1.Arithmetic operators

# "+","-","*","/","//","**","%"

a = 4
b = 2
print("This is add",a+b)
print("This is sub",a-b)
print("This is mul",a*b)
print("This is div",a/b)
print("This is floor div",a//b)
print("This is modules",a**b)
print("This is percentage",a%b)  


# In[20]:


# 2.Assignment operators

# "==","+=","-=","/=","%=","//=","*="

a = 2
b = 4
print(a==b)


# In[22]:


a = 2
a += 4
print(a)


# In[23]:


a = 2
a -= 4
print(a)


# In[24]:


a = 2
a *= 4
print(a)


# In[25]:


a = 2
a /= 4
print(a)


# In[26]:


a = 2
a //= 4
print(a)


# In[27]:


a = 2
a %= 4
print(a)


# In[29]:


# 3.Comparison operators

# "==","!=",">","<",">=","<="

a = 2
b = 4
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


# In[42]:


# 4.Logical operators

# "And","Or","Not"

a = 2
b = 4
if a!=b:
    c = (a<b and a<b) #Returns True if both statements are true
    print(c)
else:
    print("no")


# In[54]:


a = 5
print(a > 3 or a < 4) #Returns True if one of the statements is true


# In[62]:


a = 5
print(not(a > 3 and a < 4)) #Reverse the result, returns False if the result is true


# In[67]:


# 5.Identity operators

#"is","is not"

a = 2
b = 2
print(a is b)
print(a is not b)


# In[73]:


# 6.Membership operators

# "in","not in"

a = ["apple","orange","guva"]
print("apple" in a)
print("orange" not in a)


# In[78]:


# 7.Bitwise operators

# "&","|","^","<<",">>"

a = 2
b = 4
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)


# In[ ]:




