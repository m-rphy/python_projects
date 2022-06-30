#!/usr/bin/env python3

# William Murphy
# 22May22

# This program compares optimizxation techniques
# on computing the mandelbrot set, and computes a
# super hi-resolution plot with the most optimized
# method

import time
import numpy as np
import numexpr as ne
import multiprocessing as mp
import matplotlib.pyplot as plt
from matplotlib import cm

# Parameters of all the funcitons run

x_min = -00.73
x_max = -0.805
y_min = 0.01
y_max = 0.17

x_mid = (x_max - x_min)/2
y_mid = (y_max - y_min)/2

width = 512
height = 384
max_iter = 1000

width_a = 1024
height_a = 768

width_b = 4096*2
height_b = 3072*2

h_width = width//2
h_height = height//2

# List for storing data to be plotted
processes_lst = []

iter_lst = range(100,2001,100)

timeit_lst_serial = []
timeit_lst_vect = []
timeit_lst_static = []
timeit_lst_ne = []

timeit_lst_seriala = []
timeit_lst_vecta = []
timeit_lst_statica = []
timeit_lst_nea = []

#This line makes sure that the the data is sectioned in the middle
num_cpu = 4

# Computes the mandelbrot/ parts of the set
# This is the same program that was turned for p5_hw5

def mandel_serial(x_min, x_max, y_min, y_max, width, height, max_iter):

	mandel_arr = np.ones((width, height, 3), dtype='uint8')

	# Need to comput half the array since it's broken up
	re = np.linspace(x_min, x_max, width)
	im = np.linspace(y_min, y_max, height)
	
	color_arr = np.array(([1,1,1,1]))
	color_sch = cm.get_cmap('magma')
	
	for i in range(width):
		for k in range(height):
			c = complex(re[i],im[k])
			m, z = 0, 0
			while abs(z) <= 2 and m <= max_iter:
				z = z*z + c
				m += 1
			color = round(float(1-(m/max_iter)), 2)
			pix_color = color_arr * color_sch(color)*255
			mandel_arr[i,k,:] = pix_color[0:3].astype(int)

	return mandel_arr

# Everything below is for Multiprocessing/Optimization

#############################################################################

# Vectorized version of the mandel_serial

def mandel_vect(x_min, x_max, y_min, y_max, width, height, max_iter):

    re = np.linspace(x_min, x_max, width).reshape((1, width))
    im = np.linspace(y_min, y_max, height).reshape((height, -1))	
    c = re + 1j * im
    z = np.zeros(c.shape, dtype='complex128')

    # Keeping track of how many iterations it to diverge
    div_num = np.zeros(c.shape, dtype=int)

    # Keeping this for loop as small as possible and using arrays
    # and array indexing to do all computation in parallel and
    # in C

    for i in range(max_iter):
        in_set = np.less(z.real*z.real+z.imag*z.imag, 3)
        div_num[in_set] = i
        z[in_set] = z[in_set]**2 + c[in_set]

    return div_num

##############################################################################

# This is a helper function to place the data in a dictionary and process it at the same time
# This is known as inter process communication

def data_queue( x_min, x_max, y_min, y_max, width, height, max_iter, Queue, key):
	mandel_arr = mandel_vect(x_min, x_max, y_min, y_max, width, height, max_iter)
	return Queue.put({key : mandel_arr})

# The function that parallelizes the processing

def mandel_static_mp(x_max, x_min, y_min, y_max, width, height, max_iter):
	# Using a queue to organize data	
    mandel_data = mp.Queue()
    processes_lst = []

    # This dictionary organizes the data according to which core it was computed on
    data_dict = {}
    
    #min_iter = max_iter // 4 
	#Divides the compute power among the 4 cores of the ras-pi

    p0 = mp.Process(target=data_queue, args=(x_min, x_min + x_mid, y_min, y_min + y_mid, width, height, max_iter, mandel_data, 0))
    p0.start()
    processes_lst.append(p0)
				
    p1 = mp.Process(target=data_queue, args=(x_min + x_mid, x_max, y_min, y_min + y_mid, width, height, max_iter, mandel_data, 1))
    p1.start()
    processes_lst.append(p1)

    p2 = mp.Process(target=data_queue, args=(x_min, x_min + x_mid, y_min + y_mid, y_max, width, height, max_iter, mandel_data, 2))
    p2.start()
    processes_lst.append(p2)

    p3 = mp.Process(target=data_queue, args=(x_min + x_mid, x_max, y_min + y_mid, y_max, width, height, max_iter, mandel_data, 3))
    p3.start()
    processes_lst.append(p3)	

	# Getting the data from the dictionary ready to be joined
    for i in processes_lst:
        data_dict.update(mandel_data.get())
	
    bot_arr = np.concatenate((data_dict[0], data_dict[2]), axis=0)
    top_arr = np.concatenate((data_dict[1], data_dict[3]), axis=0)

    mandel_arr = np.concatenate((bot_arr,top_arr), axis=1)

    for p in processes_lst:
        p.join()	
	
    return mandel_arr

################################################################################

# This algorithm is very similar to my mandel_vect(), only now
# it uses numexpr to evaluate inside the for loop 

# using numexpr instead of numpy means that temporary arrays are 
# not created and arrays are processed on multiple cores.

def mandel_ne(x_min, x_max, y_min, y_max, width, height, max_iter):

    #Mapping the complex plane onto the area to be graphed
    re = np.linspace(x_min, x_max, width).reshape((1, width))
    im = np.linspace(y_min, y_max, height).reshape((height, -1))
    c = re + 1j * im

    # Initialize z to all zeros
    z = np.zeros(c.shape, dtype='complex128')

    # To keep track when the iteration diverged
    div_num = np.zeros(c.shape, dtype=int)

    # Keeping this for loop as small as possible, using numexpr
    # instead of numpy so temporary arrays are not created and
    # arrays are processed on multiple cores.
    for i in range(max_iter):
        in_set = ne.evaluate('z.real**2 + z.imag**2 < 2')
        div_num[in_set] = i
        z = ne.evaluate('where(in_set,z**2+c,z)')
    
    return div_num


# Program to compare functions

if __name__ == '__main__':

    # Makes the mandelbort set
    mandel_arr = mandel_ne(x_min, x_max, y_min, y_max, width_b, height_b, max_iter)


    string_for_data_output = '''
    for i in iter_lst:
        

        # Lower Resolution function calls

        t0 = time.perf_counter()
        mandel_serial(x_min, x_max, y_min, y_max, width, height, i)
        t1 = time.perf_counter()
        t_1 = t1 - t0
        timeit_lst_serial.append(t_1)

        ta = time.perf_counter()
        mandel_vect(x_min, x_max, y_min, y_max, width, height, i)
        tb = time.perf_counter()
        t_a = tb - ta
        timeit_lst_vect.append(t_a)

        t2 = time.perf_counter()
        mandel_static_mp(x_min, x_max, y_min, y_max, width, height, i)
        t3 = time.perf_counter()
        t_2 = t3 - t2
        timeit_lst_static.append(t_2)

        t4 = time.perf_counter()
        mandel_ne(x_min, x_max, y_min, y_max, width, height, i)
        t5 = time.perf_counter()
        t_3 = t5 - t4
        timeit_lst_ne.append(t_3)

        # Higher Resolution function calls

        t0a = time.perf_counter()
        mandel_serial(x_min, x_max, y_min, y_max, width_a, height_a, i)
        t1a = time.perf_counter()
        t_1a = t1a - t0a
        timeit_lst_seriala.append(t_1a)

        tc = time.perf_counter()
        mandel_vect(x_min, x_max, y_min, y_max, width_a, height_a, i)
        td = time.perf_counter()
        t_b = td - tc
        timeit_lst_vecta.append(t_b)

        t2a = time.perf_counter()
        mandel_static_mp(x_min, x_max, y_min, y_max, width_a, height_a, i)
        t3a = time.perf_counter()
        t_2a = t3a - t2a
        timeit_lst_statica.append(t_2a)

        t4a = time.perf_counter()
        mandel_ne(x_min, x_max, y_min, y_max, width_a, height_a, i)
        t5a = time.perf_counter()
        t_3a = t5a - t4a
        timeit_lst_nea.append(t_3a)

    '''

    fig, ax = plt.subplots()#(1,2)
    
    string_plotting_figures = '''
    fig.suptitle('Compute times for various methods of computing the mandelbrot set')

    #Lower resolutions data plot

    p1, =ax[0].plot(iter_lst, timeit_lst_serial,label="Serial")
    pa, =ax[0].plot(iter_lst, timeit_lst_vect,label="Vectorized Serial")
    p2, =ax[0].plot(iter_lst, timeit_lst_static,label="Static Multiprocessing")
    p3, =ax[0].plot(iter_lst, timeit_lst_ne,label="NumExpr")
    ax[0].set_title('Low Resolution')
    ax[0].set_xlabel('Interations')
    ax[0].set_ylabel('Time Elapsed (s)')
    ax[0].legend(loc='best')


   # Higher resolution data plot
    
    p1a, =ax[1].plot(iter_lst, timeit_lst_seriala,label="Serial")
    pb, =ax[1].plot(iter_lst, timeit_lst_vecta,label="Vectorized Serial")
    p2a, =ax[1].plot(iter_lst, timeit_lst_statica,label="Static Multiprocessing")
    p3a, =ax[1].plot(iter_lst, timeit_lst_nea,label="NumExpr")
    
    ax[1].set_title('High Resolution')
    ax[1].set_xlabel('Interations')
    ax[1].set_ylabel('Time Elapsed (s)')
    ax[1].legend(loc='best')
'''
    sup_hi_res = mandel_ne(x_min, x_max, y_min, y_max, width_a, height_a, 1000)
    ax.axis('off')
    ax.imshow(sup_hi_res, cmap='magma')

    plt.show()



