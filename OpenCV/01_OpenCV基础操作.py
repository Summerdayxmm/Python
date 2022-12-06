import cv2


cv2.namedWindow('img', cv2.WINDOW_NORMAL)   # 创建窗口
cv2.resizeWindow('img', 320, 240)           # 重新调整窗口大小

img = cv2.imread("./images/01.jpeg")        # 读取图片

while True:
    cv2.imshow('img', img)                  # 显示图片
    key = cv2.waitKey(0)

    if(key & 0xFF == ord('q')):             # quit
        break
    elif(key & 0xFF == ord('s')):           # save
        cv2.imwrite("/Users/enchanted/MyLibrary/CodeRepository/Python/OpenCV/images/New.jpg", img)       # rewrite
    else:
        print(key)
    
cv2.destroyAllWindows()                     # 销毁窗口