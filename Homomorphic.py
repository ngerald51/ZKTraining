#Homomorphic Experiments 

def verify_homomorphic_property(x, y, g, p):
    # Calculate g^(2x) and g^(8y) modulo p
    gx_2 = pow(g, 2 * x, p)
    gy_8 = pow(g, 8 * y, p)
    
    # Compute the product (homomorphic operation)
    product = (gx_2 * gy_8) % p
    
    # Calculate g^7944 modulo p
    g_7944 = pow(g, 7944, p)
    
    # Verify if the product equals g^7944 modulo p
    is_homomorphic = product == g_7944
    
    return is_homomorphic, gx_2, gy_8, product, g_7944

# Example values
x = 2
y = 2
g = 2  # Base for exponentiation
p = 8191  # Modulus

# Check the homomorphic property
is_homomorphic, gx_2, gy_8, product, g_7944 = verify_homomorphic_property(x, y, g, p)

print(f"g^(2x) mod p = {gx_2}")
print(f"g^(8y) mod p = {gy_8}")
print(f"(g^(2x) * g^(8y)) mod p = {product}")
print(f"g^7944 mod p = {g_7944}")
print(f"Is the operation homomorphic? {is_homomorphic}")

### End of Code sample


# Function to check if 2x + 8y = 7944 can be expressed modulo m
def check_homomorphism(x, y, target, modulus):
    # Left side of the equation under modulo
    left_side = (2 * x + 8 * y) % modulus

    # Right side (target) under modulo
    right_side = target % modulus

    # Check if both sides are equivalent modulo m
    is_homomorphic = left_side == right_side

    return is_homomorphic

# Example usage
x = 123  # Some example values for x
y = 456  # Some example values for y
target = 7944
modulus = 7944  # Choose an arbitrary modulus

# Check homomorphism
is_homomorphic = check_homomorphism(x, y, target, modulus)

print(f"Is 2x + 8y = 7944 homomorphic modulo {modulus}? {is_homomorphic}")

####

def verify_homomorphic_property(a, b, g, p):
    # Calculate g^a, g^b, and g^c modulo p
    ga = pow(g, a, p)
    gb = pow(g, b, p)
    gc = pow(g, a + b, p)

    # Calculate the product of g^a and g^b modulo p
    product = (ga * gb) % p

    # Verify if the product is equal to g^(a+b) modulo p
    is_homomorphic = product == gc

    return is_homomorphic, ga, gb, gc, product

# Example values
a = 5
b = 3
g = 2
p = 13

is_homomorphic, ga, gb, gc, product = verify_homomorphic_property(a, b, g, p)

print(f"g^a mod p = {ga}")
print(f"g^b mod p = {gb}")
print(f"g^(a+b) mod p = {gc}")
print(f"(g^a * g^b) mod p = {product}")
print(f"Is the operation homomorphic? {is_homomorphic}")
### End of Code Sample




import random

def generate_large_prime(bits=1024):
    from Crypto.Util.number import getPrime
    return getPrime(bits)

def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)

def verify_proof(g, h, p, x, y, t1, t2, c, s, z):
    left_side = mod_exp(g, s, p)
    right_side = (t1 * mod_exp(h, z, p) * mod_exp(g, (2*x + 8*y)*c, p)) % p
    return left_side == right_side

# Parameters
p = generate_large_prime()
g = 2  # We can choose any primitive root modulo p
n = random.randint(1, p-2)
h = mod_exp(g, n, p)

# Known solution (for demonstration purposes)
x = 1234
y = 789

# Prover's steps
r = random.randint(1, p-2)
t1 = mod_exp(g, r, p)
t2 = mod_exp(h, r, p)

# Verifier's steps
c = random.randint(1, p-2)

# Prover's steps (continued)
s = (r + c*n) % (p-1)
z = (c * 7944) % (p-1)

# Verification
is_valid_proof = verify_proof(g, h, p, x, y, t1, t2, c, s, z)
print("Is the proof valid?", is_valid_proof)

##End of Code Sample
