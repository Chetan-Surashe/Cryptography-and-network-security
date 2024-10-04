def columnar_transposition_encrypt(text, key):
    matrix = [text[i:i+len(key)] for i in range(0, len(text), len(key))]
    cipher_text = ""
    for num in sorted(list(key)):
        idx = key.index(num)
        for row in matrix:
            if idx < len(row):
                cipher_text += row[idx]
    return cipher_text

# Example usage
message = "HELLOWORLD"
key = "4312567"
cipher_text = columnar_transposition_encrypt(message, key)
print("Encrypted Message:", cipher_text)
