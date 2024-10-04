def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa_encrypt_decrypt():
    # Step 1: Choose two prime numbers
    p = 61
    q = 53
    
    # Step 2: Calculate n and φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Step 3: Choose public key 'e'
    e = 17
    while gcd(e, phi) != 1:
        e += 1
    
    # Step 4: Calculate private key 'd'
    d = mod_inverse(e, phi)
    
    # Step 5: Encryption and Decryption
    message = 65  # Message as a number
    cipher = pow(message, e, n)  # Encryption
    decrypted_message = pow(cipher, d, n)  # Decryption
    
    return cipher, decrypted_message

# Example usage
cipher, decrypted_message = rsa_encrypt_decrypt()
print("Encrypted Message:", cipher)
print("Decrypted Message:", decrypted_message)
