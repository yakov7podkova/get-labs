# скрипт поворота изображений
from PIL import Image 


uri_list = ['laba_3/images/blue.jpg', 'laba_3/images/calibrovka.jpg', 'laba_3/images/green.jpg', 'laba_3/images/red.jpg',
'laba_3/images/white.jpg', 'laba_3/images/yellow.jpg']

rotated_list = ['laba_3/images_rotated/blue_rotated.jpg', 'laba_3/images_rotated/calibrovka_rotated.jpg', 'laba_3/images_rotated/green_rotated.jpg', 
'laba_3/images_rotated/red_rotated.jpg', 'laba_3/images_rotated/white_rotated.jpg', 'laba_3/images_rotated/yellow_rotated.jpg']


for i in range(6):
    im = Image.open(uri_list[i])
    imC = im.rotate(178.0) # вращаем фото, чтобы получить нужный нам формат
    imC.show()
    imC.save(rotated_list[i])




