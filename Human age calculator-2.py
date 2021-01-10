#!/usr/bin/env python
# coding: utf-8

# In[46]:


def Cat_converter():
    Ha = input("How many years would you like to convert into cat years?")
    Ha = int(Ha)
    if Ha == 1:
        x = 15
    elif Ha == 2:
        x = 24
    else:
        x = 24 + 4 * (Ha - 2)
    print("That would equal to", x, "cat years.")


# In[49]:


def Dog_converter():
    Ha = input("How many years would you like to convert into cat years?")
    Ha = int(Ha)
    if Ha == 1:
        x = 12
    elif Ha == 2:
        x = 24
    else:
        x = 24 + 4 * (Ha - 2)
    print("That would equal to", x, "dog years.")


# In[50]:


T = str(input("Would you like to convert human years into dog or cat years?"))
typ = T.lower()
if typ in ['cat']:
    Cat_converter()
elif typ in ['dog']:
    Dog_converter()
