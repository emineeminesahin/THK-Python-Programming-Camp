#!/usr/bin/env python
# coding: utf-8

# In[12]:


def larama(L,a):
    for i in range(len(L)):
        if L[i]==a:
            return i+1
    return 0
L=[2,3,34,56,45,32,11,89,4,1,444]

a=int(input("Lütfen Aranacak Sayıyı Giriniz   "))
sonuc=larama(L,a)
print(sonuc)
if sonuc>0:
    print("Aradığınız",a , "Listede ", sonuc, "numarada mevcuttur")
else:
    print("Aradığınız",a , "Listede Mevcut Değil")


# In[15]:





# In[ ]:




