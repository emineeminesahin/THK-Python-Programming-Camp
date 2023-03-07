#!/usr/bin/env python
# coding: utf-8

# In[4]:


lst1=['Nisan','Şubat','Nisan','Nisan','Haziran']
lst3=[3,4,5,4,5,5,5,6,6,7,7,77,6,5,4,4,3,3]
lst3.sort()
lst3.reverse()
print(lst3)
print(lst1,len(lst1))
print(lst1[0])
print(lst1[-1])
print("ilk elemandan başlayarak her ikinci elemanı yazdır")
print(lst1[::2])
print(lst1[::-1])
print(lst1)
#ilk elemandan başlayarak her üçüncü elemanı yazdır
lst2=lst1[1::3]
print("lst2 listesi",lst2)

lst1.insert(2,'Mart')
lst1.append('Temmuz')
for eleman in lst1:
    print (eleman,end=" ")
print()
ara=input("Aranacak Ay bilgisini Giriniz")    
if ara in lst1:
    adet=lst1.count(ara)
    print ("lst1 içinde ",ara,adet,"adet bulunmaktadır")
   
else:
    print("Aradığınız değer liste içinde mevcut değildir")
 

print()
print(lst1)
lst1[2]='Ağustos'
print(lst1)
#lst1.pop(0)
#lst1.reverse()
#print(lst1)
#lst1.sort()
#print(lst1)
lst1.remove('Ağustos')

print(lst1)


# In[ ]:




