def advanced_columnar_transposition_encrypt(text, key1, key2):
    first_pass = columnar_transposition_encrypt(text, key1)
    second_pass = columnar_transposition_encrypt(first_pass, key2)
    return second_pass

# Example usage
message = "HELLOWORLD"
key1 = "4312567"
key2 = "3142"
cipher_text = advanced_columnar_transposition_encrypt(message, key1, key2)
print("Encrypted Message:", cipher_text)
