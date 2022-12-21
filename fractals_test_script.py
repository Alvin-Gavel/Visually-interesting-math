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
