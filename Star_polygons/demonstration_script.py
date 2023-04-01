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

cardinal_directions = {
'English':                 ['East',    'Northeast', 'North',      'Northwest', 'West',    'Southwest', 'South',       'Southeast'],
'English_abbrev':          ['E',       'NE',        'N',          'NW',        'W',       'SW',        'S',           'SE'],
'Swedish':                 ['Öster',   'Nordost',   'Norr',       'Nordväst',  'Väster',  'Sydväst',   'Söder',       'Sydost'],
'Swedish_abbrev':          ['Ö',       'nö',        'N',          'nv',        'V',       'sv',        'S',           'sö'],
'Finnish':                 ['Itä',     'Koillinen', 'Pohjoinen',  'Luode',     'Länsi',   'Lounas',    'Etelä',       'Kaakko'],
'Mediterranean':           ['Levante', 'Bora',      'Tramontana', 'Mistral',   'Ponente', 'Garbino',   'Mezzogiorno', 'Exaloc'],
'Mediterranean_alternate': ['Levante', 'Greco',     'Tramontana', 'Maestro',   'Ponente', 'Libeccio',  'Ostro',       'Scirocco'],
'Latin':       ['Subsolanus', 'Caecias',     'Aquilo',      'Septentrio', 'Thrascias',     'Corus',         'Favonius',  'Africus',       'Libonotus',     'Auster',    'Euronotus',   'Vulturnus'],
'Greek':       ['Apeliotes',  'Caecias',     'Boreas',      'Aparctias',  'Thrascias',     'Argestes',      'Zephyrus',  'Lips',          'Libonotus',     'Notos',     'Euronotos',   'Eurus'],
'Frankish':    ['Ostroni',    'Ostnordroni', 'Nordostroni', 'Nordroni',   'Nordvuestroni', 'Vuestnordroni', 'Vuestroni', 'Vuestsundroni', 'Sundvuestroni', 'Sundroni',  'Sundostroni', 'Ostsundroni']}

for language, directions in cardinal_directions.items():
   n = len(directions)
   if n == 8:
      label_mode = 'horisontal'
   elif n == 12:
      label_mode = 'radial'
   sp.draw_star_polygons_with_fixed_n(n,compass_folder, filename_kernel = '{}'.format(language), mode = "default", labels = directions, label_mode = label_mode)
