import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np
def image_convolution(image,kernel):
    [img_height,img_width] = image.shape
    [kernel_height,kernel_width] = kernel.shape

    expand_width = int((kernel_width - 1)/2)
    expand_height = int((kernel_height - 1)/2)

    con_height = int(img_height + expand_height*2)
    con_width = int(img_width + expand_width*2)

    #给结果图像、用于卷积处理的矩阵创建空间
    result_image = np.zeros(image.shape)
    con_image = np.zeros((con_height, con_width))

    #填入图片
    con_image[expand_height:expand_height+img_height, expand_width:expand_width+img_width]=image[ : , :]
    #对每个像素点进行处理
    for i in range(expand_height,expand_height+img_height):
        for j in range(expand_width,expand_width+img_width):
            result_image[i-expand_height][j-expand_width] = int(np.sum(con_image[i-expand_height:i+expand_height+1, j-expand_width:j+expand_width+1]*kernel))
    print(result_image)
    return result_image
def gauss_mask(sigma):
    mask_height = mask_width = sigma*2+1
    mask = np.zeros((mask_height, mask_width))
    sum = 0 
    for i in range(-sigma,sigma+1):
        for j in range(-sigma,sigma+1):
            mask[i+sigma][j+sigma] = np.exp(-0.5 * (i ** 2+ j ** 2) / sigma ** 2)
            sum += mask[i+sigma][j+sigma]
    return mask/sum
if __name__ == "__main__":
    image = cv2.imread("dongcha.jpg", 0)
    image = cv2.resize(image,(512,512))
    kernel = gauss_mask(1)
    result = np.zeros(image.shape)
    result = image_convolution(image = image,kernel = kernel)
    print(result)
    result=result.astype(np.uint8)
    cv2.imshow("result", result)
    cv2.imshow("orignal", image)
    print(gauss_mask(1))
    cv2.waitKey(0)

