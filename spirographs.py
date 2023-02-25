import numpy as np
import matplotlib.pyplot as plt

def figure_dimensions(matplot_units, inches):
   x_left, x_right, y_low, y_high = -matplot_units, matplot_units, -matplot_units, matplot_units
   plt.xlim(x_left, x_right)
   plt.ylim(y_low, y_high)
   plt.axis('off')
   fig = plt.gcf()
   fig.set_size_inches(inches, inches)
   return

def draw(plot_folder_path, R_num, R_denom, rnorm_num = 1, rnorm_denom = 1, figsize = 5, outlines = False):
   R = R_num / R_denom
   rnorm = rnorm_num / rnorm_denom
   r = R * rnorm
   d = np.linspace(0, R_num * 2 * np.pi, num = 10000)
   X = (1 - R) * np.cos(d)
   Y = (1 - R) * np.sin(d)
   x = X + r * np.cos(- d / R)
   y = Y + r * np.sin(- d / R)
   
   plt.clf()
   figure_dimensions((1 - R * (1 - rnorm)) * 1.05, figsize)
   if outlines:
      for radius in [1, (1 - R)]:
         d_circ = np.linspace(0, 2 * np.pi, num = 10000)
         X_circ = radius * np.cos(d_circ)
         Y_circ = radius * np.sin(d_circ)
         plt.plot(X_circ, Y_circ, ls="--", c = "gray")   
   plt.plot(x, y, ls="-", c = "k")

   namestring = "R_{}_{}_rnorm_{}_{}".format(R_num, R_denom, rnorm_num, rnorm_denom)
   if outlines:
      namestring += "_outlines"
   if figsize != 5:
      namestring += "_sz_{}".format(figsize)
   namestring += ".png"
   plt.savefig("{}/{}".format(plot_folder_path, namestring), format = 'png', bbox_inches = 'tight')
   plt.close()
   return
   
def draw_denom_below(plot_folder_path, m_max, rnorm_num = 1, rnorm_denom = 1, outlines = False):
   for m in range(1, m_max):
      for n in range(1, m):
         draw(plot_folder_path, n, m, rnorm_num, rnorm_denom, outlines = outlines)
   return
