def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    direction = False
    row, col = 0, 0
    
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            direction = not direction
        rail[row][col] = text[i]
        col += 1
        row += 1 if direction else -1
    
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

# Example usage
message = "HELLO WORLD"
key = 3
cipher_text = rail_fence_encrypt(message, key)
print("Encrypted Message:", cipher_text)
