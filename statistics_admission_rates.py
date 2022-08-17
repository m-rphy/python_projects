#!/usr/bin/env python3


# This program is written as a kind of journal entry, accomplishing
# tasks that are labels a) - g)

# William Murphy
# 25May22


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import special


N = 787
N_a = 146


# a) The best estimate, P, of the admission probability, p_a, is N_a/N, so N_a = N*p.
#   A repeated admissions process with N as given above and actual admission 
#   probability equal to p will produce values for NA drawn from a distribution.
#   What is the standard deviation sigma_A of this distribution?

p_a = round(N_a/N, 3)
q_a = 1-p_a
mu_a = N*p_a
sigma_a = round(np.sqrt(N * p_a * q_a),3)
print('Calculated Standard Deviation is '+str(sigma_a)+' simga')
print(str(p_a)+'% is the approximate probability of getting in')
print('')

# b) What is the 1-standard deviation uncertainty in p corresponding to σA?

err_a = sigma_a/N
print('Standard Error is ±'+str(round(err_a, 4)))
print('')

approx_a = [p_a - err_a, p_a-err_a]

# c) Assume p is the exact admission probability. In other words, neglect the 
#   uncertainty calculated above. Using binom.pmf(), compute the probability 
#   that from a randomly selected group of 154 applicants, 48 or more are admitted.

n = 154
x = np.arange(0,n)

binom_dist = [stats.binom.pmf(i, n, p_a) for i in x]
prob_more_48 = round(np.sum(binom_dist[48:]), 6)

print('The Probability of letting in more than 48 applicants is '+str(prob_more_48))
print('')


# d) Usually (normally?), a Gaussian is a good approximation to a binomial 
#   distribution. However, sometimes you can run into trouble if you are looking 
#   at the tails of the distributions. Use erfc() to calculate the probability 
#   from the previous part using a Gaussian approximation. By what factor is the 
#   resulting answer too small?

#The Number of admissions
w = 48

#The expected number of admissions, and standard deviation
mu_c = n*p_a
sigma_c = np.sqrt(154*p_a*q_a)
print(sigma_c)
print('The expected mean is '+str(mu_c)+' and the standard deviation is '+str(sigma_c))

#Difference between measurement and expectation
outcome_diff = w - mu_c
print('The difference between the number of admissions \n and the expected mean value is '+str(outcome_diff))

sd_c = outcome_diff/sigma_c
print('That is a difference of :'+str(round(sd_c,5))+' stadard deviations')

#The erfc giving it gaussian approximation
erfc = 0.5 * special.erfc(sd_c)
print('The Complimentary Error Function: '+str(round(erfc, 11)))

#The order of magnitude the erfc is off by
mag_diff = np.log10(erfc) - np.log10(prob_more_48)
print('The gaussian approximation is off by '+str(round(mag_diff, 3))+' orders of magnitude')
print('')



# e) From a group of 154 applicants, 48 are admitted. Find the best estimate, 
#   p_g, of the admission probability for this group, and the 1-standard deviation 
#   uncertainty in p_g

n = 154
n_a = 48

#The best estimate is the measurement itself
p_g = n_a/n
q_g = 1- p_g
mu_g = n*p_g
sigma_g = np.sqrt(n*p_g*q_g)
err_g = sigma_g/n
approx_g = [round(p_g-err_g, 4), round(p_g + err_g, 4)]
print('The approximate probility of admission for the group with 154 applicants\n is between '+str(round(p_g,4))+' ± '+str(round(err_g,4)))


# f) Find the best estimate, p_n, for the admission probability of applicants not 
#   in the group of 154, and the corresponding 1-standard deviation uncertainty

# probability of a random applicant is selected from 633 applicants given prob is 
# 18% and 48 out of 154 have been selected already

# Number of students applications left after 154
N_n = N - n
# Approximate number of open positions minus the 48 already distributed
n_n = N*p_a - n_a


p_n = n_n/N_n
q_n = 1-p_n
mu_n = N_n*p_n
sigma_n = np.sqrt(N_n*p_n*q_n)
err_n = sigma_n/N_n

approx_n = [round(p_n-err_n, 4), round(p_n + err_n, 4)]

print('The approximate probility of admission for the group with '+str(N_n)+' applicants \n is between '+str(round(p_n,4))+' ± '+str(round(err_n,4)))


# g) Turn in a plot showing the three Gaussian approximations to the distributions 
#   of p_n , p, and p_g in different colors. Make the areas of the Gaussians 
#   proportional to the populations of the corresponding groups.

def normal_dist(x, mu, sigma):
    amp = (1/(sigma*np.sqrt(2*np.pi)))
    prob_density_func = amp * np.exp(-1*((x-mu)/(2*sigma))**2)
    return prob_density_func


x_633 = np.linspace(0, 633, 1000)
x_787 = np.linspace(0, 787, 1000)
x_154 = np.linspace(0, 154, 1000)

# p_n
pdf_n = (633/787)*normal_dist(x_633, 98, 9.9)

# p_g
pdf_g = (154/787)*normal_dist(x_154, mu_g, sigma_g)

# p
pdf_p = normal_dist(x_787, mu_a, sigma_a)

fig, ax = plt.subplots()

gaussian_1, = ax.plot(x_633, pdf_n, label='Group of 633')
gaussian_2, = ax.plot(x_787, pdf_p, label='Whole Group')
gaussian_3, = ax.plot(x_154, pdf_g, label='Group of 154')

ax.set_title('Gaussian Approximations \n for the Probability of Graduate School Admission')

ax.set_ylabel('Probability')
ax.set_xlabel('Number of Students')
ax.set_xlim(0,250)
ax.legend(loc='best')

plt.show()

