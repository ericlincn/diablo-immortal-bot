class ColorUtil:

    @staticmethod
    def getDifference(colorA, colorB):
        averageR = (colorA[0] + colorB[0]) * 0.5
        diff = ((2 + averageR / 255) * pow(colorA[0] - colorB[0], 2) + 4 * pow(colorA[1] - colorB[1], 2) + (2 + (255 - averageR) / 255) * pow(colorA[2]- colorB[2], 2)) / (3 * 255) / (3 * 255)
        return diff