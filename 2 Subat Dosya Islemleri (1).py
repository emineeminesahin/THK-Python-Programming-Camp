#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
f=open("dosyam.txt","a")
sayi=0
while True: #Sayı negatif te olsa pozitifte olsa her durumda çalışır , 
            #girilen değer 99 olana kadar , çünkü 99 için break komutu devreye girer
    sayi=int(input("Lütfen Sayı Giriniz(Çıkış İçin 99):"))
    if sayi!=99:
        f.write(str(sayi)+" ")
        print(str(sayi))
    else:
        break #Döngüden Çıkar
f.write("Deneme"+"\n")
f.close()
#os.remove("dosyam.txt")



# In[3]:


for satir in open("dosyam.txt","r"):
    print (satir.replace("Deneme","99"))
    if satir==4444:
        f.write("Deneme"+"\n")
    else:
        print(satir)
    
            


# In[ ]:




