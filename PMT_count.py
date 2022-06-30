#!/usr/bin/env python3

# This program does

# a) Has a function which simulates photon counting for 1000 one-millisecond
#   intervals, with the probability of a detection in each interval being 0.002.
#   The function should return the total number of detections.

# b) Plots a histogram displaying the result of calling the function 1000 times

# c) overlays on the plot, in a different color, a graph of the Poisson distribution 
#   with mean, standard deviation, and maximum value corresponding to this simulation.


import numpy as np
import random 
import matplotlib.pyplot as plt
import scipy.stats as stats


# This function counts two numbers out of 1000 possible
# numbers to choose from. If one of the two is chosen,
# 1 is added to the counting variable.

#NOTE- The two numbers choose for this program have no
#       special purpose.

def counting_photons(N):
    photon_num = 0
    for i in range(N+1):
        x = random.randint(0, 1000)
        if x in [271, 277]:
            photon_num += 1
        else:
            pass
    return photon_num

#num_photons = counting_photons(1000)
#print(num_photons)

# This functions calls the previous function
# 1000 times. After each call, it stores the output
# into a list, so it can later be plotted.

def counting_counted_photons(trials):
    outcome = []
    for i in range(trials):
        outcome.append(counting_photons(1000))
    return outcome


#Creating a Poisson Fit
outcome_lst = counting_counted_photons(1000)
mean = np.mean(outcome_lst)
data_max = np.max(outcome_lst)
sd = round(np.std(outcome_lst), 3)
print(data_max)

x = np.arange(0,5, 0.01)
pmf = stats.poisson.pmf(x, mean)

# Plotting
fig, ax = plt.subplots()

ax.plot(x,pmf, color='red')

ax.hist(outcome_lst, density=True, facecolor='g', alpha=0.75)

ax.set_title('Histogram of 1000 trials of \n counting photons for 1000 miliseconds')

ax.text(5,0.25,'Max Value: '+str(data_max)+'\n \u03BC = '+str(mean)+'\n \u03C3 = '+str(sd))
ax.set_xlabel('Number of Photons Counted')
ax.set_ylabel('Probability')
ax.grid(True)
plt.show()
