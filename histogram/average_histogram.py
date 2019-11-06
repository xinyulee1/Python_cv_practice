import cv2
import matplotlib.pyplot as plt
import numpy as np
def average_histogram_cv():
    image = cv2.imread("cat.jpg", 0)  # 按灰度图像读取
    result = cv2.equalizeHist(image)
    [height, width] = image.shape
    print(height * width)
    hist1 = cv2.calcHist(image, [0], None, [256], [0.0, 255.0])  # 直方图信息提取
    hist2 = cv2.calcHist(result, [0], None, [256], [0.0, 255.0])  # 直方图信息提取
    # hist是一个shape为(256,1)的list，表示0-255每个像素值对应的像素个数，下标即为相应的像素值
    plt.plot(range(256), hist2, color='red')  # 画出图片直方图
    plt.plot(range(256), hist1, color='blue')  # 画出图片直方图
    plt.title("Grayscale Histogram")
    plt.xlabel("x")
    plt.ylabel("pixels")
    plt.show()

    cv2.imshow("gray", image)
    cv2.imshow("result", result)

    cv2.waitKey(0)

def average_histogram_my():
    image = cv2.imread("cat.jpg", 0)  # 按灰度图像读取
    result = cv2.equalizeHist(image)
    [height, width] = image.shape
    sum = height * width
    hist1 = cv2.calcHist(image, [0], None, [256], [0, 255])  # 直方图信息提取
    prob_pixel = []
    cumu_pixel = []
    bins = 0
    #print(hist1)
    for i in hist1:
        for element in i:
            bins += element
            prob_pixel.append(255/sum*bins)
    for element in prob_pixel:
            cumu_pixel.append(int(element*255+0.5))
    image2 = image.copy()
    for x in range(height):
       for y in range(width):
           image2[x,y]=cumu_pixel[image[x,y]]
    cv2.imshow("src", image)
    cv2.imshow("dst",image2)
    hist2 = cv2.calcHist(image2, [0], None, [256], [0, 255])  # 直方图信息提取
    plt.plot(range(256), hist1, color='blue')  # 画出图片直方图
    plt.plot(range(256), hist2, color='yellow')  # 画出图片直方图
    plt.title("Grayscale Histogram")
    plt.xlabel("x")
    plt.ylabel("pixels")
    plt.show()



    return 0
def main():
    return 0

if __name__ == '__main__':
    histogram_my()
    cv2.waitKey(0)
