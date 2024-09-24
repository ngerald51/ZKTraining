##Wk7
#Let φ be the transformation of a column vector into a polynomial like we discussed in class (using lagrange interpolation over the x values [0, 1, …, n] and the y values being the values in the vector).

#Use Python compute:

#$$
#\phi(c\cdot\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}) = c\cdot\phi(\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix})
#$$

#Test out a few vectors to convince yourself this is true in general.

#In English, what is the above equality stating?

##

import numpy as np

def phi(vector):
    n = len(vector) - 1
    x = np.arange(n + 1)
    
    def lagrange_poly(t):
        result = 0
        for i, yi in enumerate(vector):
            p = 1
            for j in range(n + 1):
                if i != j:
                    p *= (t - x[j]) / (x[i] - x[j])
            result += yi * p
        return result
    
    return lagrange_poly

def test_scalar_property(vector, scalar):
    phi_x = phi(vector)
    phi_cx = phi(scalar * np.array(vector))
    
    t = np.linspace(0, len(vector) - 1, 100)
    left_side = phi_cx(t)
    right_side = scalar * phi_x(t)
    
    return np.allclose(left_side, right_side)

# Test vectors
vectors = [
    [1, 2, 3],
    [0, 1, 4],
    [2, 3, 5],
    [1, 1, 1],
    [-1, 0, 1]
]

scalars = [2, 0.5, -1, 3, 10]

for vec in vectors:
    for c in scalars:
        result = test_scalar_property(vec, c)
        print(f"Vector: {vec}, Scalar: {c}, Property holds: {result}")




