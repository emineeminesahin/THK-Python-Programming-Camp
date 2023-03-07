#!/usr/bin/env python
# coding: utf-8

# In[19]:


# DÖNGÜLER 
#1...100 arasındaki sayıların toplamını alan programı yazınız => toplam=1+2+3+4+5+...+100
toplam=0 #Başlangıç değeri

#1. adımda => toplam=toplam+1
#2. adımda => toplam=toplam+2
#...
#100. adım => toplam=toplam+100

# for döngüsü : Belirli sayıda işlemlerin tekrarlanması için kullanılan döngülerdir.
#for n in range(başlangıçdeğeri, birişdeğeri+1) n birer  birer artırarak ilerler

for n in range(1,101):
    print("toplam=",toplam,"+",n) #çıktıda toplama işlemi olarak görüntülenmesi için "+" kullanılmıştır
    toplam=toplam+n  #matematiksel toplama işlemi yapılır
    print(n,"nci değer için toplam=",toplam)   
      
print("Tüm adımlar bittikten sonraki ileriye doğru topam değerini verir, TOPLAM=", toplam)
    
# 100 den 1 e kadar olan sayıların toplamını hesaplayan for döngüsü  
toplam=0
for n in range(100,0,-1):
    toplam=toplam+n  #matematiksel toplama işlemi yapılır      
print("Tüm adımlar bittikten sonraki geriye doğru topam değerini verir, TOPLAM=", toplam)
       
    
    


# In[25]:


#1..100 arasındaki çift sayıların toplamını hesaplayınız
#range kısmında ilk olarak 2'den başlayabilirsiniz 
#veya range ilk parametre 1 olacak ise, toplamda n yerine (n+1) yazmanız gerekiyor.
toplam=0
for n in range(2,101,2):
    print("toplam=",toplam,"+",n)
    toplam=toplam+n  #matematiksel toplama işlemi yapılır      
print("Tüm adımlar bittikten sonraki geriye doğru topam değerini verir, TOPLAM=", toplam)
       


# In[27]:


#Kullanıcıdan alına değere kadar 1'den başlayarak 
#tek sayıların toplamını hesaplayınız

toplam=0
sayi=int(input("Lütfen Toplmanını alınmasını istediğiniz sayı giriniz:"))
for n in range(1,sayi+1,2):
    toplam+=n #=> toplam=toplam+n
print("Girmiş Olduğunuz",sayi ,"Kadar olan Sayı Aralığındaki Tek Sayıların Toplamı:")
print(toplam)


# In[29]:


#Kullanıcıdan alına değere kadar 1'den başlayarak 
#tek sayıların toplamınını ayrı, çift sayıların toplamını ayrı hesaplayınız

toplamcift=0
toplamtek=0
sayi=int(input("Lütfen Toplmanını alınmasını istediğiniz sayı giriniz:"))
for n in range(1,sayi+1):
    if (n%2==0):
        toplamcift+=n
    else:
        toplamtek+=n
print("Girmiş Olduğunuz",sayi ,"Kadar olan Sayı Aralığındaki Tek Sayıların Toplamı:")
print(toplamtek)
print("Girmiş Olduğunuz",sayi ,"Kadar olan Sayı Aralığındaki Çift Sayıların Toplamı:")
print(toplamcift)


# In[37]:


#DÖNGÜLER :While
#ilk beş rakamın toplamını hesaplayınız
sayac=1 #Başlangıç değeri kontrol değişkenine atanır
toplam=0
while sayac<=5: #istenilen değere ulaşılıp ulaşılmadığını kontrol eder
    print("Sayac Değeri",sayac)
    print("Toplam Değeri",toplam)
    toplam=toplam+sayac   # toplam+=sayac
    sayac=sayac+1         # sayac+=1
    
    print("Toplam Değeri sayaç eklendikten sonra",toplam)
    print("Sayac Değeri artırıldıktan sonra",sayac)
    print()
    
print(toplam)
    


# In[46]:


#DÖNGÜLER :While
#ilk beş rakamın toplamını hesaplayınız
sayac=0 #Başlangıç değeri kontrol değişkenine atanır
toplam=0
while sayac<=5: #istenilen değere ulaşılıp ulaşılmadığını kontrol eder
    print("Sayac Değeri",sayac)
    print("Toplam Değeri",toplam)        
    sayac=sayac+1
    toplam=toplam+sayac
    print("Toplam Değeri sayaç eklendikten sonra",toplam)
    print("Sayac Değeri artırıldıktan sonra",sayac)
    print()
    
print(toplam)


# In[13]:


#İç İçe Döngüler
#Çarpım Talosu Hazırlayalım
sayi=int(input("Lütfen Tablo Ölçüsünü giriniz:"))
for satir in range (1,sayi+1):
    for sutun in range(1,sayi+1):
        sonuc=satir*sutun
        print("{:8}".format(sonuc),end="  ")  #tabloyu doldurmak içindir
       
    print()  #bir sonraki satıra geçmek için kullanılır
print("Girdiğiniz değer ölçüsünde çarpım tablosu çıktısı yukarıdadır")


# In[ ]:




