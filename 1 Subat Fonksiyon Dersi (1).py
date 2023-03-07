#!/usr/bin/env python
# coding: utf-8

# In[34]:


#bir sayının karesini alan fonksiyon yazınız
def kare(z):
    sonuc=z**2
    return sonuc
    
def kup(n):
    sonuc=pow(n,3) #üs almak için kullanılan fonksiyondur
 
    return sonuc  
    
#kare fonksiyonunun ana program içinde çağrılması
o=int(input("Lütfen Karesi Alınacak Bir Sayı Giriniz:"))
print("Kup Fonksiyonunun Çıktısı=",kup(o))
print("Kare Fonksiyonunun Çıktısı=",kare(o))


  


# In[ ]:




