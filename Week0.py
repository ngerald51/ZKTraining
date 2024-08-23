Prep ZK Math in Python

#Modular Arithmetic
#pow(n,positive/negative ,mod)

x = pow(15, -1, 1223) #Prints modular inverese of 15 MOD 1223
y= pow(2, 10, 1000)
print (x)
print (y)
assert 15 * x % 1223 == 1



#Point/ Scalar Operations
vector1 = np.array([1,2])
vector2 = np.array([5,6])
scalar1 = 3
scalar2 = 10


def linearCombination(A, B, a, b):
    A = np.array(A)
    B = np.array(B)
    return a * A + b * B

print (linearCombination(vector1, vector2, scalar1, scalar2))

assert (np.array([53, 66]) == linearCombination(vector1, vector2, scalar1, scalar2)).all()


##Matrix Operations
import numpy as np

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,1,1],[2,2,2],[3,3,3]]
C = [[2,3,4],[6,7,8],[10,11,12]]

def add_arrays(A, B):
    A = np.array(A)
    B = np.array(B)
    return A + B
    
assert (add_arrays(A, B) == np.array(C)).all()


def matrix_multiply(A, B):
    A = np.array(A)
    B = np.array(B)
    return np.dot(A, B)

def element_wise_multiply(A, B):
    A = np.array(A)
    B = np.array(B)
    return A * B


def dot_product(A, B):
    A = np.array(A)
    B = np.array(B)
    return np.dot(A, B)


print (dot_product(A, B))

