class Solution:
    def convertDateToBinary(self, date: str) -> str:
        day = date.split("-")
        year = bin(int(day[0]))
        month = bin(int(day[1]))
        day = bin(int(day[2]))
        year = year.replace("0b","")
        month = month.replace("0b","")
        day = day.replace("0b","")
        
        string = (f"{year}-{month}-{day}")
        return string
