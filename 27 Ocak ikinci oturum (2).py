#!/usr/bin/env python
# coding: utf-8

# In[36]:


print("Merhaba Dünya")
x=5*7+6/3 #değişken tanımlaması x bir değişkendir ve farklı değerler alabilir
print (x)
print ("Verilen (5*7)"+"+"+"(6/3) Matematiksel İşlemin Sonucu=",x)
print ("Verilen 5*7+6/3 Matematiksel İşlemin Sonucu=", x)
print ("Python"+  "  "    +"Programlama"+  " "   +"Kampı")
X=30
print ("27 Ocak Python İlk Programlama Dersi")
print("Büyük X ve Küçük X değerlerinin gösterimi=>","X=",X,"x=",x)


# In[74]:


#Koşul (if) Karar Yapıları
x=8
y=18   #tek eşit .... = ..... sembolün sağındaki değeri, solundaki değişkene atamak için kullanılır.
        # x=9 y=x => y=9 anlamına gelir

if x!=y:
    print("Birinci Sayı ile İkinci Sayı Birbirinden Farklıdır")
    
if x<y:  #koşul doğru ise hemen altındaki satır işleme alınır
    print("Birinci Sayı İkinci Sayıdan Küçüktür:", "Birinci Sayı=",x, "İkinci Sayı=" , y)
if x>y:
    print("Birinci Sayı İkinci Sayıdan Büyüktür", x,">",y)
if x==y:  # .....== ...... sembolü sağında ve solunda kalan değerlerin birbiri ile karşılaştırılması için kullanılır
    # değerler birbirine eşit ise doğru döndürür 5==5 => Doğru / 5==6 => Yanlış döndürür 
    print("İki Sayı Eşittir")
    print("İki sayı birbirine eşit ise ekranda yazdırılır")  

    
    
    
    
print("İki sayı arasındaki karşılaştırma sonuçları için yukarıya bakınız")  


# In[76]:


#Koşul (if-else) Karar Yapıları
x=8
y=18   #tek eşit .... = ..... sembolün sağındaki değeri, solundaki değişkene atamak için kullanılır.
        # x=9 y=x => y=9 anlamına gelir

if x!=y:
    print("Birinci Sayı ile İkinci Sayı Birbirinden Farklıdır")
    print("Birinci Sayı ile İkinci Sayının Çarpımı=",x+y)
    

    
else:  # .....== ...... sembolü sağında ve solunda kalan değerlerin birbiri ile karşılaştırılması için kullanılır
    # değerler birbirine eşit ise doğru döndürür 5==5 => Doğru / 5==6 => Yanlış döndürür 
    print("İki Sayı Eşittir")
    print("İki sayı birbirine eşit ise ekranda yazdırılır")  
    print("Sayının Karesi=",x*y)
    
    
    
    
print("İki sayı arasındaki karşılaştırma sonuçları için yukarıya bakınız")  


# In[ ]:


#Koşul (if-elif-else) Karar Yapıları ikiden fazla koşul olması durumunda kullanılır, 
#ilk olarak If sonrasındaki ikinci ve diğer koşullarda elif kullanılır, en son koşul için sadece else : yazılır else yanında herhangi bir karşılaştırma yer almaz.

x=8
y=18   #tek eşit .... = ..... sembolün sağındaki değeri, solundaki değişkene atamak için kullanılır.
        # x=9 y=x => y=9 anlamına gelir

if x!=y: # != Eşit değildir demek => sembolün sağında ve solundaki değerler birbirinden farklı ise Doğru değeri döndürür
    print("Birinci Sayı ile İkinci Sayı Birbirinden Farklıdır")
    
elif x<y:  #koşul doğru ise hemen altındaki satır işleme alınır
    print("Birinci Sayı İkinci Sayıdan Küçüktür:", "Birinci Sayı=",x, "İkinci Sayı=" , y)
elif x>y:
    print("Birinci Sayı İkinci Sayıdan Büyüktür", x,">",y)
else:  # .....== ...... sembolü sağında ve solunda kalan değerlerin birbiri ile karşılaştırılması için kullanılır
    # değerler birbirine eşit ise doğru döndürür 5==5 => Doğru / 5==6 => Yanlış döndürür 
    print("İki Sayı Eşittir")
    print("İki sayı birbirine eşit ise ekranda yazdırılır")  
    
    
    
    
print("İki sayı arasındaki karşılaştırma sonuçları için yukarıya bakınız")  

