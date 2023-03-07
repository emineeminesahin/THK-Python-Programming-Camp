def bolme(L,kucuk,buyuk):
i=(kucuk-1) #En küçük indeks
pivot=L[buyuk]
for j in range (kucuk,buyuk):
#Eğer j elemanı pivottan küçük ise;
if L[j]<pivot:
#küçük indeks bir artırılır
i=i+1
L[i],L[j]=L[j],L[i]
L[i+1],L[buyuk]=L[buyuk],L[i+1]
return (i+1)

def hızlısırala(L,kucuk,buyuk):
if kucuk<buyuk:
pi=bolme(L,kucuk,buyuk)
hızlısırala(L,kucuk,pi-1)
hızlısırala(L,pi+1,buyuk)
L=[10,4,2,7,5,-1]
print("Hızlı Sıralanmış Liste:")
hızlısırala(L,0,len(L)-1)
for i in range(len(L)):
print(L[i])