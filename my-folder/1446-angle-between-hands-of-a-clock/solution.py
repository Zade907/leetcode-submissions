class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteHandDegree = minutes * 6
        hourHandBasic = hour * 30
        hourHandFinal = (hourHandBasic + (minutes/60) * 30) % 360
        res = max(minuteHandDegree, hourHandFinal) - min(minuteHandDegree, hourHandFinal)
        return min(res, 360 - res)
