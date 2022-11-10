# скрипт построения графика зависимости альбедо/длина волны
import matplotlib.pyplot as plt
import numpy as np
import imageio.v3 as imageio

rotated_list = ['laba_3/images_rotated/blue_rotated.jpg', 'laba_3/images_rotated/calibrovka_rotated.jpg', 'laba_3/images_rotated/green_rotated.jpg', 
'laba_3/images_rotated/red_rotated.jpg', 'laba_3/images_rotated/white_rotated.jpg', 'laba_3/images_rotated/yellow_rotated.jpg']


def readRGB(photoName):
    photo = imageio.imread(photoName)

    cut = photo[255:630, 470:600, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    return luma


luma_blue = readRGB(rotated_list[0])
luma_green = readRGB(rotated_list[2])
luma_red = readRGB(rotated_list[3])
luma_white = readRGB(rotated_list[4])
luma_yellow = readRGB(rotated_list[5])

w = 95

wavelength_l = [578 - (241 - i)*1.12 for i in range(w, 300)] # массив длин волн


albedo_b = [luma_blue[i]/luma_white[i] for i in range(w, 300)]
albedo_g = [luma_green[i]/luma_white[i] for i in range(w, 300)]
albedo_r = [luma_red[i]/luma_white[i] for i in range(w, 300)]
albedo_w = [luma_white[i]/luma_white[i] for i in range(w, 300)]
albedo_y = [luma_yellow[i]/luma_white[i] for i in range(w, 300)]


fig = plt.figure(figsize=(10, 5), dpi=200)

plt.plot(wavelength_l, albedo_b, c = 'blue')
plt.plot(wavelength_l, albedo_g, c = 'green')
plt.plot(wavelength_l, albedo_r, c = 'red')
plt.plot(wavelength_l, albedo_w, c = 'white')
plt.plot(wavelength_l, albedo_y, c = 'yellow')


plt.xlabel('Длина волны, нм')
plt.ylabel('Альбедо')

ax = plt.gca()

ax.set_facecolor('lightgray')


plt.minorticks_on()
plt.grid(which = 'major', c = 'gray', linewidth = 1)
plt.grid(which = 'minor', c = 'gray', linestyle = ':')

plt.legend(fontsize = 8)
plt.show()
