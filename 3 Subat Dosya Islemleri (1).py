#!/usr/bin/env python
# coding: utf-8

# In[33]:


import os
f=open("dosyaadi.doc","a")
L1=[1,2,3,4,5,6,7,6,5,4,3,4,34,3]
L="MERHABA"
L2=list(L)
for i in range(len(L2)):
    eleman=str(L2[i])+" "
    f.write(eleman)
f.write("\n")
for i in range(len(L1)):
    eleman=str(L1[i])+" "
    f.write(eleman)
f.write("\n")
f.truncate()
f.close()
ac=open("dosyaadi.doc","r")
for i in ac:
    print(i)
ac.close()
#os.remove("dosyaadi.doc")


# In[ ]:





# In[ ]:




