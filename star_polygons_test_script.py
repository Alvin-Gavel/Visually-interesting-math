import os

import star_polygons as sp

folder = 'Star_polygons_plots'
try:
   os.mkdir(folder)
except FileExistsError:
   pass
   
sp.draw_star_polygons_below(10, folder)
