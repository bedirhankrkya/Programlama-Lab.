from sympy import Symbol, Limit
from sympy import pprint
from sympy import Symbol, exp, sqrt, pi, Integral

#                      LESSON 1

#               S(t1+delta) + S(t1)
#               ___________________
#                     delta
#Kodlarımızı bu formüle göre yazıyoruz.

t=Symbol('t') #t'nin bir sembol olduğunu söylüyoruz
St= 5*t**2 + 2*t+8
t1 = Symbol('t1')#t1'in bir sembol olduğunu söylüyoruz
delta_t = Symbol('delta_t')#delta_t'nin bir sembol olduğunu söylüyoruz

St1 = St.subs({t: t1})  #t gördüğümüz yere t1 yazıyoruz
St1_delta = St.subs({t: t1 + delta_t})#t gördüğümüz yere t1+delta yazıyoruz

pprint(Limit((St1_delta-St1)/delta_t, delta_t, 0).doit())#delta_t yaklaşırken 0'a limit aldık

print("<--------------------------------->")

#                   LESSON2
#bir pdf fonksiyonu üzerinden integral alarak olasılığı bulma

#          -(x-10)**2
#             _____
#     1         2
#    ___     *e
#(2*pi)**1/2

#formülüne göre yazdığımız kod.

x = Symbol('x')# x'in bir sembol olduğunu söylüyoruz
p = exp(-(x - 10)**2/2)/sqrt(2*pi)
pprint(Integral(p, (x, 11, 12)).doit().evalf())#x'e göre integral alıyoruz aralıklarda 10 ve 11
