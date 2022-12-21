import os

import fractals

sidelength = 1001
iterations = 100

plot_folder = 'Fractal_plots'
try:
   os.mkdir(plot_folder)
except FileExistsError:
   pass

# Value of c borrowed from https://commons.wikimedia.org/wiki/File:Julia_set,_plotted_with_Matplotlib.svg
fractals.normal_julia(plot_folder, c = -0.512511498387847167 + 0.521295573094847167j, x_steps = sidelength, y_steps = sidelength, iterations = iterations)

fractals.multibrot(plot_folder, d = 2, x_steps = sidelength, y_steps = sidelength, iterations = iterations)
fractals.mandelbar(plot_folder, d = 2, x_steps = sidelength, y_steps = sidelength, iterations = iterations)
fractals.burning_ship(plot_folder, x_steps = sidelength, y_steps = sidelength, iterations = iterations)
