import os

import fractals

plot_folder = 'Fractal_plots'
try:
   os.mkdir(plot_folder)
except FileExistsError:
   pass
fractals.multibrot(plot_folder, d = 2, x_steps = 1000, y_steps = 1000)
fractals.mandelbar(plot_folder, d = 2, x_steps = 1000, y_steps = 1000)
fractals.burning_ship(plot_folder, x_steps = 1000, y_steps = 1000)
