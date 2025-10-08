from Tag import Tag
import re

class LZ77:
    @staticmethod
    def SearchForSequence(searchWindow: str, subString: str) -> int:
        swSize = len(searchWindow)
        subLen = len(subString)

        for i in range(swSize - 1, -1, -1):
            j = 0
            while j + i < swSize and j < subLen and searchWindow[i + j] == subString[j]:
                j += 1
                if j == subLen:
                    return i
        return -1

    @staticmethod
    def Encode(inpt: str) -> list[Tag]:
        result: list[Tag] = []
        searchWindow = ""

        startIndex: int = 0
        inptSize: int = len(inpt)

        while startIndex < inptSize:
            subLength: int = 1
            if LZ77.SearchForSequence(searchWindow, inpt[startIndex: startIndex + 1]) == -1:
                symbol: str = inpt[startIndex]
                result.append(Tag(0, 0, symbol))
                searchWindow += symbol
                startIndex += 1
                continue

            startingWordIndex: int = -1
            while startIndex + subLength <= inptSize and LZ77.SearchForSequence(searchWindow, inpt[
                                                                                              startIndex:startIndex + subLength]) != -1:
                startingWordIndex = LZ77.SearchForSequence(searchWindow, inpt[startIndex:startIndex + subLength])
                subLength += 1

            nextSymbol: str = "" if startIndex + subLength >= inptSize else inpt[(startIndex + subLength - 1)]
            result.append(Tag(len(searchWindow) - startingWordIndex, subLength - 1, nextSymbol))
            searchWindow += inpt[startIndex:startIndex + subLength]
            startIndex += subLength

        return result

    @staticmethod
    def EncodeFromFileIntoFile(inputFilePath: str, outputFilePath: str):
        readFile = open(inputFilePath, "r")
        writeFile = open(outputFilePath, "w", encoding="utf-8")
        line = readFile.readline()
        while line:
            tagsResult: list[Tag] = LZ77.Encode(line)
            TagsAsString = ""
            for tag in tagsResult:
                TagsAsString += tag.GetFormattedTag()

            writeFile.write(TagsAsString + "\n")
            line = readFile.readline()

        readFile.close()
        writeFile.close()


    '''
    returns a list of tags tuple 
    '''
    @staticmethod
    def extractTagsFromLine(line):
        pattern = r"\((\d+),(\d+),(\w?)\)"
        matches = re.findall(pattern, line)
        tags : list[Tag] = []
        for match in matches:
            tags.append(Tag(int(match[0]), int(match[1]), match[2]))
        return tags
    

    @staticmethod
    def decode(tags: list[Tag]):
        decompressed = ""
        for tag in tags:
            if tag.offset == 0 and tag.length == 0:
                decompressed += tag.nextSymbol
            
            elif tag.length > tag.offset:
                for i in range(tag.length):
                    decompressed += decompressed[-tag.offset + i]
                decompressed += tag.nextSymbol

            else:
                decompressed += decompressed[-tag.offset : -tag.offset + tag.length]
                decompressed += tag.nextSymbol

        return decompressed


    def decodeFromFileIntoFile(input_path, output_path):
        readFile = open(input_path, "r")
        writeFile = open(output_path, "w", encoding="utf-8")
        line = readFile.readline()
        while line:
            tagsFromLine = LZ77.extractTagsFromLine(line)
            decodedLine = LZ77.decode(tagsFromLine)
            writeFile.write(decodedLine + "\n")
            line = readFile.readline()

        readFile.close()
        writeFile.close()
