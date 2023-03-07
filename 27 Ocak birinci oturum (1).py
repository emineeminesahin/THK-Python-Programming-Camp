#!/usr/bin/env python
# coding: utf-8

# In[4]:


#print() fonksiyonu ile ilgili örnek kodlar


print("3+5") # (+) Çift tırnak içinde yer aldğından dolayı sadece ekranda yazdırılır
print(3+5) # (+) Matematiksel işlem olarak değerlendirilir ve iki sayının toplamını verir
print('3'+'5') # (+) iki metin ifadesinin birleştirilmesi için kullanılır
print('Merhaba Dünya')


x="Meltem" # x bir metin (string) değişkeni olup, Meltem değerine sahiptir
y="YILDIRIM" # y bir metin (string) değişkeni olup, YILDIRIM değerine sahiptir
print(x+" "+y)


# In[16]:


#Değişkenlere defalarca farklı değer atama
x=10
print("x in ilk aldığı değeri yazdır:", x)
y=20

print("x ve y nin toplamını:", x+y)
x=20

print("hemen öncesindeki x in aldığı değeri yazdır:", x)
x=30
y=40
print(x+y)


# In[29]:


#Çoklu Atama
x,y,z=100,-45,5
print("X=",x,"Y=",y,"Z=",z)
t=x+y+z
t=50
print("X+Y+Z=",t)
print("Toplam X+Y+Z=",x+y+z)
print("Ortalama",t/3)
print("Parantezden ötürü yanlış hesaplanan ortalama",x+y+z/3)


# In[35]:


# Koşul İşlemleri (Karar)      
# x==y Eğer x ve y birbirine eşitse doğrudur  
# 1. x<y veya 2. x>y Eğer 1. için x y den küçük ise doğru, 2. için x y den büyük ise doğru
# 1. x<=y veya 2. x>=y Eğer 1. için x y den küçük yada eşit ise doğru, 2. için x y den büyük yada eşit ise doğru
# x!=y Eğer x ve y birbirinden fakrlı ise doğrudur, eşit değil ise


x=10
y=10
if x<y:
    print("Birinci Sayı İkinci Sayıdan Küçüktür")
if x>y:
    print("Birinci Sayı İkinci Sayıdan Büyüktür")
if x==y:
    print("İki sayı birbirine eşittir")
    


# In[ ]:


# Kullanıcıdan veri alarak Koşul İşlemleri (Karar) program parçası      

x=int(input("Lütfen Birinci Sayıyı Giriniz:"))
y=int(input("Lütfen İkinci Sayıyı Giriniz:"))


if x<y:
    print("Birinci Sayı İkinci Sayıdan Küçüktür", "Birinci Sayı X=",x,"İkinci Sayı Y=",y)
if x>y:
    print("Birinci Sayı İkinci Sayıdan Büyüktür",x ,">", y)
if x==y:
    print("İki Sayı Birbirine Eşittir")
print("Girmiş olduğunuz iki sayının karşılaştırmasını yukarıda bulabilirsiniz")
    


# In[54]:


# Kullanıcıdan veri alarak Koşul İşlemleri (Karar) program parçası      
x=int(input("Lütfen Birinci Sayıyı Giriniz:"))
y=int(input("Lütfen İkinci Sayıyı Giriniz:"))

if x<y:
    print("Birinci Sayı İkinci Sayıdan Küçüktür", "Birinci Sayı X=",x,"İkinci Sayı Y=",y)
elif x>y:
    print("Birinci Sayı İkinci Sayıdan Büyüktür",x,">", y)
else:
    print("X ve Y Birbirine Eşittir")
print("Girmiş olduğunuz iki sayının karşılaştırmasını yukarıda bulabilirsiniz")
    


# In[ ]:




