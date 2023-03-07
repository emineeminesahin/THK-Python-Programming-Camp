#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Fibonacci sayıları şu şekilde tanımlanır: 
#fib (0) = 1, fib (1) =1, …….
#fib (n) = fib (n - 1) + fib (n - 2) 
#=> fib(2)=fib(1)+fib(0)=1+1=3

def fib(n):
    if n<=1:
        
        return 1
    else:
       
        return (fib(n-1)+fib(n-2))
m=int(input("Fibonacci hesaplanacak sayı giriniz"))

if m<=0:
    print("Lütfen Pozitif Bir Sayı Giriniz")
else:
    print ("Fibonacci Dizisi Çıktısı")
    for i in range(m+1):
        print(fib(i),end=" ")    

    


# In[1]:


def fib(i, j):

    if (i, j) in {(0, 0), (1, 0), (1, 1), (2, 1)}:
        return 1
    elif j >= 2:
        return fib(i - 1, j - 1) + fib(i - 2, j - 2)
    else:
        return fib(i - 1, j) + fib(i - 2, j)
 
m=int(input("Fibonacci hesaplanacak sayı giriniz:"))

if m<=0:
    print("lütfen pozitif bir sayı giriniz")
else:
    print("Fibonacci dizisi çıktısı")
    for i in range(m+1):
        for j in range(i + 1):
            print(fib(i, j), end=' ')
        print()


# In[ ]:




