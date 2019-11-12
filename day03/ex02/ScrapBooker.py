from ImageProcessor import ImageProcessor
import numpy as np


class ScrapBooker:

    @staticmethod
    def crop(array, dimensions=(1, 1), position=(0, 0)):
        x0 = position[0]
        y0 = position[1]
        x1 = x0 + dimensions[0]
        y1 = y0 + dimensions[1]
        if (x1 < array.shape[0] and y1 < array.shape[1]):
            return (array[x0:x1, y0:y1])
        else:
            print('Error: dimensions are larger than the current image size.')
            return None

    @staticmethod
    def thin(array, n, axis):
        axis = 1 - axis
        slc = slice(n - 1, None, n)
        return np.delete(array, slc, axis)

    @staticmethod
    def juxtapose(array, n, axis):
        return np.concatenate([array] * n, axis=axis)

    @staticmethod
    def mosaic(array, dimensions):
        return np.tile(array, dimensions + (1,))

if __name__ == '__main__':
    ip = ImageProcessor()
    img = ip.load('../resources/42AI.png')
    sb = ScrapBooker()

    cropped_img = sb.crop(img, (4, 4), (50, 50))
    print('Cropped image of dimensions {} x {}'.format(cropped_img.shape[0], cropped_img.shape[1]))

    arr = np.arange(49).reshape(7, 7)
    thin_arr = sb.thin(arr, 3, 0)
    print(thin_arr)

    juxt_arr = sb.juxtapose(img, 3, axis=1)
    ip.display(juxt_arr)

    mos_arr = sb.mosaic(img, (2, 3))
    ip.display(mos_arr)
