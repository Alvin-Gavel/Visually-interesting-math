import os

import ulam_spiral as us

sidelength = 1001
iterations = 100

main_folder = 'Ulam_spiral_plots'
ten_folder = main_folder + '/10'
hundred_folder = main_folder + '/100'
thousand_folder = main_folder + '/1000'
euler_folder = main_folder + '/Euler'
for folder in [main_folder, ten_folder, hundred_folder, thousand_folder, euler_folder]:
   try:
      os.mkdir(folder)
   except FileExistsError:
      pass

us.plot_prime_square(ten_folder, 10, mark_euler = False)
us.plot_prime_square(hundred_folder, 100, mark_euler = False)
us.plot_prime_square(thousand_folder, 1000, mark_euler = False)
us.plot_prime_square(euler_folder, 100, mark_euler = True)
