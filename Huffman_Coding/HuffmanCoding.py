import heapq
import ast
from Node import Node, BuildCodes


class HuffmanCoding:
    def __init__(self):
        self.heap = []

    def BuildHuffmanTree(self, charactersDic: dict) -> Node:
        for char, freq in charactersDic.items():
            heapq.heappush(self.heap, (freq, char))

        currentRoot: Node = None
        currentLeafs: int = 0  # 0 or odd and there at least 2 => take two | even or one elment left => take one
        while len(self.heap) >= 1:
            if currentLeafs == 0 or currentLeafs % 2 != 0 and len(self.heap) >= 2:
                left = heapq.heappop(self.heap)
                right = heapq.heappop(self.heap)
                leftNode: Node = Node(left[0], str(left[1]))
                rightNode: Node = Node(right[0], str(right[1]))

                if currentRoot is None:
                    currentRoot = Node(left[0] + right[0])
                    currentRoot.left = leftNode
                    currentRoot.right = rightNode

                else:
                    newRootRightChild = Node(left[0] + right[0])
                    newRootRightChild.left = leftNode
                    newRootRightChild.right = rightNode
                    newRoot = Node(newRootRightChild.value + currentRoot.value)
                    newRoot.left = currentRoot
                    newRoot.right = newRootRightChild
                    currentRoot = newRoot
                currentLeafs += 2

            else:
                nextLeafValue = heapq.heappop(self.heap)
                nextLeaf = Node(nextLeafValue[0], str(nextLeafValue[1]))
                newRoot = Node(currentRoot.value + nextLeafValue[0])
                newRoot.left = currentRoot
                newRoot.right = nextLeaf
                currentRoot = newRoot
                currentLeafs += 1

        return currentRoot

    def BuildFrequencyTable(self, text: str) -> dict:
        charactersDic: dict = {}
        for c in text:
            if c in charactersDic:
                charactersDic[c] += 1
            else:
                charactersDic[c] = 1

        return charactersDic

    def Encode(self, text: str) -> (str, dict):
        freqTable = self.BuildFrequencyTable(text)
        currentRoot: Node = self.BuildHuffmanTree(freqTable)
        codes = BuildCodes(currentRoot)
        encodedText: str = ""
        for c in text:
            encodedText += codes[c]
        return encodedText, freqTable

    def EncodeFromFileIntoFile(self, inputFilePath: str, outputFilePath: str):
        readFile = open(inputFilePath, "r")
        writeFile = open(outputFilePath, "w", encoding="utf-8")

        line = readFile.read()
        encodedResult = self.Encode(line)

        writeFile.write(str(encodedResult[1]) + "\n")
        writeFile.write(encodedResult[0])

        readFile.close()
        writeFile.close()

    def Decode(self, freqTable: dict, encoded_str: str) -> str:
        binaryTreeRoot: Node = self.BuildHuffmanTree(freqTable)  
        if binaryTreeRoot is None:
            return ""

        if binaryTreeRoot.left is None and binaryTreeRoot.right is None:
            total = sum(freqTable.values())
            return binaryTreeRoot.character * total

        result_chars = []
        node = binaryTreeRoot

        for bit in encoded_str:
            if bit == "0":
                node = node.left
            else:
                node = node.right

            if node.left is None and node.right is None:
                result_chars.append(node.character)
                node = binaryTreeRoot

        return "".join(result_chars)

    def DecodeFromFileIntoFile(self, inputFilePath: str, outputFilePath: str):
        readFile = open(inputFilePath, 'r')
        writeFile = open(outputFilePath, 'w')
        line = readFile.readline()
        freq_dict = ast.literal_eval(line)
        line = readFile.readline()
        decoded = self.Decode(freq_dict, line)
        writeFile.write(decoded)
        readFile.close()
        writeFile.close()


