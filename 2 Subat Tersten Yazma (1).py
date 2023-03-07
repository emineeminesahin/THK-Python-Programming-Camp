#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Verilen Bir Sayının Tersten Yazımını Yapan Program
#12345 => 54321
sayi=int(input("Sayı giriniz:"))
ters=0
while (sayi>0):
    gecici=sayi%10
    ters=(ters*10)+gecici
    sayi=sayi//10
print("Sayının ters çevrilmiş hali=",ters)
    


# In[1]:


#Özyinelem ile tersten yazdıran program

def tersten(sayi,ters):
    if sayi==0:
        return ters
    else:
        return (tersten(sayi//10,(ters*10+sayi%10)))
    
sayi=int(input("Sayı giriniz:"))

print("Sayının ters çevrilmiş hali=",tersten(sayi,0))


# In[15]:


#Metin tersten yazdıran
def Ters(lst):
    temp=""
    for i in lst:
        temp=i+temp
    return temp

#lst = [10, 11, 12, 13, 14, 15]
ls="MERHABA"
lst=list(ls)
print(Ters(lst))


# In[ ]:




