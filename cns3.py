def generate_playfair_matrix(key):
    # Prepare the matrix with unique letters from the key and the rest of the alphabet
    key = key.upper().replace("J", "I")  # Replace J with I
    matrix = []
    used_letters = set()

    for char in key:
        if char not in used_letters and char.isalpha():
            matrix.append(char)
            used_letters.add(char)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in used_letters:
            matrix.append(char)
            used_letters.add(char)
    
    # Create 5x5 playfair matrix
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    
    # Process plaintext into digraphs
    digraphs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1:
            digraphs.append(plaintext[i] + 'X')  # Padding last single character
            i += 1
        elif plaintext[i] == plaintext[i + 1]:
            digraphs.append(plaintext[i] + 'X')  # Insert X between repeating letters
            i += 1
        else:
            digraphs.append(plaintext[i:i+2])
            i += 2

    cipher_text = ""
    
    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        
        if row1 == row2:
            # Same row: replace with letter to the right (circular)
            cipher_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            # Same column: replace with letter below (circular)
            cipher_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            # Rectangle swap: replace with letters on the same row but opposite corners
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    
    return cipher_text

# Example usage
key = "ldrp"
plaintext = "HELLO WORLD"
cipher_text = playfair_encrypt(plaintext, key)
print("Encrypted Message:", cipher_text)
