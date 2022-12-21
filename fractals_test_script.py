import os

import fractals

sidelength = 1001

plot_folder = 'Fractal_plots'
try:
   os.mkdir(plot_folder)
except FileExistsError:
   pass
for color in [True, False]:
   fractals.multibrot(plot_folder, d = 2, x_steps = sidelength, y_steps = sidelength, color = color)
   fractals.mandelbar(plot_folder, d = 2, x_steps = sidelength, y_steps = sidelength, color = color)
   fractals.burning_ship(plot_folder, x_steps = sidelength, y_steps = sidelength, color = color)
   # Value of c borrowed from https://commons.wikimedia.org/wiki/File:Julia_set,_plotted_with_Matplotlib.svg
   fractals.normal_julia(plot_folder, c = -0.512511498387847167 + 0.521295573094847167j, x_steps = sidelength, y_steps = sidelength, color = color)
