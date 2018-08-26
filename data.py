#this is a comment

import pandas as pd
import matplotlib.pyplot as plt

XYZ = pd.read_csv('data.csv', sep=',')

TIME = XYZ['Time(s)']
X = XYZ['LINEAR ACCELERATION X (m/s2)']
Y = XYZ['LINEAR ACCELERATION Y (m/s2)']
Z = XYZ['LINEAR ACCELERATION Z (m/s2)']

plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs. Time')

plt.subplot(111)
plt.plot(TIME, X, 'b')

plt.subplot(111)
plt.plot(TIME, Y, 'g')

plt.subplot(111)
plt.plot(TIME, Z, 'r')
