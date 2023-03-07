#Python ile toplam, çıkarma, çarpma ve bölme işlemini fonksiyon kullanarak gerçekleştiren
#print(" Lütfen işlem yapmak için 1(toplama)-2(cıkarma)-3(carpma)-4(bolme) seçeneklerinden birini seçiniz. ")

 

secim=int(input(" Lütfen işlem yapmak için 1(toplama)-2(cıkarma)-3(carpma)-4(bolme) seçeneklerinden birini seçiniz. "))
sayi1=int(input("1.sayiyi giriniz:"))
sayi2=int(input("2.sayiyi giriniz:"))          
  
          
def topla(sayi1,sayi2):
          sonuc=sayi1+sayi2
          return sonuc

 

def cıkar(sayi1,sayi2):
          sonuc=sayi1-sayi2
          return sonuc          

 

def carp(sayi1,sayi2):
          sonuc=sayi1*sayi2
          return sonuc          

 

          
def bol(sayi1,sayi2):
          sonuc=sayi1/sayi2
          return sonuc          
          
if secim==1:
          print("toplama sonucu:",topla(sayi1,sayi2))
elif secim==2:    
          print("cıkarma sonucu:",cıkar(sayi1,sayi2))
elif secim==3:
          print("carpma sonucu:",carp(sayi1,sayi2))
else:       
          print("bölme sonucu:",bol(sayi1,sayi2))