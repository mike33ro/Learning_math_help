
'''
This project take random numbers and prints them to console in order to help small childrens
to learn sum .
'''
from random import randint
import time
from datetime import datetime

Concurent=input('State your name > ')
p=0 #points

i=int(input('Haw many tries ? ')) #try
t=time.time()
f=i

while f >0 :

    a=randint(0,10)
    b=randint(0,10)
    T=a+b
    R=int(input(f'{a} + {b} = '))
    if R== T :
        print (' Bravo ')
        p=p+1
    else:
        print('Try again !')
    #print (f'Hurry the answer was ... {T}')
    f=f-1

t=round(time.time()-t,0)
data=time.strftime("%Y-%m-%d %H:%M")
conc_place=(f'{Concurent}  did the test in {t} seconds and  done  {p} points from top {i}  {data} ')
print(f' {Concurent}  did the test in {t} seconds and  done  {p} points from top {i}')

fis_concurenti=open('Concurenti.txt','a')
fis_concurenti.write(conc_place+'\n')
#fis_concurenti.write('\n')
fis_concurenti.close()
