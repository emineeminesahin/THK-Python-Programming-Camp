#!/usr/bin/env python
# coding: utf-8

# In[13]:


print("Yapmak istediğiniz işlemi seçiniz. ( 'T' Toplama - 'Çı' Çıkarma - 'Ça' Çarpma - 'B' Bölme ) ")
 
def Carp(x, y):
    sonuc=x * y   
    return sonuc
 
def Bol(x, y):
   return x / y 
 
def Topla(x, y):
   return x + y
 
def Cikar(x, y):
   return x - y
 
secim = input("Seçim :")

sayi1 = int(input("1. Sayı Giriniz: "))
 
sayi2 = int(input("2. Sayı Giriniz: "))
 
if secim == 'T':
    
   print("\n" , sayi1 , " + " , sayi2 , " = " , Topla(sayi1,sayi2) )
 
elif secim == 'Çı' or secim=='çı' or secim=='ÇI':
    
   print("\n" , sayi1 , " - ", sayi2 , " = " , Cikar(sayi1,sayi2) )
 
elif secim == 'Ça':
    
   print("\n" , sayi1 , " * ", sayi2 , " = " , Carp(sayi1,sayi2) )
 
elif secim == 'B':
    
   print("\n" , sayi1 , "/ " , sayi2 , " = ", Bol(sayi1,sayi2) )
else:
   print(" Lütfen işlem yapmak için 1-2-3-4 seçeneklerinden birini seçiniz. ")
 


# In[14]:


print("Yapmak istediğiniz işlemi seçiniz. ( 'T' Toplama - 'Çı' Çıkarma - 'Ça' Çarpma - 'B' Bölme ) ")
# aşağıdaki 4 fonksiyon yerine HesapMakinesi olarak tek bir fonksiyon ile çözme 

def HesapMakinesi (x,y,i):
    secim=i
    sayi1=x
    sayi2=y
    if secim == 'T':
        print("\n" , sayi1 , " + " , sayi2 , " = " , sayi1+sayi2 )
    elif secim == 'Çı' or secim=='çı' or secim=='ÇI':
        print("\n" , sayi1 , " - ", sayi2 , " = " , sayi1-sayi2 )

    elif secim == 'Ça':
        print("\n" , sayi1 , " * ", sayi2 , " = " , sayi1*sayi2 )

    elif secim == 'B':
        print("\n" , sayi1 , "/ " , sayi2 , " = ", sayi1/sayi2 )
    else:
        print(" Lütfen işlem yapmak için 1-2-3-4 seçeneklerinden birini seçiniz. ")

      
   
    
islem = input("Seçim :")

x = int(input("1. Sayı Giriniz: "))
 
y = int(input("2. Sayı Giriniz: "))

HesapMakinesi(x,y,islem)
 


# In[ ]:




