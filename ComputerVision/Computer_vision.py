import cv2
import numpy as np

aruco = cv2.aruco
p_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
img = cv2.imread('inu.jpg')
corners, ids, rejectedImgPoints = aruco.detectMarkers(img, p_dict) #detection

#Change here
corners2 = [np.empty((1,4,2))]*4
for i,c in zip(ids.ravel(), corners):
  corners2[i] = c.copy()
m[0] = corners2[0][0][2]
m[1] = corners2[1][0][3]
m[2] = corners2[2][0][0]
m[3] = corners2[3][0][1]

width, height = (500,500) #Size of the image after transformation
marker_coordinates = np.float32(m)
true_coordinates   = np.float32([[0,0],[width,0],[width,height],[0,height]])
trans_mat = cv2.getPerspectiveTransform(marker_coordinates,true_coordinates)
img_trans = cv2.warpPerspective(img,trans_mat,(width, height))
cv2_imshow(img_trans)

tmp = img_trans.copy()

# Conversion of the gray scale
tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
#cv2_imshow(tmp)

# Treatment of the blur
tmp = cv2.GaussianBlur(tmp, (11, 11), 0)
#cv2_imshow(tmp)

# (3)Binarisation Processus
th = 130 #Seuil de binarisation(Ajustement requis)
_,tmp = cv2.threshold(tmp,th,255,cv2.THRESH_BINARY_INV) 
#cv2_imshow(tmp)

# (4)Blob detection (= mass)
n, img_label, data, center = cv2.connectedComponentsWithStats(tmp)

# (5)Organisation of the detection results
detected_obj = list() #Destination de stockage du résultat de la détection
tr_x = lambda x : x * 150 / 500 #Coordonnées de l'image sur l'axe X → coordonnées réelles
tr_y = lambda y : y * 150 / 500 #Axe Y 〃
img_trans_marked = img_trans.copy()
for i in range(1,n):
  x, y, w, h, size = data[i]
  if size < 300 : #Ignore the area with less than 300 pixels
    continue
  detected_obj.append( dict( x = tr_x(x),
                              y = tr_y(y),
                              w = tr_x(w),
                              h = tr_y(h),
                              cx = tr_x(center[i][0]),
                              cy = tr_y(center[i][1])))  
  #Verification
  cv2.rectangle(img_trans_marked, (x,y), (x+w,y+h),(0,255,0),2)
  cv2.circle(img_trans_marked, (int(center[i][0]),int(center[i][1])),5,(0,0,255),-1)

# (6)Show the results
cv2_imshow(img_trans_marked)
for i, obj in enumerate(detected_obj,1) :
  print(f'■ Objet détecté{i}Position centrale X={obj["cx"]:>3.0f}mm Y={obj["cy"]:>3.0f}mm ')
