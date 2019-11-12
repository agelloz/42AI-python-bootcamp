import matplotlib.pyplot as plt


class ImageProcessor:

    @staticmethod
    def load(path):
        img = plt.imread(path)
        print('Loading image of dimensions {} x {}'.format(img.shape[0], img.shape[1]))
        return img

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()


if __name__ == '__main__':
    img = ImageProcessor()
    arr = img.load('../resources/42AI.png')
    print(arr)
    img.display(arr)
