"""
This module is written for my own amusement. It contains a couple of
functions for plotting fractals. Some of the algorithms are taken from
the book The Science of Fractal Images.

Written by Alvin Gavel,

https://github.com/Alvin-Gavel/Demodigi
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

def divergence_fractal(function, plot_folder_path, x_range, y_range, x_steps = 101, y_steps = 101, iterations = 100):
   """
   Given a function, plot which regions of the complex plane diverge
   under repeated iteration and which ones do not.
   """
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
      z[not_diverged] = function(z[not_diverged]) + complex_plane[not_diverged]
      divergence_time[diverged] = np.minimum(divergence_time[diverged], i)
   return real_axis, imag_axis, divergence_time

def standard_plot(real_axis, imag_axis, divergence_time, plot_path):
   plt.pcolormesh(real_axis, imag_axis, divergence_time, shading = 'nearest', cmap = 'gist_gray', norm=LogNorm())
   plt.axis('off')
   fig = plt.gcf()

   # May adjust later
   approx_screen_height = 14.   
   for optimise_width in [True, False]:
      if optimise_width:
         real_convergence_sum = np.where(np.isinf(np.sum(divergence_time, 0)))[0]
         imag_convergence_sum = np.where(np.isinf(np.sum(divergence_time, 1)))[0]
         x_left, x_right = real_axis[real_convergence_sum[0]], real_axis[real_convergence_sum[-1]]
         y_low, y_high = imag_axis[imag_convergence_sum[0]], imag_axis[imag_convergence_sum[-1]]
      else:
         x_left, x_right, y_low, y_high = real_axis[0], real_axis[-1], imag_axis[0], imag_axis[-1]
      fig.set_size_inches((x_right-x_left)/(y_high-y_low) * approx_screen_height, approx_screen_height)
      plt.xlim(x_left, x_right)
      plt.ylim(y_low, y_high)

      if not optimise_width:
         plot_path += "_fixed_width"
      plt.savefig('{}.png'.format(plot_path), format = 'png', bbox_inches = 'tight', dpi=100)
   plt.close()
   return

def multibrot(plot_folder_path, d = 2, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
   """
   Plots the Mandelbrot set, or a generalisation with arbitrary exponent d.
   """
   if plot_folder_path[-1] != '/':
      plot_folder_path += '/'
   
   multibrot_function = lambda z : z**d
   real_axis, imag_axis, divergence_time = divergence_fractal(multibrot_function, plot_folder_path, x_range, y_range, x_steps = x_steps, y_steps = y_steps, iterations = iterations)
   standard_plot(real_axis, imag_axis, divergence_time, "{}multibrot_{}".format(plot_folder_path, d))
   return

def mandelbar(plot_folder_path, d = 2, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
   """
   Plots the Mandelbar set, or a generalisation with arbitrary exponent d.
   """
   if plot_folder_path[-1] != '/':
      plot_folder_path += '/'
      
   mandelbar_function = lambda z : np.conjugate(z)**d
   real_axis, imag_axis, divergence_time = divergence_fractal(mandelbar_function, plot_folder_path, x_range, y_range, x_steps = x_steps, y_steps = y_steps, iterations = iterations)
   standard_plot(real_axis, imag_axis, divergence_time, "{}mandelbar_{}".format(plot_folder_path, d))
   return
   
def burning_ship(plot_folder_path, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
   """
   Plots the Burning ship fractal
   """
   if plot_folder_path[-1] != '/':
      plot_folder_path += '/'
      
   burning_ship_function = lambda z : (np.abs(np.real(z)) + 1j * np.abs(np.imag(z)))**2
   real_axis, imag_axis, divergence_time = divergence_fractal(burning_ship_function, plot_folder_path, x_range, y_range, x_steps = x_steps, y_steps = y_steps, iterations = iterations)
   standard_plot(real_axis, imag_axis, divergence_time, "{}burning_ship".format(plot_folder_path))
   return
