import numpy as np
import matplotlib.pyplot as plt

def is_prime(c):
   if c < 2:
      return False
   for i in range(2, int(np.sqrt(c))+1):
      if c % i == 0:
         return False
   return True

def euler_formula(m):
   euler_formula_primes = []
   for i in range(0, m):
      k = i**2 + i + 41
      if is_prime(k):
         euler_formula_primes.append(k)
   return np.asarray(euler_formula_primes)

def make_square(n):
   def f(c):
      return int(np.floor(np.sqrt(c - 1)))
   def g(c):
      return int(np.floor(np.sqrt(c - 3/4) - 1/2))
   
   # Side length must be odd
   n += (n + 1) % 2
   euler_primes = euler_formula(n)
   
   number_square = np.zeros((n, n), dtype=np.double)
   prime_square = np.zeros((n, n), dtype=np.bool)
   euler_square = np.zeros((n, n), dtype=np.bool)
   x = n // 2
   y = n // 2
   for c in range(1, n**2 + 1):
      number_square[y,x] = c
      prime_square[y,x] = is_prime(c)
      euler_square[y,x] = c in euler_primes
      fc = f(c)
      gc = g(c)
      if fc % 2 == 1 and gc % 2 == 0:
         y += 1
      elif fc % 2 == 1 and gc % 2 == 1:
         x -= 1
      elif fc % 2 == 0 and gc % 2 == 1:
         y -= 1
      elif fc % 2 == 0 and gc % 2 == 0:
         x += 1
   return number_square, prime_square, euler_square

def plot_prime_square(plot_folder_path, n, mark_euler = False):
   # Side length must be odd
   n += (n + 1) % 2
   
   dummy, prime_square, euler_square = make_square(n)
   if mark_euler:
      plot_square = prime_square.astype(int) + euler_square.astype(int)
   else:
      plot_square = prime_square
   plt.pcolormesh(np.linspace(0., 1., n), np.linspace(0., 1., n), plot_square, shading = 'nearest', cmap = 'gist_gray')
   plt.gca().invert_yaxis() # I do *not* understand why printing matrices and plotting them follow opposite axis conventions.
   approx_screen_height = 14.
   plt.axis('off')
   fig = plt.gcf()
   fig.set_size_inches(approx_screen_height, approx_screen_height)
   plot_name = "{}".format(n)
   if mark_euler:
      plot_name += "_euler_shown"
   plt.savefig("{}/{}.png".format(plot_folder_path, plot_name), format = 'png', bbox_inches = 'tight', dpi=100)
   plt.close()
   return
