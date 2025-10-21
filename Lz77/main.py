from LZ77 import LZ77


def encode():
    while True:
        print("Encoding Options:")
        print("1. Encode string input")
        print("2. Encode from file")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            input_str = input("Enter string to encode: ")
            result = LZ77.Encode(input_str)
            print("\nEncoded result:")
            for tag in result:
                print(tag.GetFormattedTag(), end='')
            print("\n")
            input("Press Enter to continue...")

        elif choice == "2":
            input_path = input("Enter input file path: ")
            output_path = input("Enter output file path: ")
            try:
                LZ77.EncodeFromFileIntoFile(input_path, output_path)
                print("\nEncoding completed successfully!")
            except Exception as e:
                print(f"\nError: {str(e)}")
            input("\nPress Enter to continue...")

        elif choice == "3":
            return


def decode():
    print("Decoding Options:")
    print("1. Decode string input")
    print("2. Decode from file")
    print("3. Back to main menu")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        input_str = input("Enter the string to decode: ")
        tags = LZ77.extractTagsFromLine(input_str)
        result = LZ77.decode(tags)
        print(result)
        input("\nPress Enter to continue...")

    elif choice == "2":
        input_path = input("Enter input file paht: ")
        output_path = input("Enter output file path: ")
        try:
            LZ77.decodeFromFileIntoFile(input_path, output_path)
            print("\nEncoding completed successfully!")
        except Exception as e:
            print(f"\nError: {str(e)}")
        input("\nPress Enter to continue...")

    elif choice == "3":
        return


def main():
    while True:
        print("LZ77 Compression Tool")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            encode()
        elif choice == "2":
            decode()
        elif choice == "3":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
