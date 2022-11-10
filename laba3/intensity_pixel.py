import numpy as np
import lightfunctions as j 

rotated_list = ['laba_3/images_rotated/blue_rotated.jpg', 'laba_3/images_rotated/calibrovka_rotated.jpg', 'laba_3/images_rotated/green_rotated.jpg', 
'laba_3/images_rotated/red_rotated.jpg', 'laba_3/images_rotated/white_rotated.jpg', 'laba_3/images_rotated/yellow_rotated.jpg']

plot_list = ['laba_3/plots/blue_tungsten.jpg', 'laba_3/plots/calibrovka_plot.jpg', 'laba_3/plots/green_tungsten.jpg', 'laba_3/plots/red_tungsten.jpg',
'laba_3/plots/white_tungsten.jpg', 'laba_3/plots/yellow_tungsten.jpg']

lamp = ['tungsten', 'mercury']
surface = ['blue', 'white', 'green', 'red', 'white', 'yellow']


for i in range(6):
    if i == 1:
        luma = j.readIntensity(rotated_list[i], plot_list[i], lamp[1], surface[i])
        green_peak = np.argmax(luma[200:225])
        orange_peak = np.argmax(luma[225:250])
        blue_peak = np.argmax(luma[150:175])

    else:
        j.readIntensity(rotated_list[i], plot_list[i], lamp[0], surface[i])