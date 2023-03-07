#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#DÖNGÜLER ÖRNEK
#Girilen Değere Göre "*" karakterinden ağaç çizen program yazalım
yukseklik=int(input("Çizilecek Ağacın yüksekliğini Giriniz:"))
satir=0
while satir<yukseklik: #satir = 0 ve yukseklik = 3 => 0<3 TRUE /DOĞRU
    sayac=0
    while sayac<yukseklik-satir: 
        print(end=" ")
        sayac+=1
        sayac=0
    while sayac<2*satir+1:
        print(end="*")
        sayac+=1
    print()
    satir+=1


# In[ ]:




