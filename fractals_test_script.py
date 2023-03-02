import os

import fractals as fr

sidelength = 1001
iterations = 100

main_folder = 'Fractal_plots'
mandelbrot_folder = main_folder + '/Mandelbrot'
mandelbar_folder = main_folder + '/Mandelbar'
ship_folder = main_folder + '/Burning_ship'
julia_folder = main_folder + '/Julia'
for folder in [main_folder, mandelbrot_folder, mandelbar_folder, ship_folder, julia_folder]:
   try:
      os.mkdir(folder)
   except FileExistsError:
      pass

mandelbrot = fr.multibrot('Mandelbrot', mandelbrot_folder, d = 2, x_steps = sidelength, y_steps = sidelength, iterations = iterations)
mandelbrot.run()
mandelbrot.plot_all()

mandelbar = fr.mandelbar('Mandelbar', mandelbar_folder, d = 2, x_steps = sidelength, y_steps = sidelength, iterations = iterations)
mandelbar.run()
mandelbar.plot_all()

ship = fr.burning_ship('Burning_ship', ship_folder, x_steps = sidelength, y_steps = sidelength, iterations = iterations)
ship.run()
ship.plot_all()

# Value of c borrowed from https://commons.wikimedia.org/wiki/File:Julia_set,_plotted_with_Matplotlib.svg
julia = fr.normal_julia('Julia', julia_folder, c = -0.512511498387847167 + 0.521295573094847167j, x_steps = sidelength, y_steps = sidelength, iterations = iterations)
julia.run()
julia.plot_all()
