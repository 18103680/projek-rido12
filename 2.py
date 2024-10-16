# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:40:38 2020

@author: artmenlope

This script uses a rational function on complex numbers, implements bilinear interpolation,
and includes an animation of the function.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cplotting_tools as cplt

def bilinear_interpolation(x, y, f, xi, yi):
    """Perform bilinear interpolation at the point (xi, yi) based on values in f."""
    x0 = np.floor(xi).astype(int)
    x1 = x0 + 1
    y0 = np.floor(yi).astype(int)
    y1 = y0 + 1

    if x0 < 0 or x1 >= f.shape[0] or y0 < 0 or y1 >= f.shape[1]:
        raise ValueError("Interpolation point out of bounds.")

    Q11 = f[x0, y0]
    Q21 = f[x1, y0]
    Q12 = f[x0, y1]
    Q22 = f[x1, y1]

    interpolated_value = (Q11 * (x1 - xi) * (y1 - yi) +
                          Q21 * (xi - x0) * (y1 - yi) +
                          Q12 * (x1 - xi) * (yi - y0) +
                          Q22 * (xi - x0) * (yi - y0))
    
    return interpolated_value

plt.close("all")

# Parameters
N = 100
lim = 2
x, y = np.meshgrid(np.linspace(-lim, lim, N), 
                   np.linspace(-lim, lim, N))

z = x + 1j * y

# Coefficients for the function
try:
    a = float(input("Masukkan koefisien a: "))
    b = float(input("Masukkan koefisien b: "))
    c = float(input("Masukkan koefisien c: "))
    d = float(input("Masukkan koefisien d: "))
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
    exit()

# Prepare for animation
fig, ax = plt.subplots()
im = ax.imshow(np.zeros((N, N)), extent=(-lim, lim, -lim, lim), cmap="twilight_r")
ax.set_title("Animation of f(z) = (a*z + b) / (c*z + d)")
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")

# Animation function
def update(a):
    f = (a * z + b) / (c * z + d)
    im.set_array(np.angle(f))  # Use the angle of the complex function for coloring
    return [im]

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(-2, 2, 100), blit=True)

# Display the plot
plt.colorbar(im, ax=ax)
plt.show()
