import os

import star_polygons as sp

main_folder = 'Star_polygons_plots'
default_folder = main_folder + '/Default'
shaded_folder = main_folder + '/Shaded'
inscribed_folder = main_folder + '/Inscribed'
inwards_folder = main_folder + '/Inwards'
outwards_folder = main_folder + '/Outwards'
repetitive_folder = main_folder + '/Repetitions'
for folder in [main_folder, default_folder, shaded_folder, inscribed_folder, inwards_folder, outwards_folder, repetitive_folder]:
   try:
      os.mkdir(folder)
   except FileExistsError:
      pass

   
sp.draw_star_polygons_below(10, default_folder, mode = "default")
sp.draw_star_polygons_below(10, shaded_folder, mode = "shaded")
sp.draw_star_polygons_below(10, inscribed_folder, mode = "inscribed")
sp.draw_star_polygons_below(10, inwards_folder, mode = "inwards")
sp.draw_star_polygons_below(10, outwards_folder, mode = "outwards")
sp.draw_star_polygons_below(10, repetitive_folder, mode = "default", repetitions = 5)
