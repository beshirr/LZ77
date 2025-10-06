# (offset, length, nextSymbol)

class Tag:
    def __init__(self, offset: int, length: int, nextSymbol: str):
        self.offset = offset
        self.length = length
        self.nextSymbol = nextSymbol

    def GetFormattedTag(self) -> str:
        return f"({self.offset},{self.length},{self.nextSymbol})"
