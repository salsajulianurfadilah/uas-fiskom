import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (x**2)*np.exp(-x*+5)
#Input Variabel
a = input('Nilai batas bawah integral =');
b = input('Nilai batas atas integral = ');
n = input('Masukkan Jumlah Iterasi = ');

#Trapezoid
def trapezoid(f,a,b,n):
    h=(b-a)/n
    sum=0.0
    for i in range(1,n):
        x=a+i*h
        sum=sum+f(x)
    integral =(h/2)*(f(a)+2*sum+f(b))
    return integral 


xp = np.linspace(a,b)
plt.plot(xp, func(xp))

for i in range (n):
    plt.bar(x[i], func(x[i]), align='edge', width=0.000001, color = 'gray', edgecolor = 'red')
    plt.fill_between(x,func(x), color = 'yellow')
    plt.show()
