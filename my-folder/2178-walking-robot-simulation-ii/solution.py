class Robot:

    def __init__(self, width: int, height: int):
        self.pos = [0,0]
        self.direction = [[1,0],[0,1],[-1,0],[0,-1]] #E N W S
        self.directions = ["East", "North", "West","South"]
        self.curDir = 0
        self.maxWidth = width
        self.maxHeight = height

        self.perimeter = 2*(width + height) - 4

    def step(self, num: int) -> None:
        num %= self.perimeter

        if num == 0 and self.pos == [0,0]:
            self.curDir = 3
            return

        x, y = self.pos

        for _ in range(num):
            dx, dy = self.direction[self.curDir]
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < self.maxWidth and 0 <= ny < self.maxHeight):
                self.curDir = (self.curDir + 1) % 4
                dx, dy = self.direction[self.curDir]
                nx, ny = x + dx, y + dy

            x, y = nx, ny 
        self.pos = [x,y]

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.directions[self.curDir]
