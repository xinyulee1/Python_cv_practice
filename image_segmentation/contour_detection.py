def contour_detection():
    image_rgb=cv2.imread("cubes.jpg")
    image_rgb=cv2.resize(image_rgb, (800, 500))
    image_rgb=cv2.GaussianBlur(image_rgb, (15, 15), 0)
    #首先将图片根据颜色二值化处理,阈值由同一文件夹下threshold.py手动测试得到
    floor=np.array([56, 155, 0])
    ceil=np.array([83, 203, 255])
    mask=cv2.inRange(image_hsv, floor, ceil)
    cv2.imshow("result", mask)
    #找出绿色的所有区域
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #将每个绿色区域圈起来
    print(len(contors))
    for i in range(0,len(contours)):
        x,y,w,h = cv2.boundingRect(contours[i])
        cv2.rectangle(image_rgb,(x,y),(x+w,y+h),(153,153,0),3)
    #cv2.drawContours(image_rgb, contours, -1, (0, 255, 0), 3)
    cv2.imshow("src",image_rgb)
