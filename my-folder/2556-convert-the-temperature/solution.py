class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        #float list1 = []
        kelvin = celsius + 273.15
        fahrenheit = (celsius*1.80) + 32
        return kelvin,fahrenheit

