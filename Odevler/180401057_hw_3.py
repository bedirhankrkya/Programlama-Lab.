import sympy as sym
from sympy import Symbol
from sympy import pprint
import matplotlib.pyplot as plot

p=Symbol('p')
x=Symbol('x')
n=Symbol('n')

my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
#pprint(my_f_3_part_0)
#print("\n")

my_f_3_part_1=p**x
#pprint(my_f_3_part_1)
#print("\n")

my_f_3_part_2=(1-p)**(n-x)
#pprint(my_f_3_part_2)
#print("\n")

my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2
#pprint(my_f_3)
#print("\n")
sym.plot(my_f_3.subs({p:0.5,n:25}),(x,0,25),title='Binomal Distribution')

x_values, y_values = [], []
for value in range(26):
    y = my_f_3.subs({p:0.5, n:25, x:value}).evalf()
    print(value,y)
    
for value in range(0, 26):
    y = my_f_3.subs({p:0.5, n:25, x:value})
    x_values.append(value)
    y_values.append(y)

plot.plot(x_values, y_values)
plot.show()