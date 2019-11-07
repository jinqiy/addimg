# -*- coding: utf8 -*-

import cv2

# OpenCV 人脸检测
face_patterns = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml'
)

headimg = cv2.imread('face2.jpg')
#headimg = cv2.imread('face2.png')
faces = face_patterns.detectMultiScale(
    headimg,
    scaleFactor=1.1,
    minNeighbors=8,
    minSize=(50, 50)
)
k_w = faces[0][2]
k_h = faces[0][3]
print k_w,k_h

headimg_wh = headimg.shape
#temp = float(headimg_wh[1])/float(headimg_wh[0])
#temp_h = int(1024*temp)
#print headimg_wh,temp,temp_h
#headimg_res = cv2.resize(headimg,(temp_h,1024),interpolation=cv2.INTER_CUBIC)
headimg_res = headimg

hat = cv2.imread('chrismashat.png')
hat1 = cv2.imread('chrismashat.png',cv2.IMREAD_UNCHANGED)
b,g,r = cv2.split(hat)
b,g,r,a = cv2.split(hat1)

rgb_hat = cv2.merge((b,g,r))
hat_wh = rgb_hat.shape
temp_hat = float(hat_wh[1]/hat_wh[0])
#temp_hat_h = int((k_w)*4/5*temp_hat)
temp_hat_h = int(k_h*temp_hat*1.3)
#temp_hat_w = int(k_w*3/5)
temp_hat_w = int(k_w)
print hat_wh,temp_hat_h,temp_hat_w,temp_hat
# change hat size
hat_res = cv2.resize(rgb_hat,(temp_hat_h,temp_hat_w),interpolation=cv2.INTER_CUBIC)
d_res = cv2.resize(a,(temp_hat_h,temp_hat_w),interpolation=cv2.INTER_CUBIC)

#for face0 in faces:
# change hat position
#x_new = faces[0][0] + int(k_w/6)
#y_new = faces[0][1] - int(k_h*0.65)
x_new = faces[0][0] - int(k_w/10)
y_new = faces[0][1] - int(k_h*0.7)
#  x_new = face0[0] + int(k_w/6)
#  y_new = face0[1] - int(k_h*0.65)
center=[y_new,x_new]
for i in range(temp_hat_w - 10):  # -10去掉噪
  for j in range(temp_hat_h):
    if d_res[i,j] > 10:# 0 is black
      headimg_res[center[0]+i,center[1]+j] = hat_res[i,j] # color replace


# 保存最终结果
#for (x,y,w,h) in faces:
  #cv2.imwrite('new_head.jpg', faces)
#  cv2.rectangle(headimg,(x,y),(x+w,y+h),(0,255,0),2)
#cv2.imshow('iimm',headimg)

cv2.imshow('iimm',headimg_res)
cv2.waitKey(0)
cv2.destoryAllWindows()

#cv2.imwrite('result.png',headimg_res)

# 获取头像和hat图案宽度
#w_head, h_head = headimg.shape[:2]
#w_hat, h_hat = hat.shape[:2]

