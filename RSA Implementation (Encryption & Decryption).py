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

# Function to encrypt a message (number or character)
def encrypt(message, public_key):
    e, n = public_key
    if isinstance(message, str):  # Encrypting a single alphabet
        message = ord(message)  # Convert to ASCII
    return pow(message, e, n)  # Encryption formula C = (M^e) % n

# Function to decrypt a message
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_message = pow(ciphertext, d, n)  # Decryption formula M = (C^d) % n
    if 65 <= decrypted_message <= 122:  # Convert back to character if it's an ASCII letter
        return chr(decrypted_message)
    return decrypted_message

# Main execution
public_key, private_key = generate_rsa_keys()

# Encrypting a number (e.g., 42)
num = 42
encrypted_num = encrypt(num, public_key)
decrypted_num = decrypt(encrypted_num, private_key)

# Encrypting a letter (e.g., 'A')
letter = 'A'
encrypted_letter = encrypt(letter, public_key)
decrypted_letter = decrypt(encrypted_letter, private_key)

# Display results
print(f"Public Key: {public_key}")  # (e, n)
print(f"Private Key: {private_key}")  # (d, n) 

print(f"\nOriginal Number: {num}")
print(f"Encrypted Number: {encrypted_num}")
print(f"Decrypted Number: {decrypted_num}")

print(f"\nOriginal Letter: '{letter}'")
print(f"Encrypted Letter: {encrypted_letter}")
print(f"Decrypted Letter: '{decrypted_letter}'")
