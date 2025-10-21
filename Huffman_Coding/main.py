from HuffmanCoding import HuffmanCoding


def main():
    hfm: HuffmanCoding = HuffmanCoding()

    testCase: str = "AAABBBBBCCCCCCDDDDEE"

    result = hfm.Encode(testCase)
    print(result)


if __name__ == "__main__":
    main()
