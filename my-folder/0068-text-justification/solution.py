class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []

        currLine = []
        currLen = 0  # total characters in current line

        for word in words:
            # len(currLine) = minimum spaces needed if we add this word
            if currLen + len(word) + len(currLine) > maxWidth:

                spaces = maxWidth - currLen
                gaps = len(currLine) - 1

                # Single word line
                if gaps == 0:
                    line = currLine[0] + " " * spaces

                else:
                    evenSpace = spaces // gaps
                    extraSpace = spaces % gaps

                    line = ""

                    for i in range(gaps):
                        line += currLine[i]

                        line += " " * (
                            evenSpace +
                            (1 if i < extraSpace else 0)
                        )

                    line += currLine[-1]

                result.append(line)

                currLine = [word]
                currLen = len(word)

            else:
                currLine.append(word)
                currLen += len(word)

        # Last line (left justified)
        lastLine = " ".join(currLine)
        lastLine += " " * (maxWidth - len(lastLine))

        result.append(lastLine)

        return result
        
