import sympy as sp
from sympy import symbols, Poly
#Question 6

# Define the variable
x = symbols('x')

# Define the polynomials
p = Poly(52*x**2 + 24*x + 61, x)
q = Poly(40*x**2 + 40*x + 58, x)

# Find the roots of p(x)
roots_p = sp.solve(p, x)
print("Roots of p(x):", roots_p)

# Find the roots of q(x)
roots_q = sp.solve(q, x)
print("Roots of q(x):", roots_q)

### End of Code sample


from galois import GF
# Question 7
# Define the finite field GF(71)
GF71 = GF(71)

# Define the points
x1, y1 = GF71(10), GF71(15)
x2, y2 = GF71(23), GF71(29)

# Calculate the slope a
inverse_13 = GF71(13).inverse()
a = GF71(14) * inverse_13

# Calculate the y-intercept b
b = y1 - a * x1

# Define the function f(x) = ax + b
def f(x):
    return a * x + b

# Verify the solution
assert f(GF71(10)) == GF71(15)
assert f(GF71(23)) == GF71(29)

print(f"Slope (a): {a}")
print(f"Y-intercept (b): {b}")
print(f"f(x) = {a}x + {b}")


