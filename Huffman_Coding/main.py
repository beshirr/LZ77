from HuffmanCoding import HuffmanCoding


def encode(hfm: HuffmanCoding):
    while True:
        print("Encoding Options:")
        print("1. Encode string input")
        print("2. Encode from file")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            input_str = input("Enter string to encode: ")
            result = hfm.Encode(input_str)  # will internally construct the table
            print("\nEncoded result:")
            print(result)
            print("\n")
            input("Press Enter to continue...")

        elif choice == "2":
            input_path = input("Enter input file path: ")
            output_path = input("Enter output file path: ")
            hfm.EncodeFromFileIntoFile(input_path, output_path)
            print("\nEncoding completed successfully!")
            input("\nPress Enter to continue...")

        elif choice == "3":
            return


def decode(hfm: HuffmanCoding):
    print("Decoding Options:")
    print("1. Decode string input")
    print("2. Decode from file")
    print("3. Back to main menu")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        input_str = input("Enter the string to decode: ")
        result = hfm.Decode(input_str)
        print(result)
        input("\nPress Enter to continue...")

    elif choice == "2":
        input_path = input("Enter input file paht: ")
        output_path = input("Enter output file path: ")
        try:
            hfm.DecodeFromFileIntoFile(input_path, output_path)
            print("\nEncoding completed successfully!")
        except Exception as e:
            print(f"\nError: {str(e)}")
        input("\nPress Enter to continue...")

    elif choice == "3":
        return


def main():
    hfm: HuffmanCoding = HuffmanCoding()
    while True:
        print("Huffman Compression Tool")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            encode(hfm)
        elif choice == "2":
            decode(hfm)
        elif choice == "3":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
