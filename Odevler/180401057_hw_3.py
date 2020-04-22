import sympy as sym
from sympy import Symbol
from sympy import pprint
import matplotlib.pyplot as plot

p=Symbol('p')
x=Symbol('x')
n=Symbol('n')

my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))#formülümüzün ilk kısmı
#pprint(my_f_3_part_0)
#print("\n")

my_f_3_part_1=p**x#formülümüzün 2. kısmı
#pprint(my_f_3_part_1)
#print("\n")

my_f_3_part_2=(1-p)**(n-x)#formülümüzün 3. kısmı
#pprint(my_f_3_part_2)
#print("\n")

my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2#en son olarak formülümüzün kısımlarını birleştirerek bir bütün haline getirdik.
#pprint(my_f_3)
#print("\n")

#sympy ile çizdirdiğimiz grafik
sym.plot(my_f_3.subs({p:0.5,n:25}),(x,0,25),title='Binomal Distribution')

#matplotlib ile çizdirdiğimiz grafik
x_values, y_values = [], []
#bu for dongusunde x değeri için y değerlerini gösteriyoruz.
for value in range(26):
    y = my_f_3.subs({p:0.5, n:25, x:value}).evalf()
    print(value,y)
    
for value in range(0, 26):
    y = my_f_3.subs({p:0.5, n:25, x:value})#x'e karşılık gelen y değerlerini buluyoruz.
    x_values.append(value)
    y_values.append(y)

plot.plot(x_values, y_values)
plot.show()