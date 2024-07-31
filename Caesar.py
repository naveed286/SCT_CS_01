def encrypt(text, shift):
    result = ""  # This will store the encrypted message
    
    for char in text:
        if char.isupper():  # Check if the character is an uppercase letter
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():  # Check if the character is a lowercase letter
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # If it's not a letter, just add it as is
    
    return result

def decrypt(text, shift):
    result = ""  # This will store the decrypted message
    
    for char in text:
        if char.isupper():  # Check if the character is an uppercase letter
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():  # Check if the character is a lowercase letter
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char  # If it's not a letter, just add it as is
    
    return result

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'e':
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted message: {encrypted_text}")
    elif choice == 'd':
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted message: {decrypted_text}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()