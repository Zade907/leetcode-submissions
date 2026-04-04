class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText.rstrip()
        cols = len(encodedText)//rows
        plainText = ""
        for start in range(cols):
            r,c = 0,start
            while r < rows and c < cols:
                plainText += encodedText[r*cols + c]
                r += 1
                c += 1
        return plainText.rstrip()

