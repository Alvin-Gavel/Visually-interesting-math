import os

import star_polygons as sp

main_folder = 'Star_polygons_plots'
default_folder = main_folder + '/Default'
shaded_folder = main_folder + '/Shaded'
inscribed_folder = main_folder + '/Inscribed'
inwards_folder = main_folder + '/Inwards'
outwards_folder = main_folder + '/Outwards'
repetitive_folder = main_folder + '/Repetitions'
compass_folder = main_folder + '/Compass_roses'
for folder in [main_folder, default_folder, shaded_folder, inscribed_folder, inwards_folder, outwards_folder, repetitive_folder, compass_folder]:
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

Swedish_cardinal_directions = ['Öster', 'Nordost', 'Norr', 'Nordväst', 'Väster', 'Sydväst', 'Söder', 'Sydost']
English_cardinal_directions = ['East', 'Northeast', 'North', 'Northwest', 'West', 'Southwest', 'South', 'Southeast']
Mediterranean_cardinal_directions = ['Levante', 'Bora', 'Tramontana', 'Mistral', 'Ponente', 'Garbino', 'Mezzogiorno', 'Exaloc']
Alternate_Mediterranean_cardinal_directions = ['Levante', 'Greco', 'Tramontana', 'Maestro', 'Ponente', 'Libeccio', 'Ostro', 'Scirocco']
Latin_cardinal_directions = ['Subsolanus', 'Caecias', 'Aquilo', 'Septentrio', 'Thrascias', 'Corus', 'Favonius', 'Africus', 'Libonotus', 'Auster', 'Euronotus', 'Vulturnus']
Greek_cardinal_directions = ['Apeliotes', 'Caecias', 'Boreas', 'Aparctias', 'Thrascias', 'Argestes', 'Zephyrus', 'Lips', 'Libonotus', 'Notos', 'Euronotos', 'Eurus']

sp.draw_star_polygon(8, 3, compass_folder, filename = 'Swedish_compass_rose_8_3', mode = "default", labels = Swedish_cardinal_directions)
sp.draw_star_polygon(8, 2, compass_folder, filename = 'Swedish_compass_rose_8_2', mode = "default", labels = Swedish_cardinal_directions)
sp.draw_star_polygon(8, 3, compass_folder, filename = 'English_compass_rose_8_3', mode = "default", labels = English_cardinal_directions)
sp.draw_star_polygon(8, 2, compass_folder, filename = 'English_compass_rose_8_2', mode = "default", labels = English_cardinal_directions)
sp.draw_star_polygon(8, 3, compass_folder, filename = 'Mediterranean_compass_rose_8_3', mode = "default", labels = Mediterranean_cardinal_directions)
sp.draw_star_polygon(8, 2, compass_folder, filename = 'Mediterranean_compass_rose_8_2', mode = "default", labels = Mediterranean_cardinal_directions)
sp.draw_star_polygon(8, 3, compass_folder, filename = 'Alternate_Mediterranean_compass_rose_8_3', mode = "default", labels = Alternate_Mediterranean_cardinal_directions)
sp.draw_star_polygon(8, 2, compass_folder, filename = 'Alternate_Mediterranean_compass_rose_8_2', mode = "default", labels = Alternate_Mediterranean_cardinal_directions)

sp.draw_star_polygon(12, 2, compass_folder, filename = 'Latin_compass_rose_12_2', mode = "default", labels = Latin_cardinal_directions)
sp.draw_star_polygon(12, 3, compass_folder, filename = 'Latin_compass_rose_12_3', mode = "default", labels = Latin_cardinal_directions)
sp.draw_star_polygon(12, 4, compass_folder, filename = 'Latin_compass_rose_12_4', mode = "default", labels = Latin_cardinal_directions)
sp.draw_star_polygon(12, 5, compass_folder, filename = 'Latin_compass_rose_12_5', mode = "default", labels = Latin_cardinal_directions)

sp.draw_star_polygon(12, 2, compass_folder, filename = 'Greek_compass_rose_12_2', mode = "default", labels = Greek_cardinal_directions)
sp.draw_star_polygon(12, 3, compass_folder, filename = 'Greek_compass_rose_12_3', mode = "default", labels = Greek_cardinal_directions)
sp.draw_star_polygon(12, 4, compass_folder, filename = 'Greek_compass_rose_12_4', mode = "default", labels = Greek_cardinal_directions)
sp.draw_star_polygon(12, 5, compass_folder, filename = 'Greek_compass_rose_12_5', mode = "default", labels = Greek_cardinal_directions)
