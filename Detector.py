from PIL import Image, ImageDraw
import random, sys, math, PIL, traceback

class Detector:
    def __init__(self, _fillColor, _imagePath, _correctColorParams, _shouldDrawImage):
        self.fillColor = _fillColor
        self.imagePath = _imagePath
        self.correctColorParams = _correctColorParams
        self.shouldDrawImage = _shouldDrawImage
        
        try:
            self.image = Image.open(self.imagePath).convert('RGB') # converting to rgb
            self.draw = ImageDraw.Draw(self.image) # initializing a drawing tool
            self.width = self.image.size[0] # initializing a width and height of image
            self.height = self.image.size[1]
            self.pix = self.image.load()
        except Exception as error:
            print(error)
            exit()

        self.formsPos = []
        self.result = [] # in result array data are sorted(positions are located in a special subarrays)
    
    def Main(self):
        # pushing formsPos array:
        # it contains positions of yellow pixels
        for y in range(self.height):
            for x in range(self.width):
                countCells = 1
                
                r = self.pix[x, y][0]
                g = self.pix[x, y][1]
                b = self.pix[x, y][2]

                isAForm = self.CheckCells([x, y], countCells, 0, self.correctColorParams[0]["value"], self.correctColorParams[0]["mode"])
                isBForm = self.CheckCells([x, y], countCells, 1, self.correctColorParams[1]["value"], self.correctColorParams[1]["mode"])
                isCForm = self.CheckCells([x, y], countCells, 2, self.correctColorParams[2]["value"], self.correctColorParams[2]["mode"])

                if (isAForm and isBForm and isCForm):
                    r, g, b = self.fillColor[0], self.fillColor[1], self.fillColor[2]

                    if (self.shouldDrawImage): self.FillSquare([x, y], countCells, [r, g, b])
                    self.formsPos.append([x,y])

        # pushing result array
        for formPosIndex in range(len(self.formsPos)):
            isFound = False
            if (len(self.result) == 0):
                self.result.append([[self.formsPos[formPosIndex][0],self.formsPos[formPosIndex][1]]])
                continue
            for el in self.result:
                for i in el:
                    if (math.fabs(self.formsPos[formPosIndex][0] - i[0]) < 15 and math.fabs(self.formsPos[formPosIndex][1] - i[1]) < 15):
                        el.append([self.formsPos[formPosIndex][0], self.formsPos[formPosIndex][1]])
                        isFound = True
                        break
            if (not isFound):
                self.result.append([[self.formsPos[formPosIndex][0],self.formsPos[formPosIndex][1]]])
        
        if (self.shouldDrawImage):
            for i in self.result:
                self.FillSquare([i[0][0],i[0][1]], 1, [255, 255, 255])

        print(self.result)

        print("There are " + str(len(self.result)) + " forms.")

        self.image.save("res.jpg", "JPEG")

        print("You can check the result in the res.jpg file.")

    # function for detecting yellow pixels
    def CheckCells(self, point, countCells, colorIndex, value, mode = "moreEquals"):
        for cellX in range(-countCells, countCells):
            for cellY in range(-countCells, countCells):
                try:
                    if (mode == "moreEquals"):
                        # if pixel code less or equals value
                        if (not (self.pix[point[0] + cellX, point[1]][colorIndex] >= value and self.pix[point[0], point[1] + cellY][colorIndex] >= value and self.pix[point[0] + cellX, point[1] + cellY][colorIndex] >= value)):
                            return False
                    elif (mode == "equals"):
                        # if pixel code does not equal value
                        if (not (self.pix[point[0] + cellX, point[1]][colorIndex] == value and self.pix[point[0], point[1] + cellY][colorIndex] == value and self.pix[point[0] + cellX, point[1] + cellY][colorIndex] == value)):
                            return False
                    elif (mode == "less"):
                        # if pixel code more or equals value
                        if (not (self.pix[point[0] + cellX, point[1]][colorIndex] < value and self.pix[point[0], point[1] + cellY][colorIndex] < value and self.pix[point[0] + cellX, point[1] + cellY][colorIndex] < value)): 
                            return False
                except:
                    return False
        return True

    def FillSquare(self, point, countCells, params): # just filling area
        for cellX in range(-countCells, countCells):
            for cellY in range(-countCells, countCells):
                self.draw.point((point[0] + cellX, point[1]), (params[0], params[1], params[2]))
                self.draw.point((point[0], point[1] + cellY), (params[0], params[1], params[2]))
                self.draw.point((point[0] + cellX, point[1] + cellY), (params[0], params[1], params[2]))