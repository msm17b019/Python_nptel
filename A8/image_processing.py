#Flipping the image

# from PIL import Image
# img=Image.open('C:\\Users\\sujee\\Downloads\\bullet.jpg')

# transposed_image=img.transpose(Image.FLIP_LEFT_RIGHT)
# transposed_image.save('C:\\Users\\sujee\\Downloads\\bullet_edit.jpg')

# print("Done Flipping")


# Enhancing the image

import cv2
img=cv2.imread('C:\\Users\\sujee\\Downloads\\bullet.jpg')

clahe=cv2.createCLAHE()

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

enh_img = clahe.apply(gray_img)

cv2.imwrite('C:\\Users\\sujee\\Downloads\\enhanced.jpg',enh_img)
print('Done Enhancing')


