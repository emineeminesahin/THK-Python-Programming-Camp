#!/usr/bin/env python
# coding: utf-8

# In[83]:


#Diziler (Array) / listeler (List) => Köşeli Parantez ile tanımlanır [] 
#ilk tanımlanma sırasında değer ataması yapılabilir
b=[] #b değişkeni boş bir liste olarak tanımlanmıştır
#metin parçalayarak liste oluşturma =>list metodu kullanılarak yapılır
#list() parantezin içine parşalanacak metin değeri parametre olarak girilimesi gerekir
D="ABCDEFGHIJKLMN"
yenilst=list(D)
print(yenilst)
print()
lst=[2,'B','C',5,'E',"Merhaba",8,'H','I',100,'O','P','R','S','Ş']
x=lst[0]+lst[3] 
# + listedeki iki sayının toplamı için kullanılan matematiksel operatör
y=lst[5]+":"+lst[7]+lst[8]
# + listedeki metin ifadelerinin birleştirilmesi olarak dikkate alınır
print("Toplam Değerler:\t",x,"\n'Metin Birleştirme'",y)
print("Orjinal Liste:",lst)
#lst[2]='Ç'
dizi[6]='Ğ'
yeni_dizi=lst
#Baştan 5. indekse kadar (dahil değil)
print("Listenin İlk 5 elemanı:",lst[:5])
#5. indeksten sonuna kadar getir
print("Listenin 5. elemandan sonraki kalan değerleri:",lst[5:])
#10 ncu ve 13ncü arasını alma (dahil değil)
yeniaraliste=lst[10:12]
print(yeniaraliste)
print(len(yeniaraliste))
#print(yeni_dizi[1],yeni_dizi[0],yeni_dizi[1],yeni_dizi[0])
len(lst) #len() metodu => dizinin karakter sayısını  length:uzunluğu gösterir
#listeleri birleştirme 
listebirlestir=dizi+yeniaraliste
#listenin elemanını değiştirme, aşağıdaki kod parçacığı listenin 11nci elemanınındeğerini değiştirir
listebirlestir[10]='Deneme'
print(listebirlestir[10:])
#liste çarpma işlemi ile tekrarlama
listecarpma=dizi*2
print(listecarpma)
#print (dizi[0],dizi[14-1],dizi[14-1],dizi[4])


# In[123]:


#listelere ilişkin temel metodlar-fonksiyonlar
#listenin sonuna eleman eklemek için kullanılan metod append()
lst.append("Deneme")
lst.append("En Son Değer")


#pop() metodu ile diziden eleman çıkartılır, 
#parantez içine indeks numarası yazılır ve o indeksin elemanı listeden çıkartılır
lst.pop(5)
print(lst)


#listenin sıralanması için sort() metodu kullanılır

sırala=[1,23,567,6545,6789,7678,56,45,3,56,76]
#listenin elemanları küçükten büyüğe doğru sıralanır
sırala.sort()
print(sırala)
#liste elemanlarını büyükten küçüğe sıralamak için kullanılr
sırala.sort(reverse=True)
tersi=sırala.reverse()
print(tersi)
#remove() metodu, listeden bir elemanı silmek için kullanılır
#silinmek istenen değer , parantez iin de tam olarak listede yazıldığı şekli ile belirtmelisiniz
lst.remove('Deneme')
print(lst)
lst.append("EEEEEE")
print(lst)

#lst.pop(len(lst)-1)

lst.pop()
print(lst)


# In[ ]:




