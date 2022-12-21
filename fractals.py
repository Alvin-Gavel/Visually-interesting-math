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
from matplotlib.colors import ListedColormap

_length = 1000
_rgb_array = np.zeros((_length, 4))
_rgb_array[:,0] = np.linspace(0, 1, _length)
_rgb_array[:,1] = np.linspace(0, 0.9, _length)
_rgb_array[:,3] = 1
_YlBl = ListedColormap(_rgb_array, name = 'YlBl')

def _adjust_folder_path(folder_path):
   if folder_path[-1] != '/':
      folder_path += '/'
   return folder_path
   
def _adjust_steps(p_range, p_steps):
   """
   If we have symmetric intervals, we want to make sure that the real
   and imaginary axes are plotted.
   """
   if abs(p_range[0]) == abs(p_range[1]):
      p_steps += (p_steps + 1) % 2
   return p_steps

def _make_complex_plane(real_axis, imag_axis):
   complex_plane = np.meshgrid(real_axis, imag_axis)
   complex_plane = np.asarray(complex_plane)   
   complex_plane = complex_plane[0,:,:] + 1j * complex_plane[1,:,:]
   return complex_plane

def plot_given_flags(real_axis, imag_axis, divergence_time, plot_path, color, blank_undiverged, log_scale, optimise_width):
   plt.axis('off')
   fig = plt.gcf()
         
   if blank_undiverged:
      mask = np.where(np.isinf(divergence_time))
      plot_array = np.copy(divergence_time)
      plot_array[mask] = 1
   else:
      plot_array = divergence_time
         
   if color:
      cmap = _YlBl
   else:
      cmap = 'gist_gray'
         
   if log_scale:
      plt.pcolormesh(real_axis, imag_axis, plot_array, shading = 'nearest', cmap = cmap, norm=LogNorm())
   else:
      plt.pcolormesh(real_axis, imag_axis, plot_array, shading = 'nearest', cmap = cmap)

   if optimise_width:
      real_convergence_sum = np.where(np.isinf(np.sum(divergence_time, 0)))[0]
      imag_convergence_sum = np.where(np.isinf(np.sum(divergence_time, 1)))[0]
      if len(real_convergence_sum) != 0:
         x_left, x_right = real_axis[real_convergence_sum[0]], real_axis[real_convergence_sum[-1]]
         y_low, y_high = imag_axis[imag_convergence_sum[0]], imag_axis[imag_convergence_sum[-1]]   
      else:
         print('Converged nowhere!')
         x_left, x_right, y_low, y_high = real_axis[0], real_axis[-1], imag_axis[0], imag_axis[-1]
   else:
      approx_screen_height = 14.
      x_left, x_right, y_low, y_high = real_axis[0], real_axis[-1], imag_axis[0], imag_axis[-1]
      fig.set_size_inches((x_right-x_left)/(y_high-y_low) * approx_screen_height, approx_screen_height)
      plt.xlim(x_left, x_right)
      plt.ylim(y_low, y_high)

   this_plot_path = plot_path
   if not optimise_width:
      this_plot_path += '-fixed_width'
   if color:
      this_plot_path += '-color'
   if blank_undiverged:
      this_plot_path += '-undiverged_blanked'
   if log_scale:
      this_plot_path += '-log_scale'
   plt.savefig('{}.png'.format(this_plot_path), format = 'png', bbox_inches = 'tight', dpi=400)
   plt.close()
   return

def standard_plot(real_axis, imag_axis, divergence_time, plot_path):
   for color in [True, False]:
      for blank_undiverged in [True, False]:
         for log_scale in [True, False]:
            for optimise_width in [True, False]:
               plot_given_flags(real_axis, imag_axis, divergence_time, plot_path, color, blank_undiverged, log_scale, optimise_width)
   return

def divergence_fractal(function, plot_folder_path, x_range, y_range, x_steps = 101, y_steps = 101, iterations = 100):
   """
   Given a function f(z), plot which points c on the complex plane diverge
   under repeated iteration of f_n(z) = f_n-1(z) + c, f_0 = c.
   """
   x_steps = _adjust_steps(x_range, x_steps)
   y_steps = _adjust_steps(y_range, y_steps)
   real_axis = np.linspace(x_range[0], x_range[1], x_steps)
   imag_axis = np.linspace(y_range[0], y_range[1], y_steps)
   
   complex_plane = _make_complex_plane(real_axis, imag_axis)
   z = np.zeros((x_steps, y_steps), dtype = np.clongdouble)
   divergence_time = np.ones((x_steps, y_steps), dtype = np.longdouble) * np.inf
   
   for i in range(1, iterations+1):
      diverged = np.abs(z) > 2
      not_diverged = np.logical_not(diverged)      
      z[not_diverged] = function(z[not_diverged]) + complex_plane[not_diverged]
      divergence_time[diverged] = np.minimum(divergence_time[diverged], i)
   return real_axis, imag_axis, divergence_time

def multibrot(plot_folder_path, d = 2, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
   """
   Plots the Mandelbrot set, or a generalisation with arbitrary exponent d.
   """
   plot_folder_path = _adjust_folder_path(plot_folder_path)
   
   multibrot_function = lambda z : z**d
   real_axis, imag_axis, divergence_time = divergence_fractal(multibrot_function, plot_folder_path, x_range, y_range, x_steps = x_steps, y_steps = y_steps, iterations = iterations)
   standard_plot(real_axis, imag_axis, divergence_time, "{}multibrot_{}".format(plot_folder_path, d))
   return

def mandelbar(plot_folder_path, d = 2, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
   """
   Plots the Mandelbar set, or a generalisation with arbitrary exponent d.
   """
   plot_folder_path = _adjust_folder_path(plot_folder_path)
      
   mandelbar_function = lambda z : np.conjugate(z)**d
   real_axis, imag_axis, divergence_time = divergence_fractal(mandelbar_function, plot_folder_path, x_range, y_range, x_steps = x_steps, y_steps = y_steps, iterations = iterations)
   standard_plot(real_axis, imag_axis, divergence_time, "{}mandelbar_{}".format(plot_folder_path, d))
   return
   
def burning_ship(plot_folder_path, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
   """
   Plots the Burning ship fractal
   """
   plot_folder_path = _adjust_folder_path(plot_folder_path)
      
   burning_ship_function = lambda z : (np.abs(np.real(z)) + 1j * np.abs(np.imag(z)))**2
   real_axis, imag_axis, divergence_time = divergence_fractal(burning_ship_function, plot_folder_path, x_range, y_range, x_steps = x_steps, y_steps = y_steps, iterations = iterations)
   standard_plot(real_axis, imag_axis, divergence_time, "{}burning_ship".format(plot_folder_path))
   return
   
def normal_julia(plot_folder_path, c = 0.0, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
   """
   Using the default value of c will produce a unit circle.
   """
   plot_folder_path = _adjust_folder_path(plot_folder_path)
   
   x_steps = _adjust_steps(x_range, x_steps)
   y_steps = _adjust_steps(y_range, y_steps)
   real_axis = np.linspace(x_range[0], x_range[1], x_steps)
   imag_axis = np.linspace(y_range[0], y_range[1], y_steps)
   z = _make_complex_plane(real_axis, imag_axis)
   divergence_radius = 1./2 + np.sqrt(1./4 + np.sqrt(c) + np.abs(z))

   divergence_time = np.ones((x_steps, y_steps), dtype = np.longdouble) * np.inf      
   for i in range(1, iterations+1):
      diverged = np.abs(z) > divergence_radius
      not_diverged = np.logical_not(diverged)      
      z[not_diverged] = z[not_diverged]**2 + c
      divergence_time[diverged] = np.minimum(divergence_time[diverged], i)
   standard_plot(real_axis, imag_axis, divergence_time, "{}normal_julia".format(plot_folder_path))
   return
