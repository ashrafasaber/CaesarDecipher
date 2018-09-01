def choice_options():
    print("Do you want to: ")
    print("1) Specify Key")
    print("2) Bruteforce Keys")
    print("3) Quit")

    user_choice=int(input("Input 1/2:"))
    if user_choice == 1:
        decrypt_with_key()
    elif user_choice == 2:
        decrypt_without_key()
    elif user_choice == 3:
        print("Goodbye!")
        quit()

# Decrypt with key Function
def decrypt_with_key():
    ci_text = str(input("Please Input Cipher Text: "))
    key = int(input("Please Input Key: "))
    decrypt(ci_text , key)

# Decrypt
def decrypt(ci_text, key):
    #ci_text.lower()
    dec_text = ""
    for char in ci_text.lower():
        # ord(char)-97 to get the numerical order of a character in ci_text from 0-26
        # - key to shift, % 26 to put in range from 0-26
        # + 97 to get the numerical order of the character (according to python - not 0-26)



        dec_text = dec_text+chr((ord(char)-97 - key )% 26 + 97).upper()
    print(dec_text)

# Decrypt without key Function
def decrypt_without_key():
    ci_text = str(input("Please Input Cipher Text: "))

    # for loop
    for key in range(2,27):
        print("Key: " + str(key))
        decrypt(ci_text , key)

# Main Function
def main():
    choice_options()

# Running the program
main()