import matplotlib.pyplot as plt
import numpy as np
import imageio.v3 as imageio


rotated_list = ['laba_3/images_rotated/blue_rotated.jpg', 'laba_3/images_rotated/calibrovka_rotated.jpg', 'laba_3/images_rotated/green_rotated.jpg', 
'laba_3/images_rotated/red_rotated.jpg', 'laba_3/images_rotated/white_rotated.jpg', 'laba_3/images_rotated/yellow_rotated.jpg']


def readRGB(photoName):
    photo = imageio.imread(photoName)
    background = photo[255:630, 400:550, 0:3].swapaxes(0, 1)


    cut = photo[255:630, 470:600, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    return luma


luma_blue = readRGB(rotated_list[0])
luma_green = readRGB(rotated_list[2])
luma_red = readRGB(rotated_list[3])
luma_white = readRGB(rotated_list[4])
luma_yellow = readRGB(rotated_list[5])


wavelength_l = [578 - (241 - i)*1.12 for i in range(375)]


fig = plt.figure(figsize=(10, 5), dpi=200)

plt.plot(wavelength_l, luma_blue, c = "blue", label = "синий лист")
plt.plot(wavelength_l, luma_green, c = "green", label = "зелёный лист")
plt.plot(wavelength_l, luma_red, c = "red", label = "красный лист")
plt.plot(wavelength_l, luma_white, c = "white", label = "белый лист")
plt.plot(wavelength_l, luma_yellow, c = "yellow", label = "жёлтый лист")


plt.xlabel('Длина волны, нм')
plt.ylabel('Яркость')

ax = plt.gca()

ax.set_facecolor('lightgray')

plt.title('Отраженная интенсивность излучения лампы накаливания')
plt.minorticks_on()
plt.grid(which = 'major', c = 'gray', linewidth = 1)
plt.grid(which = 'minor', c = 'gray', linestyle = ':')

plt.legend(fontsize = 8)
plt.show()

