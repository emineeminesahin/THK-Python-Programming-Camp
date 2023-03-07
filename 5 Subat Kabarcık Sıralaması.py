#!/usr/bin/env python
# coding: utf-8

# In[1]:


def kabarcıksıralaması(L):
    for i in range(len(L)):
        for j in reversed(range(i+1,len(L))): #for j in range(len[L]-1,0,-1)
            if L[j]<L[j-1]:
                temp=L[j-1]
                L[j-1]=L[j]
                L[j]=temp
    print(L)

L=[3,5,1,10,-3,8]
kabarcıksıralaması(L)


# In[ ]:




