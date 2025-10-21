import heapq
from Node import Node, BuildCodes


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.charactersDic = {}
        self.huffmanTreeRoot: Node = None

    def isTreeBuilt(self) -> bool:
        return self.huffmanTreeRoot is not None

    def BuildHuffmanTree(self, text: str) -> Node:
        for c in text:
            if self.charactersDic.get(c):
                self.charactersDic[c] += 1
            else:
                self.charactersDic[c] = 1

        for char, freq in self.charactersDic.items():
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

        self.huffmanTreeRoot = currentRoot
        return currentRoot

    def BuildTable(self, text: str) -> dict:
        currentRoot: Node = self.BuildHuffmanTree(text)
        codes = BuildCodes(currentRoot)
        return codes

    def Encode(self, text: str) -> str:
        codes = self.BuildTable(text)
        encodedText: str = ""
        for c in text:
            encodedText += codes[c]
        return encodedText

    def EncodeFromFileIntoFile(self, inputFilePath: str, outputFilePath: str):
        readFile = open(inputFilePath, "r")
        writeFile = open(outputFilePath, "w", encoding="utf-8")

        line = readFile.read()
        encodedResult = self.Encode(line)
        writeFile.write(encodedResult)

        readFile.close()
        writeFile.close()

    def Decode(self, encodedText: str) -> str:
        pass
        # use DFS on root to decore, very simple approach
        # check if the root is None or not before doing though

    def DecodeFromFileIntoFile(self, inputFilePath: str, outputFilePath: str):
        pass
