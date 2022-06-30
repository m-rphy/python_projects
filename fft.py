#!/usr/bin/env python3

#
# fft.py - Demonstrate power spectrum from discrete fft
#
# 25Jul22  William Murphy
#

FTIME = 1       # function range in seconds
FS = 920         # samples per second
npts = FTIME*FS  # number of sample points

import numpy as np
import matplotlib.pyplot as plt

#solar cell data into numpy array
sc_data = np.loadtxt('fft_data.txt')

#print(sc_data)

#plots the raw data
t = np.linspace(0, FTIME, npts)
y_raw = sc_data
y_fft = sc_data - np.mean(sc_data)
f1, ax1 = plt.subplots()
ax1.plot(t,y_raw)
ax1.set_title('Data Acquisition of Solar Cell')
ax1.set_xlabel('Sec')
ax1.set_ylabel('Voltage')
f1.show()

#Computng the FFT
ft = np.fft.fft(y_fft, n=16*npts)
ftnorm = abs(ft)
fs = ftnorm**2
ps = np.fft.fftshift(fs)
x_vals = np.fft.fftfreq(len(ps), 1.0/FS)
xvals = np.fft.fftshift(x_vals)

f2, ax2 = plt.subplots()
ax2.plot(xvals,ps)
ax2.set_xlim(0,200)
ax2.title.set_text('FFT of Raw Data')
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Amplitude')
f2.show()

input('\nPress <Enter> to exit...\n')
