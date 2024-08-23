import hashlib
import random
from ecdsa import SECP256k1, SigningKey


# Helper functions
def sha256(message):
  """Hash a message using SHA-256."""
  return hashlib.sha256(message).digest()


# Step 1: Pick a private key
def generate_private_key():
  """Generate a random private key for use with the secp256k1 curve."""
  curve = SECP256k1
  private_key = random.randint(1, curve.order - 1)
  return private_key


# Step 2: Generate the public key
def generate_public_key(private_key):
  """Generate a public key from a private key using the secp256k1 curve."""
  curve = SECP256k1
  generator = curve.generator
  public_key = generator * private_key
  return public_key


# Step 3: Pick a message and hash it
def hash_message(message):
  """Hash a message using SHA-256."""
  return int.from_bytes(sha256(message), 'big')


# Step 4: Sign the message
def sign_message(private_key, message):
  """Sign a message using ECDSA with the secp256k1 curve."""
  curve = SECP256k1
  generator = curve.generator
  order = curve.order

  # Hash the message
  h = hash_message(message)

  # Pick a random nonce k
  k = random.randint(1, order - 1)

  # Calculate r
  r_point = generator * k
  r = r_point.x() % order

  # Calculate s
  s = ((h + r * private_key) * pow(k, -1, order)) % order

  return (r, s, h)


# Step 5: Verify the signature
def verify_signature(public_key, message, signature):
  """Verify an ECDSA signature."""
  curve = SECP256k1
  order = curve.order
  generator = curve.generator

  r, s, h = signature

  if not (1 <= r < order and 1 <= s < order):
    return False

  w = pow(s, -1, order)

  u1 = (h * w) % order
  u2 = (r * w) % order

  # Calculate the point
  point = (generator * u1) + (public_key * u2)

  return r == point.x() % order


# Example usage
message = b"Hello, Big Boy with secp256k1!"
private_key = generate_private_key()
public_key = generate_public_key(private_key)

signature = sign_message(private_key, message)

print(f"Private Key: {private_key}")
print(f"Public Key: ({public_key.x()}, {public_key.y()})")
print(f"Message: {message}")
print(f"Signature: {signature}")


# Verification
is_valid = verify_signature(public_key, message, signature)
print(f"Signature valid: {is_valid}")

# ECDSA verify tampered signature (using the curve secp256k1 + SHA3-256)
#message = b"Tampered message"
valid = verify_signature(public_key, message, signature)
print("\nMessage:", message)
print("Signature (tampered msg) valid?", valid)
