import random
import math
from sympy import isprime, mod_inverse

# Function to generate a random prime number
def generate_prime():
    while True:
        num = random.randint(50, 200)  # Choose a random number in a small range
        if isprime(num):  # Ensure it's prime
            return num

# Function to generate RSA keys
def generate_rsa_keys():
    p = generate_prime()
    q = generate_prime()
    
    while p == q:  # Ensure p and q are different
        q = generate_prime()
    
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:  # Ensure e is coprime to phi
        e = random.randint(2, phi - 1)

    # Compute d such that (d * e) % phi = 1
    d = mod_inverse(e, phi)

    # Return Public and Private Keys
    return (e, n), (d, n)

# Generate RSA keys
public_key, private_key = generate_rsa_keys()

# Display the generated keys
print(f"Public Key: {public_key}")  # (e, n)
print(f"Private Key: {private_key}")  # (d, n)
