import numpy as np

def hill_cipher_encrypt(message, key):
    # Convert message to numerical values (A=0, B=1, ..., Z=25)
    message = message.upper().replace(" ", "")
    message_vector = [ord(char) - ord('A') for char in message]
    
    # Reshape the message to match the key matrix dimensions
    n = len(key)
    while len(message_vector) % n != 0:
        message_vector.append(ord('X') - ord('A'))  # Padding with 'X'
    
    message_vector = np.array(message_vector).reshape(-1, n)
    key = np.array(key)
    
    # Encryption: Multiply message vector by key matrix
    cipher_vector = np.dot(message_vector, key) % 26
    
    # Convert back to letters
    cipher_text = ''.join([chr(int(num) + ord('A')) for row in cipher_vector for num in row])
    return cipher_text

# Example usage
key_matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]  # Example 3x3 key matrix
message = "HELLO"
cipher_text = hill_cipher_encrypt(message, key_matrix)
print("Encrypted Message:", cipher_text)
