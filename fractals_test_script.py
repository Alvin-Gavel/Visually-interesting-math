import os

import fractals

plot_folder = 'Fractal_plots'
try:
   os.mkdir(plot_folder)
except FileExistsError:
   pass
for colour in [True, False]:
   fractals.multibrot(plot_folder, d = 2, x_steps = 1000, y_steps = 1000, colour = colour)
   fractals.mandelbar(plot_folder, d = 2, x_steps = 1000, y_steps = 1000, colour = colour)
   fractals.burning_ship(plot_folder, x_steps = 1000, y_steps = 1000, colour = colour)
