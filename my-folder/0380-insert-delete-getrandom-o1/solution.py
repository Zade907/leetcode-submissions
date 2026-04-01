import random
class RandomizedSet:

    def __init__(self):
        self.randomSet = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.randomSet:
            self.randomSet[val] = len(self.nums)
            self.nums.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False
        idx = self.randomSet[val]
        lastElement = self.nums[-1]
        self.randomSet[lastElement] = idx
        self.nums[idx] = lastElement
        del self.randomSet[val]
        self.nums.pop()
        return True


    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
