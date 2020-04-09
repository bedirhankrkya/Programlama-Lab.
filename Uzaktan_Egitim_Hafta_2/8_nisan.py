from sympy import Symbol
from sympy import factor
from sympy import expand
from sympy import pprint
#matematiksel işlemlerini bizim günlük hayatta kullandığımız şekilde gösterir.
from sympy import *
import sympy.plotting as syp
import sympy as sym
import matplotlib.pyplot as plt
#Symbol('x') x e sembolık bir x değeri veriyoruz
x= Symbol('x')
y=Symbol('y')
p=x*(x+x)
print(p)
print("<--------------->")
p=(x+2)*(x+3)
print(p)
print("<--------------->")
#factor ile çarpanlara ayırıyoruz
expr = x*2-y*2
print(factor(expr))
print("<--------------->")
#expand ile çarpanlara ayrılmış ifadeyi tekrar çarpılmış haline geri çeviriyoruz.
factors=factor(expr)
print(expand(factors))
expand=expand(factors)
print("<--------------->")
print(factors,expand)
print("<--------------->")
expr2 = x*3+3*x*2*y+3*x*y*2+y*3
factors=factor(expr2)
pprint(factors)
#pprint(expand(factors))

print("<--------------->")
#bir seri oluşturuyoruz
x = Symbol('x')
series = x
n = 5
for i in range(2, n+1):
    series = series + (x**i) / i
pprint(series)

print("<--------------->")
#değişkenlere değer verip x-y ifadelerine subs taki değerleri veriyoruz.

expr = x*x + x*y + y*x + y*y
print("ifadenin sonucu = ", expr.subs({x:5, y:3}))

print("<--------------->")
#x'e değer vererek cevabı bulduk.
x = Symbol('X')
series = x
n = 5
x_value = 10
for i in range(2, n+1):
    series = series + (x**i) / i
series_value = series.subs({x:x_value})

pprint(series_value)

print("<--------------->")
#gauss fonksiyonunu formülle oluşturma
sigma = Symbol('sigma')
mu = Symbol('mu')
x = Symbol('X')

pprint(2*sym.pi*sigma)
part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part_2 = sym.exp(-1*((x-mu)*2) / (2*sigma*2))


print("<--------------->")
gauss_function = part_1*part_2
pprint(gauss_function)

print("<--------------->")
#bu fonksiyondaki sigma ve mu ifadelerine plot ile değer veriyoruz ve grafik haline getiriyoruz.Title ile de grafiğe isim veriyoruz.
sym.plot(gauss_function.subs({mu:1, sigma:3}), (x, -100, 50), title='gauss_distribution')

print("<--------------->")

#İşlemi for döngüsüyle yaparsak(evalf ile matematiksel hale getirdik)
for value in range(-5, 5):
    y = gauss_function.subs({mu:1, sigma:3, x:value}).evalf()
    print(value, y)

print("<--------------->")

#burada da plot ile grafik haline getirdik

x__values = []
y__values = []
for value in range(-100, 100):
    y = gauss_function.subs({mu:1, sigma:3, x:value}).evalf()
    x__values.append(value)
    y__values.append(y)

plt.plot(x__values, y__values)#grafiğe  atama yaptık
plt.show()#grafiği konsolda gösterdik