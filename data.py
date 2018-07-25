#this is a comment

import math
import pandas as pd
import matplotlib.pyplot as plt

XYZ = pd.read_csv('data.csv', sep=',')

Time = XYZ['Time(s)']
X = XYZ['LINEAR ACCELERATION X (m/s2)']
Y = XYZ['LINEAR ACCELERATION Y (m/s2)']
Z = XYZ['LINEAR ACCELERATION Z (m/s2)']

plt.subplot(311)
plt.plot(Time,X, 'b')

plt.subplot(312)
plt.plot(Time,Y, 'g')

plt.subplot(313)
plt.plot(Time,Z, 'r')


plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs. Time')




