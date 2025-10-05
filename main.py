# file handlers (if needed)


# Encoding
def encode():
    pass


# Decoding 
def decode():
    pass


while (True):
    choice = input("Encode (1) \nDecode (2) \nExit(0) \n-> ")
    if choice == '0':
        break
    elif choice == '1':
        encode()
    elif choice == '2':
        decode()
    else:
        print("Invalid input")

