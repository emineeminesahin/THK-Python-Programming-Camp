#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Binary Search - İkili Arama
def barama(L,a,l,h):
    if h>=l:
        orta=(l+h)//2
        if L[orta]==a:
            return orta
        elif L[orta]<a:
            return barama(L,a,orta+1,h)
        else:
            return barama(L,a,l,orta-1)
    else:
        return -1
L=[2,3,4,10,40]
a=10
#barama(Liste,aranacakdeğer,başlangıçindeksi,bitişindeksi) şekilde olacak
#fonksiyon ana programdan ilk defa çalırıldığında başlangıçindeks değeri sıfırdır
#bitiş değeri de listenin en son elemanı olacağı için, len(L)-1 olarak alınır
sonuc=barama(L,a,0,len(L)-1)
if sonuc!=-1:
    print ("aradığınız değer listede mevcut")
else:
    print ("aradığınız değer listede mevcut değil")
        
        
    


# In[ ]:




