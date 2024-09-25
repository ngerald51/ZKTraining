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


#### Question 2-QAP by hand
import numpy as np

# Define the interpolation points (corresponding to the number of columns in the matrices)
points = [1, 2, 3, 4, 5, 6]  # 6 points for 6 variables

# Define the matrices
A = np.array([[0,0,3,0,0,0],
               [0,0,0,0,1,0],
               [0,0,1,0,0,0]])

B = np.array([[0,0,1,0,0,0],
               [0,0,0,1,0,0],
               [0,0,0,5,0,0]])

C = np.array([[0,0,0,0,1,0],
               [0,0,0,0,0,1],
               [-3,1,1,2,0,-1]])

# Define witness vector and intermediate variables
x = 100
y = 100
v1 = 3 * x * x
v2 = v1 * y
out = 3 * x * x * y + 5 * x * y - x - 2 * y + 3
w = np.array([1, out, x, y, v1, v2])

# Function to interpolate over real numbers (Lagrange interpolation)
def interpolate_lagrange(points, values):
    # Ensure that values are the same length as points
    if len(points) != len(values):
        raise ValueError(f"Length mismatch: {len(points)} points but {len(values)} values.")
    return np.polyfit(points, values, len(points)-1)

# Interpolate each row of matrices A, B, C
A_polys = [interpolate_lagrange(points, row) for row in A]
B_polys = [interpolate_lagrange(points, row) for row in B]
C_polys = [interpolate_lagrange(points, row) for row in C]

# Interpolate witness vector
w_polys = interpolate_lagrange(points, w)

# Function to evaluate a polynomial at a given point x
def evaluate_polynomial(poly, x):
    return np.polyval(poly, x)

# Verify that A(x) * B(x) = C(x) at each interpolation point
for i in points:
    A_eval = evaluate_polynomial(A_polys, i)
    B_eval = evaluate_polynomial(B_polys, i)
    C_eval = evaluate_polynomial(C_polys, i)
    
    # Element-wise comparison and multiplication
    product = A_eval * B_eval
    
 print(f"Point {i}:")
    print(f"A_eval: {A_eval}")
    print(f"B_eval: {B_eval}")
    print(f"Product (A_eval * B_eval): {product}")
    print(f"C_eval: {C_eval}")
    
    
   
result = C_eval == product
assert result.all(), "result contains an inequality"

print("QAP verified successfully!")





