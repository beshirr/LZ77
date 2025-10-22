from HuffmanCoding import HuffmanCoding
import ast


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
            print("\nEncoded result: ", result[0])
            print(f"Frequency Table: {result[1]}")
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

    user_input = input("Enter character frequencies (e.g. {'a': 5, 'b': 2}): ")

    freq_dict = {}
    try:
        freq_dict = ast.literal_eval(user_input)
    except (SyntaxError, ValueError):
        print("Invalid input! Please enter a valid dictionary.")
        return

    if choice == "1":
        encoded_str = input("Enter encoded string to decode: ")
        result = hfm.Decode(freq_dict, encoded_str)
        print(result)
        input("\nPress Enter to continue...")

    elif choice == "2":
        input_path = input("Enter input file paht: ")
        output_path = input("Enter output file path: ")
        try:
            hfm.DecodeFromFileIntoFile(freq_dict, input_path, output_path)
            print("\nDecoding completed successfully!")
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
