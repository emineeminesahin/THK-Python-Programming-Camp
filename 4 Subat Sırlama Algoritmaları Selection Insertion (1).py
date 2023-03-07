#!/usr/bin/env python
# coding: utf-8

# In[9]:


def secereksırala(L):
    for i in range(len(L)):
        minimum=i
        for j in range(i+1,len(L)):
            if L[j]<L[minimum]:
                minimum=j
        gecici = L[i]
        L[i] = L[minimum]
        L[minimum] = gecici
        #L[minimum],L[i]= L[i], L[minimum]
        #print(L)
    return L

L=[45,9,-5,3,-11,4,99]
sonuc=secereksırala(L)
print(sonuc)



# In[8]:


def eklemesıralama(L):
    for i in range(len(L)):
        deger=L[i]
        j=i-1
        while j>=0 and deger<L[j]:
            L[j+1]=L[j]
            j-=1
        L[j+1]=deger
            
nlist = [14,46,43,27,57,41,45,21,70]
eklemesıralama(nlist)
print(nlist)       
    


# In[ ]:




