import os
import sys
import logging
from PIL import Image

logging.basicConfig(filename='imageWaterMark.log',level=logging.INFO)
if len(sys.argv) < 3:
    print('Usage: watermark.py \'image folder path\' \'logo path\' [topleft, topright, bottomleft, bottomright, center]')
    sys.exit()
elif len(sys.argv) == 4:
    path = sys.argv[1]
    lgo = sys.argv[2]
    pos = sys.argv[3]
else:
    path = sys.argv[1]
    lgo = sys.argv[2]


logo = Image.open(lgo)
logoWidth = logo.width
logoHeight = logo.height
count = 0

for filename in os.listdir(path):
    if (filename.endswith('.jpg') or filename.endswith('.png')) and (filename != lgo):
        try:
            image = Image.open(path + '/' + filename)
        except:
            logging.error('Error abriendo image '+ filename)
            
        imageWidth = image.width
        imageHeight = image.height
        try:
            image = image.resize((1080,1080), Image.ANTIALIAS)
        except:
             logging.error('Error durante image resize'+ filename)
        count+=1
        print count
        try:
            if pos == 'topleft':
                image.paste(logo, (0, 0), logo)
            elif pos == 'topright':
                image.paste(logo, (imageWidth - logoWidth, 0), logo)
            elif pos == 'bottomleft':
                image.paste(logo, (0, imageHeight - logoHeight), logo)
            elif pos == 'bottomright':
                image.paste(logo, ((imageWidth - logoWidth)/2, (imageHeight - logoHeight)/2), logo)
            elif pos == 'center':
                image.paste(logo, ((imageWidth - logoWidth)/2, (imageHeight - logoHeight)/2), logo)
            elif pos == 'centralized':
                image.paste(logo, (0, 0), logo)

            else:
                print('Error: ' + pos + ' is not a valid position')
                print('Usage: watermark.py \'image path\' \'logo path\' [topleft, topright, bottomleft, bottomright, center]')

            image.save('image_new' + '/' + filename)
            print('Added watermark to ' + path + '/' + filename)

        except:
            image.paste(logo, ((imageWidth - logoWidth)/2, (imageHeight - logoHeight)/2), logo)
            image.save('image_new' + '/' + filename)
            print('Added default watermark to ' + 'image_new' + '/' + filename)
