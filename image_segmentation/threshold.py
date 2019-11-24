import cv2
import numpy as np

#此为编写颜色空间转换的测试函数
def rgb_read():
    image_rgb = cv2.imread("cubes.jpg")
    image_rgb = cv2.resize(image_rgb,(800,500))
    image_rgb=cv2.GaussianBlur(image_rgb, (15, 15), 0)
    # image_hsv = cv2.cvtColor(image_rgb,cv2.COLOR_BGR2HSV)#官方库处理代码
    image_hsv = image_rgb.copy()
    for row in image_hsv:
        for pixel in row:
           [pixel[0], pixel[1], pixel[2]]= rgb2hsv(pixel[2],pixel[1], pixel[0])
    print(image_hsv)
    cv2.imshow("src", image_rgb)
    cv2.imshow("hsv", image_hsv)

    #颜色空间转换函数
    def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g-b)/m)*30
        else:
            h = ((g-b)/m)*30 +180
    elif mx == g:
        h = ((b-r)/m)*30 + 60
    elif mx == b:
        h = ((r - g) / m) * 30 + 120
    if mx == 0:
        s = 0
    else:
        s = m / mx *255
    v = mx * 255
    return h, s, v
#通过滚动条调节上下阈值选出相应颜色
def threshold_my():
    image_rgb = cv2.imread("cubes.jpg")
    image_rgb = cv2.resize(image_rgb,(800,500))
    image_rgb=cv2.GaussianBlur(image_rgb, (15, 15), 0)
    cv2.namedWindow('threshold',flags= cv2.WINDOW_NORMAL)
    image_hsv = image_rgb.copy()
    for row in image_hsv:
        for pixel in row:
            [pixel[0], pixel[1], pixel[2]] = rgb2hsv(pixel[2], pixel[1], pixel[0])

    cv2.createTrackbar('hmin', 'threshold', 0, 180, lambda x: None)
    cv2.createTrackbar('hmax', 'threshold', 180, 180, lambda x: None)
    cv2.createTrackbar('smin', 'threshold', 0, 255, lambda x: None)
    cv2.createTrackbar('smax', 'threshold', 255, 255, lambda x: None)
    cv2.createTrackbar('vmin', 'threshold', 0, 255, lambda x: None)
    cv2.createTrackbar('vmax', 'threshold', 255, 255, lambda x: None)
    cv2.imshow("src",image_rgb)
    while(True):
        hmin = cv2.getTrackbarPos('hmin', 'threshold')
        hmax = cv2.getTrackbarPos('hmax', 'threshold')
        smin = cv2.getTrackbarPos('smin', 'threshold')
        smax = cv2.getTrackbarPos('smax', 'threshold')
        vmin = cv2.getTrackbarPos('vmin', 'threshold')
        vmax = cv2.getTrackbarPos('vmax', 'threshold')
        floor = np.array([hmin, smin, vmin])
        ceil = np.array([hmax, smax, vmax])
        mask = cv2.inRange(image_hsv, floor, ceil)
        cv2.imshow("result", mask)
        #按下按键q即可退出程序
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
if __name__ == '__main__':
    threshold_my()
    cv2.waitKey(0)
