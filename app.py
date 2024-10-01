import math
import sympy as sp
import numpy as np

x, y = sp.symbols('x y')

m, n = 1, 1

a, b = 8, 8
h = 1

E = 1
nu = 0.3
G = E/(2*(1+nu))
k = (5/6)**0.5
D = (E*h**3)/(12*(1-nu**2))

#P11
P11 = (4/(a*b))*( sp.integrate(sp.sin( (sp.pi*x)/(a) ), (x, 0, a)) * sp.integrate(sp.sin( (sp.pi*y)/b ), (y, 0, b)) )
print(P11)

