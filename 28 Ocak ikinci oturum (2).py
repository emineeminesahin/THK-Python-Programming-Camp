#!/usr/bin/env python
# coding: utf-8

# In[30]:


#liste/dizi işlemleri
# [] köşeli parantez ile dizi/liste tanımlaması yapılır
den=[]
print(den)
liste=[2,5,6,4,7,8,9,6,2,32,56,22,32320,45]
print(liste)
str_liste=["A",'B','Merhaba','Dünya','H',9,10]
print("Str_Liste içindeki elemanları listeler:",str_liste)

x=str_liste[-1]+str_liste[-2]
y=str_liste[2]+str_liste[3]

print(x,y)

den=str_liste*2
print(den)
print("Dizinin İlk Elemanının Değerini Gösterir:",den[0])
# [-1], indeks değerinin -1 olduğu durum, listenin son elemanı ile işlem yapmak için kullanılır
print("Dizinin Son Elemanının Değerini Gösterir:",den[-1])
print("Dizinin Son İkinci Elemanının Değerini Gösterir:",den[-2])
#len() metodu, verilen liste/dizi uzunluğunu (length) döndürür, 
#parantez içinde mutlaka uzunluğunu görmek istediğimiz listenin adı yer almalıdır.
print("Dizinin Son Elemanının Değerini Gösterir:",den[len(den)-1])
#Metin (String) Parçalayarak dizi/liste oluşturmak için list() metodu kullanılır
#list() parantez içine , listeye dönüştürülecek metin değeri yazılır
D="ABCDEFGHIJKLMN"
D_Liste=list(D)
ucuncu=D_Liste[2]
print("Listenin Üçüncü Elemanının Değeri:",ucuncu,"dir.")
# \n ifadesi , print içinde tırnaklar ("") arasına yazılır ve hemen sonrasındaki ifadeleri bir sonraki satırda ekranda göstermek için kullanılır.
print("Metinden Parçalanarak Liste Oluşturumak:\n",D_Liste,"\n Oluşturulan Listenin Uzunluğu",len(D_Liste))



# In[53]:


str_liste=["A",'B','Merhaba','Dünya','H',9,10]
print("Str_Liste içindeki elemanları listeler:",str_liste)
#(+) iki sayının toplamı olarak dikkate alınır
x=str_liste[-1]+str_liste[-2]
#(+) iki metin ifadesinin birleşimi olarak dikkate alınır
y=str_liste[2]+" "+str_liste[3]

print("Listedeki Sayıların Toplamı=",x,"'\n'\nListedeki İki İfadenin Mesajı:'",y,"'")


# In[58]:


lstyn=[2,5,78,98,656,5223564,14,56,98,78,98,99,66,23,21]
# [:5] baştan 5. indekse kadar olan değerleri getirir (5 dahil değil)
yarım=lstyn[:5]
print(yarım)
# [5:] ise, 5. indeksten sonuna kadar listeyi getirir
kalan=lstyn[5:]
print(kalan)
# [5:9], 5'ten 9'a kadar olan kısmı almak için kullanılır
orta=lstyn[5:9] 
print(orta)
print(lstyn)
#kullanıcıdan alınan bir değerin listeye eklenmesi
yenisayıekle=int(input("Listeye Değer Ekleyin:"))
#append() metodu ile listenin sonuna bir değer eklenir, eleman sayısı bir artar
lstyn.append(yenisayıekle)
print(lstyn)
lstyn[5]=564
print(lstyn)

print("\\n Merhaba Dünya")


# In[73]:


d="ABFKGLHKRODMSKLSŞDSF"
liste=list(d)
print(len(liste))

#listenin 4. indeksine Z değerini ekleyelim
#Bunun için insert()metodu kullanılır 
#ve mutlaka parantez içinde ilk önce hangi indeks olacağı belirtilir, 
#daha sonra ise alacağı değer yazılı

liste.insert(4,'Merhaba')
liste.insert(len(liste),10)

#listeden değer silmek için remove() metodu kullanılır
#listeden Merbaha kelimesini silelim
liste.remove('Merhaba')
#pop() metodu ile de listeden verilen indeks numarasındaki değer silinir.
#silinecek değerini indeks bilgisi pop() metodunda parantez içinde belirtilmelidir. 
liste.pop(4)

#listenin sonundaki değerin silinmesi için pop() metodu parametresiz kullanılır
liste.pop()
print(liste)
print(len(liste))


# In[95]:


lstyn=[1998,2000,2005,1998,1999,2000,2005,2001,2003,2004,1999,1998,2004,2001,2002,2003,2000]
#sort() metodu listedeki değerlerin küçükten büyüğe sıralanması için kullanılır
lstyn.sort()
#print(lstyn)
#reverse() metodu, sıralamayı büyükten küçüğe olacak şekilde yapar
#lstyn.sort(reverse=True)
lstyn.reverse()
#print(lstyn)
#print("Listedeki En Küçük Değer:",min(lstyn),"\nListedeki En Büyük Değer:",max(lstyn))

#count() metodu liste içinde tekrarlayan elemanların sayısını almak için kullanılır
dogumtarihi=int(input("Lütfen Kaç Adet Olduğunu Öğrenmek İstediğiniz Doğum Tarihi Yılını Giriniz:"))
print("Listenin İçinde",dogumtarihi, "Yılı Doğumlular Toplamı ",lstyn.count(dogumtarihi))


# In[ ]:





# In[ ]:




