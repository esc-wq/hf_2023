def atbash_cipher(text):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            position = ord(char) - start
            reversed_position = 25 - position

            reversed_char = chr(reversed_position + start)

            result += reversed_char
        else:
            result += char

    return result

plaintext = input("Enter the text: ")

cipher_text = atbash_cipher(plaintext)

print("Original Text:", plaintext)
print("Atbash Cipher:", cipher_text)
