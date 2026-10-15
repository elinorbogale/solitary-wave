# July 29, this is for the COVER IMAGE
# 8 september 2026 whoop whoop

# pyconda (Python 3.13.5) - you need all these packages
import matplotlib.pyplot as plt
import scipy.stats as stats
import csv
import numpy as np
import pandas as pd
import glob
import os
from scipy.signal import find_peaks, argrelextrema
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path
from scipy.interpolate import CubicSpline
from mayavi import mlab
from tvtk.api import tvtk
from mlabtex import mlabtex
# ---------------------------------------------------


master_fig = mlab.figure(size=(900, 900), bgcolor=(0.1, 0.1, 0.1))

top_scale_factor = 0.0015  # multiplier for size of chain
z_offset = 1.4  # distance between figure and chain


# THE CHAIN
N = np.arange(1, 21)  
num_spheres = len(N)
radii_orig = 5 * (1.13) ** (N - 1)

x_centers_orig = np.zeros(len(N))
x_centers_orig[0] = radii_orig[0]
y_centers = np.zeros(num_spheres)
z_centers = np.zeros(num_spheres)

for i in range(1, len(N)):
    x_centers_orig[i] = x_centers_orig[i - 1] + radii_orig[i - 1] + radii_orig[i]

# Apply the scaling factor uniformly
x_centers_scaled = x_centers_orig * top_scale_factor
radii_scaled = radii_orig * top_scale_factor

# The increasing tapered Grains
chain = mlab.points3d(
    x_centers_scaled,
    y_centers,  
    z_centers + z_offset,  # Lifted strictly UP on the vertical axis
    radii_scaled,  
    mode="sphere",
    scale_factor=2.0,      # Keeps diameter = 2 * radii_scaled
    colormap="jet",
    resolution=64,  
    figure=master_fig
)

max_r_scaled = max(radii_scaled)
box_thickness_scaled = 1.5 * max_r_scaled  

# Right Wall
x_wall_right = (max(x_centers_scaled) + max_r_scaled) + (box_thickness_scaled / 2)
box_right = mlab.points3d(
    x_wall_right,
    0,
    z_offset,
    max_r_scaled,
    mode="cube",
    color=(0.7, 0.7, 0.7),
    scale_factor=2.0,
    figure=master_fig
)
box_right.actor.actor.scale = [1, 2, 1]

# Left Wall
x_wall_left_center = - (box_thickness_scaled / 2)
box_left = mlab.points3d(
    x_wall_left_center,
    0,
    z_offset,
    max_r_scaled,
    mode="cube",
    color=(0.7, 0.7, 0.7),
    scale_factor=2.0,
    figure=master_fig
)
box_left.actor.actor.scale = [1, 2, 1]


# ASSEMBLY MAAKES LIFE EAZZY

left_actor = box_left.actor.actor
right_actor = box_right.actor.actor
chain_actor = chain.actor.actor

combined_assembly = tvtk.Assembly()
combined_assembly.add_part(left_actor)
combined_assembly.add_part(right_actor)
combined_assembly.add_part(chain_actor)

# remove individuals, move as one
master_fig.scene.renderer.remove_actor(right_actor)
master_fig.scene.renderer.remove_actor(left_actor)
master_fig.scene.renderer.remove_actor(chain_actor)
master_fig.scene.renderer.add_actor(combined_assembly)

 # keep tweaking it

combined_assembly.position = [0.12, 0.0, 0.0]
combined_assembly.rotate_z(40)


# --- 3. 3D PHASE DIAGRAM PLOT (UNTOUCHED AT THE BOTTOM) ---
folder = Path(
    "/Users/derrick/Documents/Theoretical_Physics/MARCH-APRIL-ELI/q13/w00_q13/KE_q13_n20_w00_Mar30.dat"
)
matrix = pd.read_table(folder)
t = matrix.iloc[:, 0] 
cmap = plt.get_cmap('jet')
extents = [0, 1, 0, 1, 0, 1]
x = t*10**(-3) # sets time in ms,not musec
ranges = [0, x.max(), 0, 20, 0, 1]

for n in range(1, 21):
    z = matrix.iloc[:, n] 
    norm_z = z / 0.001157
    y = [n] *len(x) #3
    norm_y = [n / 20] * len(t)
    norm_x = t / max(t) 
    line_color = cmap((n - 1) / 19.0)[:3] 
    m=mlab.plot3d(
        norm_x, norm_y, norm_z, 
        #x,y,norm_z,
        tube_radius=0.01, 
        color=line_color,
        figure=master_fig,
        #extent=extents
    )
    #m.actor.actor.scale  = (1/x.max(), 1/20, 1) 
    m.actor.actor.scale = (1,1,1)
   
mlab.outline(extent=extents, 
             color=(1, 1, 1), 
             figure=master_fig,
             line_width=3)


# ==========================================================
# CUSTOM TICKS FOR THE UNIT CUBE
# ==========================================================

tick_radius = 0.0012
tick_length = 0.025
scales = 0.029

xmax_ms = x.max()      # your displayed time range in ms

# ----------------------------------------------------------
# X TICKS (Lower Forward: y=0, z=0)
# ----------------------------------------------------------
x_tick_labels = np.arange(0, int(np.floor(xmax_ms)) + 1, 1)

for xt in x_tick_labels:
    xpos = xt / xmax_ms

    # tick mark (pointing outward to negative y)
    mlab.plot3d(
        [xpos, xpos],
        [0.0, -tick_length],
        [0.0, 0.0],
        tube_radius=tick_radius,
        color=(1, 1, 1),
        figure=master_fig
    )

    # tick label
    mlab.text3d(
        xpos - 0.02,
        -0.08,
        -0.02,
        f"{xt}",
        scale=scales,
        color=(1, 1, 1)
    )

# X axis title
mlab.text3d(
    0.50,
    -0.15,
    -0.1,
    "t (ms)",
    scale=0.04,
    color=(1, 1, 1)
)

# ----------------------------------------------------------
# Y TICKS (Lower Right: x=1, z=0)
# ----------------------------------------------------------
y_tick_labels = np.arange(0, 21, 5)

for n in y_tick_labels:
    ypos = n / 20

    # tick mark (pointing outward to positive x)
    mlab.plot3d(
        [1.0, 1.0 + tick_length],
        [ypos, ypos],
        [0.0, 0.0],
        tube_radius=tick_radius,
        color=(1, 1, 1),
        figure=master_fig
    )

    # tick label
    mlab.text3d(
        1.04,
        ypos - 0.01,
        -0.02,
        f"{n}",
        scale=scales,
        color=(1, 1, 1)
    )

# Y axis title
mlab.text3d(
    1.15,
    0.5,
    -0.05,
    "N",
    scale=0.05,
    color=(1, 1, 1)
)

# ----------------------------------------------------------
# Z TICKS (Upward Left: x=0, y=0)
# ----------------------------------------------------------
z_tick_values = np.arange(0.2, 1.01, 0.2)

for zt in z_tick_values:
    # tick mark (pointing outward to negative x)
    mlab.plot3d(
        [-tick_length, 0.0],
        [0.0, 0.0],
        [zt, zt],
        tube_radius=tick_radius,
        color=(1, 1, 1),
        figure=master_fig
    )

    # tick label
    mlab.text3d(
        -0.12,
        -0.03,
        zt - 0.01,
        f"{zt:.1f}",
        scale=scales,
        color=(1, 1, 1)
    )

# Z axis title
mlab.text3d(
    -0.36,
    -0.05,
    0.5,
    "KE",
    scale=0.05,
    color=(1, 1, 1)
)
mlab.text3d(-0.26, 0.01, 0.47, "norm", scale=0.025, color=(1, 1, 1))

# cherry on the icing
mlab.view(azimuth=-50, elevation=70, distance='auto', focalpoint='auto')

mlab.draw()
filename = 'Cover_10Sep26_Ver3.eps'
mlab.savefig(f"/Users/derrick/Documents/LalaStudy2/{filename}", figure=master_fig,size=(600, 600),magnification=4)

mlab.show()