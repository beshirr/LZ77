import heapq
from Node import Node, BuildCodes


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.charactersDic = {}

    def Encode(self, text: str) -> dict:
        for c in text:
            if self.charactersDic.get(c):
                self.charactersDic[c] += 1
            else:
                self.charactersDic[c] = 1

        for kv in self.charactersDic.items():
            heapq.heappush(self.heap, (kv[1], kv[0]))  # (frequency, (character, frequency))

        currentRoot: Node = None
        currentLeafs: int = 0  # 0 or odd take two | even take one
        while len(self.heap) > 1:
            if currentLeafs == 0 or currentLeafs % 2 != 0:
                left = heapq.heappop(self.heap)
                right = heapq.heappop(self.heap)
                leftNode: Node = Node(left[0], left[1])
                rightNode: Node = Node(right[0], right[1])

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
                nextLeaf = Node(nextLeafValue, nextLeafValue[1])
                newRoot = Node(currentRoot.value + nextLeafValue[0])
                newRoot.left = currentRoot
                newRoot.right = nextLeaf
                currentRoot = newRoot
                currentLeafs += 1

        codes = BuildCodes(currentRoot)
        return codes
