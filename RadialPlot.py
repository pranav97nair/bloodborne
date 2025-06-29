# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:35:01 2024

@author: prana
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as image

r = [2, 3, 5, 4, 6, 7, 8, 2]
r2 = [5, 6, 2, 3, 9, 5, 8, 5]
theta = np.linspace(0.0, 2 * np.pi, len(r))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r, color='blue', label='Armor 1')
ax.fill(theta, r, color='blue', alpha=0.3)
ax.plot(theta, r2, color='red', label='Armor 2')
ax.fill(theta, r2, color='red', alpha=0.3)
ax.set_rmax(10)
ax.grid(True)

# Modify theta labels
theta_ticks = np.linspace(0.0, 2 * np.pi, len(r)-1, endpoint=False)
ax.set_xticks(theta_ticks)
ax.set_xticklabels([''] * len(theta_ticks)) # remove default labels
ax.set_xticklabels(['P', 'B', 'T', 'Bd', 'A', 'F', 'B']) # placeholder labels
ax.tick_params(pad=4)

# Configure image labels
images = ['physical_DEF.jpg','VS_blunt.jpg','VS_thrust.jpg','blood_DEF.jpg','arcane_DEF.jpg','fire_DEF.jpg','bolt_DEF.jpg']
loaded_images = [image.imread(file) for file in images]

# physical
img = loaded_images[0]
img_imgbox = ax.inset_axes([1.03, 0.45, 0.1, 0.1])
img_imgbox.imshow(img)
img_imgbox.axis('off')
# blunt
img = loaded_images[1]
img_imgbox = ax.inset_axes([0.82, 0.91, 0.1, 0.1])
img_imgbox.imshow(img)
img_imgbox.axis('off')
# thrust
img = loaded_images[2]
img_imgbox = ax.inset_axes([0.32, 1.01, 0.1, 0.1])
img_imgbox.imshow(img)
img_imgbox.axis('off')
# blood
img = loaded_images[3]
img_imgbox = ax.inset_axes([-0.08, 0.7, 0.1, 0.1])
img_imgbox.imshow(img)
img_imgbox.axis('off')
# arcane
img = loaded_images[4]
img_imgbox = ax.inset_axes([-0.08, 0.2, 0.1, 0.1])
img_imgbox.imshow(img)
img_imgbox.axis('off')
# fire
img = loaded_images[5]
img_imgbox = ax.inset_axes([0.32, -0.11, 0.1, 0.1])
img_imgbox.imshow(img)
img_imgbox.axis('off')
# bolt
img = loaded_images[6]
img_imgbox = ax.inset_axes([0.82, -0.01, 0.1, 0.1])
img_imgbox.imshow(img)
img_imgbox.axis('off')

#Add legend
angle = np.deg2rad(240)
ax.legend(loc="lower left",
          bbox_to_anchor=(0.1 + np.cos(angle)/2, 0.1 + np.sin(angle)/2))

ax.set_title("Damage Reduction", va='bottom')
plt.show()