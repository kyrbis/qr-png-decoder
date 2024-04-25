import os

import cv2

 # config
allowed_image_extensions = ('.png', '.jpg', '.jpeg')  # lower case

def readBarcode(image_file, output_file_extension):
    img = cv2.imread(image_file)
    qcd = cv2.QRCodeDetector()
    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
    print(str(image_file) + '\n' + str(points))
    
    with open(image_file + output_file_extension, 'w+') as f:
        for info in decoded_info:
            f.write(info)

 # main
print(cv2.__version__)

for f in os.listdir('.'):
    if f.lower().endswith(allowed_image_extensions):
        readBarcode(f, '.conf')
