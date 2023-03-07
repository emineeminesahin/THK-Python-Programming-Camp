#emine_sahin_odev1
#Soru 1
#x,y,z degiskenleri arasinda en kücük olan tam sayiyi ekrana yazdirma.

x = int(input("Birinci tam sayiyi giriniz:"))
y = int(input("Ikinci tam sayiyi giriniz:"))
z = int(input("Ucuncu tam sayiyi giriniz:"))
Min = int

if x <= y and x <= z:
    Min = x
elif y <= x and y <= z:
    Min = z
elif z <= x and z <= y:
    Min = z
print("En kucuk tam sayi Min=", Min)



#Soru 2
#Girilen yaslardan yasli ve genc nufus sayisini bulma.

lst = []
q = int(input("Kac adet yas gireceksiniz:"))
for i in range(0, q):
    lst.append(int(input("Lutfen yasi giriniz:")))

gencnufus = 0
yaslinufus = 0

for i in lst:
    if (i >= 65):
        yaslinufus = yaslinufus + 1
    else:
        gencnufus = gencnufus + 1
print("Yasli Nufus:\t", yaslinufus, "\nGenc Nufus:\t", gencnufus)



#Soru 3
#"while" dongusu ile 50'ye kadar olan sayma sayilerinin karelerinin toplami.

K = 1
Toplam = 0
while K <= 50:
    Toplam = Toplam + K**2
    print("K degeri:\t", K, "\tK degerinin karesi:\t", K**2,
          "\tKareleri toplamı:\t", Toplam)
    K += 1
print("1'den 50'ye kadar olan tam sayilarin karelerinin toplami:\t", Toplam)




#Soru 4
#"for" dongusu ile 50'ye kadar olan sayma sayilerinin karelerinin toplami.

k = 1
toplam = 0
for k in range(1,51):
    toplam = toplam + k**2
    print("k degeri:\t", k, "\tk degerinin karesi:\t", k**2,
          "\tKareleri Toplami:\t", toplam)
print("1'den 50'ye kadar olan tam sayilerin karelerinin toplami:\t", toplam)



#Soru 5
#"for" dongusu ile 4 ile 50 arasindaki sayilari 5 adimlik araliklarla yazdirma.

for j in range(4, 50, 5):
    print(j, end="     ")
print()