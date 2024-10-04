def toLowerCase(text):
    return text.lower()

def removeSpaces(text):
    return text.replace(" ", "")

def Diagraph(text):
    diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        diagraph.append(text[group:i])
        group = i
    diagraph.append(text[group:])
    return diagraph

def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i + 1]:
                new_word = text[:i + 1] + 'x' + text[i + 1:]
                return FillerLetter(new_word)
    else:
        for i in range(0, k - 1, 2):
            if text[i] == text[i + 1]:
                new_word = text[:i + 1] + 'x' + text[i + 1:]
                return FillerLetter(new_word)
    return text

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = key_letters[:]
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = [compElements[i:i + 5] for i in range(0, 25, 5)]
    return matrix

def search(matrix, element):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element:
                return i, j
    return None, None

def encrypt_RowRule(matrix, e1r, e1c, e2r, e2c):
    char1 = matrix[e1r][0] if e1c == 4 else matrix[e1r][e1c + 1]
    char2 = matrix[e2r][0] if e2c == 4 else matrix[e2r][e2c + 1]
    return char1, char2

def encrypt_ColumnRule(matrix, e1r, e1c, e2r, e2c):
    char1 = matrix[0][e1c] if e1r == 4 else matrix[e1r + 1][e1c]
    char2 = matrix[0][e2c] if e2r == 4 else matrix[e2r + 1][e2c]
    return char1, char2

def encrypt_RectangleRule(matrix, e1r, e1c, e2r, e2c):
    char1 = matrix[e1r][e2c]
    char2 = matrix[e2r][e1c]
    return char1, char2

def encryptByPlayfairCipher(matrix, plainList):
    CipherText = []
    for pair in plainList:
        ele1_x, ele1_y = search(matrix, pair[0])
        ele2_x, ele2_y = search(matrix, pair[1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        CipherText.append(c1 + c2)
    return CipherText

# Main function
if _name_ == "_main_":
    text_Plain = 'instruments'
    text_Plain = removeSpaces(toLowerCase(text_Plain))
    PlainTextList = Diagraph(FillerLetter(text_Plain))
    if len(PlainTextList[-1]) != 2:
        PlainTextList[-1] = PlainTextList[-1] + 'z'

    key = "ldrp"
    print("Key text:", key)
    key = toLowerCase(key)
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Matrix = generateKeyTable(key, list1)

    print("Plain Text:", text_Plain)
    CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

    CipherText = "".join(CipherList)
    print("CipherText:", CipherText)