import math
import sympy as sp
import numpy as np

x, y = sp.symbols('x y')

#number of polynomials
n = m = 40

#Geometrical properties
a, b = 10, 10
h = 1

#mechanical properties
E = 1
nu = 0.3
G = E/(2*(1+nu))
ka = (5/6)
D = (E*h**3)/(12*(1-nu**2))

#P0
p0 = 1

#Pmn
def P(m, n):
    if m % 2 == 1 and n % 2 == 1:  # Only for odd m and n
        return (16 * p0) / (math.pi**2 * m * n)
    else:
        return 0  # Returns 0 for even m or n, according to the formula
#Wmn
def W(m, n):
    term1 = 1 + (6 * D * math.pi**2) / (5 * G * h) * ((m / a)**2 + (n / b)**2)
    denominator = (D * math.pi**4) * ((m / a)**2 + (n / b)**2)**2
    return term1 * (P(m, n) / denominator)

def deflection(x_val, y_val):
    w_sum = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            w_sum += W(i, j) * math.sin(i * math.pi * x_val / a) * math.sin(j * math.pi * y_val / b)
    return w_sum

# Calculate deflection at the center of the plate (x = a/2, y = b/2)
deflection_center = deflection(a / 2, b / 2)
deflection_center_numeric = deflection_center  # Evaluate numerically
print("Deflection at the center (x = a/2, y = b/2):", deflection_center_numeric)

# Normalized deflection at center
deflection_normalized = deflection_center_numeric / (p0 * a**4 / D)
print("Normalized deflection at the center:", deflection_normalized)
