import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.pyplot import figure

def make_multibrot(plot_folder_path, d = 2, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
   """
   Plots the Mandelbrot set, or a generalisation with arbitrary exponent d.
   """
   if plot_folder_path[-1] != '/':
      plot_folder_path += '/'
   
   # If we have symmetric intervals, we want to make sure that the real
   # and imaginary axes are plotted.
   if abs(x_range[0]) == abs(x_range[1]):
      x_steps += (x_steps + 1) % 2
   if abs(y_range[0]) == abs(y_range[1]):
      y_steps += (y_steps + 1) % 2
   real_axis = np.linspace(x_range[0], x_range[1], x_steps)
   imag_axis = np.linspace(y_range[0], y_range[1], y_steps)
   complex_plane = np.meshgrid(real_axis, imag_axis)
   complex_plane = np.asarray(complex_plane)   
   complex_plane = complex_plane[0,:,:] + 1j * complex_plane[1,:,:]
   z = np.zeros((x_steps, y_steps), dtype = np.clongdouble)
   
   divergence_time = np.ones((x_steps, y_steps), dtype = np.longdouble) * np.inf
   for i in range(iterations):
      diverged = np.abs(z) > 2
      not_diverged = np.logical_not(diverged)      
      z[not_diverged] = z[not_diverged]**d + complex_plane[not_diverged]
      divergence_time[diverged] = np.minimum(divergence_time[diverged], i)

   plt.pcolormesh(real_axis, imag_axis, divergence_time, shading = 'nearest', cmap = 'gist_gray', norm=LogNorm())
   plt.axis('off')
   plt.savefig("{}multibrot_{}.png".format(plot_folder_path, d), format = 'png', bbox_inches = 'tight', dpi=100)
   plt.close()
   return
