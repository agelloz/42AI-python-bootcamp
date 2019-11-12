from ImageProcessor import ImageProcessor
import numpy as np

class ColorFilter:

    @staticmethod
    def invert(array):
        return 255 - array

    def to_blue(self, array):
        return img

    def to_green(self, array):
        return array

    def to_red(self, array):
        return array - self.to_green(array) - self.to_blue(array)

    @staticmethod
    def celluloid(array, k):
        return new


if __name__ == '__main__':
    ip = ImageProcessor()
    img = ip.load('../resources/Toon-shader.jpg')
    ip.display(img)

    print(img[:10,0,0])
    print(img.shape)

    cf = ColorFilter()

    inv = cf.invert(img)
    ip.display(inv)

    blu = cf.to_blue(img)
    ip.display(blu)

    gre = cf.to_green(img)
    print(gre.shape)
    ip.display(gre)

    red = cf.to_red(img)
    print(red.shape)
    ip.display(red)

    cel = cf.celluloid(img, 3)
    print(cel.shape)
    ip.display(cel)
