class Province:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color
        self.isNew = False

        self.pixels = []
        self.xSum = 0
        self.ySum = 0
        self.count = 0

    def addPixel(self, pixel):
        self.pixels.append(pixel)
        self.xSum += pixel.x
        self.ySum += pixel.y
        self.count += 1

    def calculateAverageX(self):
        return round(self.xSum / self.count, 3)

    def calculateAverageY(self):
        return round(self.ySum / self.count, 3)