import os

import spirographs as sp

main_folder = 'Spirograph_plots'
default_folder = main_folder + '/Default'
outlined_folder = main_folder + '/Outlined'
for folder in [main_folder, default_folder, outlined_folder]:
   try:
      os.mkdir(folder)
   except FileExistsError:
      pass

   
sp.draw_denom_below(default_folder, 10, outlines = False)
sp.draw_denom_below(outlined_folder, 10, outlines = True)
