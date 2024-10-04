import random

def diffie_hellman(p, g, private_key_A, private_key_B):
    A = pow(g, private_key_A, p)
    B = pow(g, private_key_B, p)
    
    shared_secret_A = pow(B, private_key_A, p)
    shared_secret_B = pow(A, private_key_B, p)
    
    return shared_secret_A, shared_secret_B

# Example usage
p = 23  # Public prime number
g = 5   # Public base
private_key_A = random.randint(1, p-1)
private_key_B = random.randint(1, p-1)

shared_secret_A, shared_secret_B = diffie_hellman(p, g, private_key_A, private_key_B)
print("Shared Secret A:", shared_secret_A)
print("Shared Secret B:", shared_secret_B)
