from DES import DES_encryption
from decrypt import decrypt

key = "133457799BBCDEE1"

print("#############WELCOME#############")
choice = "y"
while choice == "y":
    message = input("Enter the plain text message\n")
    encrypt_message = DES_encryption(message,key)
    print("Your Message is:")
    print(message)
    print("The Encrypted Message is :")
    print(encrypt_message)
    print("Do you want to decrypt the message?")
    select = input("y = yes     n = no\n")
    if select == "y":
        decrypt_message = decrypt(encrypt_message,key)
        print("The Decrypted message is:")
        print(decrypt_message)
    print("Do you want to do it again?")
    choice = input("y = yes    N = no\n")



