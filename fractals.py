"""
This module is written for my own amusement. It contains a couple of
functions for plotting fractals. Some of the algorithms are taken from
the book The Science of Fractal Images.

Written by Alvin Gavel,

https://github.com/Alvin-Gavel/Demodigi
"""

from abc import ABC, abstractmethod

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

class divergence_fractal(ABC):
   """
   A set of points in the complex plane, defined by whether they diverge upon
   repeated iteration of some mathematical function
   """

   def __init__(self, name, plot_folder_path, x_limits = [-2, 2], y_limits = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
      self.name = name
      self.plot_folder_path = _adjust_folder_path(plot_folder_path)
      self.x_limits = x_limits
      self.y_limits = y_limits
      self.x_steps = self._adjust_steps(x_limits, x_steps)
      self.y_steps = self._adjust_steps(y_limits, y_steps)
      self.iterations = iterations
      
      self.real_axis = np.linspace(self.x_limits[0], self.x_limits[1], self.x_steps)
      self.imag_axis = np.linspace(self.y_limits[0], self.y_limits[1], self.y_steps)
   
      self.complex_plane = self._make_complex_plane()
      self.divergence_time = np.ones((self.x_steps, self.y_steps), dtype = np.longdouble) * np.inf
      
      self.defining_function = None
      self.z0 = None
      self.divergence_treshold = None
      return

   def _adjust_steps(self, p_limits, p_steps):
      """
      If we have symmetric intervals, we want to make sure that the real
      and imaginary axes are plotted.
      """
      if abs(p_limits[0]) == abs(p_limits[1]):
         p_steps += (p_steps + 1) % 2
      return p_steps

   def _make_complex_plane(self):
      complex_plane = np.meshgrid(self.real_axis, self.imag_axis)
      complex_plane = np.asarray(complex_plane)   
      complex_plane = complex_plane[0,:,:] + 1j * complex_plane[1,:,:]
      return complex_plane

   def run(self):
      """
      Perform repeated iteration of the function that defines the fractal.
      """

      z = self.z0[:]
      divergence_time = np.ones((self.x_steps, self.y_steps), dtype = np.longdouble) * np.inf
   
      for i in range(1, self.iterations+1):
         diverged = np.abs(z) > self.divergence_radius
         not_diverged = np.logical_not(diverged)      
         z[not_diverged] = self.defining_function(z[not_diverged], self.complex_plane[not_diverged])
         divergence_time[diverged] = np.minimum(divergence_time[diverged], i)
      self.divergence_time = divergence_time
      return

   def plot(self, color, blank_undiverged, log_scale, optimise_width):
      plt.axis('off')
      fig = plt.gcf()
         
      if blank_undiverged:
         mask = np.where(np.isinf(self.divergence_time))
         plot_array = np.copy(self.divergence_time)
         plot_array[mask] = 1
      else:
         plot_array = self.divergence_time
            
      if color:
         cmap = _YlBl
      else:
         cmap = 'gist_gray'
         
      if log_scale:
         plt.pcolormesh(self.real_axis, self.imag_axis, plot_array, shading = 'nearest', cmap = cmap, norm=LogNorm())
      else:
         plt.pcolormesh(self.real_axis, self.imag_axis, plot_array, shading = 'nearest', cmap = cmap)

      if optimise_width:
         real_convergence_sum = np.where(np.isinf(np.sum(self.divergence_time, 0)))[0]
         imag_convergence_sum = np.where(np.isinf(np.sum(self.divergence_time, 1)))[0]
         if len(real_convergence_sum) != 0:
            x_left, x_right = self.real_axis[real_convergence_sum[0]], self.real_axis[real_convergence_sum[-1]]
            y_low, y_high = self.imag_axis[imag_convergence_sum[0]], self.imag_axis[imag_convergence_sum[-1]]   
         else:
            print('Converged nowhere!')
            x_left, x_right, y_low, y_high = self.real_axis[0], self.real_axis[-1], self.imag_axis[0], self.imag_axis[-1]
      else:
         approx_screen_height = 14.
         x_left, x_right, y_low, y_high = self.real_axis[0], self.real_axis[-1], self.imag_axis[0], self.imag_axis[-1]
         fig.set_size_inches((x_right-x_left)/(y_high-y_low) * approx_screen_height, approx_screen_height)
         plt.xlim(x_left, x_right)
         plt.ylim(y_low, y_high)

      this_plot_path = self.plot_folder_path + self.name
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

   def plot_all(self):
      """
      Plot fractal for all combinations of flag settings.
      """
      for color in [True, False]:
         for blank_undiverged in [True, False]:
            for log_scale in [True, False]:
               for optimise_width in [True, False]:   
                  self.plot(color, blank_undiverged, log_scale, optimise_width)
      return


class multibrot(divergence_fractal):
   """
   The Mandelbrot set, or a generalisation with arbitrary exponent d
   """
   def __init__(self, name, plot_folder_path, d = 2, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
      divergence_fractal.__init__(self, name, plot_folder_path, x_range, y_range, x_steps, y_steps, iterations)   
      self.defining_function = lambda z, complex_plane_section : z**d + complex_plane_section
      self.z0 = np.zeros((self.x_steps, self.y_steps), dtype = np.clongdouble)
      self.divergence_radius = 2.
      return

class mandelbar(divergence_fractal):
   """
   The Mandelbar set, or a generalisation with arbitrary exponent d
   """
   def __init__(self, name, plot_folder_path, d = 2, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
      divergence_fractal.__init__(self, name, plot_folder_path, x_range, y_range, x_steps, y_steps, iterations)
      self.defining_function = lambda z, complex_plane_section : np.conjugate(z)**d + complex_plane_section
      self.z0 = np.zeros((self.x_steps, self.y_steps), dtype = np.clongdouble)
      self.divergence_radius = 2.
      return
   
class burning_ship(divergence_fractal):
   """
   The Burning ship fractal
   """
   def __init__(self, name, plot_folder_path, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
      divergence_fractal.__init__(self, name, plot_folder_path, x_range, y_range, x_steps, y_steps, iterations)
      self.defining_function = lambda z, complex_plane_section : (np.abs(np.real(z)) + 1j * np.abs(np.imag(z)))**2 + complex_plane_section
      self.z0 = np.zeros((self.x_steps, self.y_steps), dtype = np.clongdouble)
      self.divergence_radius = 2.
      return
   
class normal_julia(divergence_fractal):
   """
   A Julia set
   """
   def __init__(self, name, plot_folder_path, c = 0.0 + 0.0j, x_range = [-2, 2], y_range = [-2, 2], x_steps = 101, y_steps = 101, iterations = 100):
      divergence_fractal.__init__(self, name, plot_folder_path, x_range, y_range, x_steps, y_steps, iterations)
      self.defining_function = lambda z, complex_plane_section : z**2 + c
      self.z0 = self.complex_plane[:]
      self.divergence_radius = 1./2 + np.sqrt(1./4 + np.sqrt(c) + np.abs(self.complex_plane))
      return
