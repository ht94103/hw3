import matplotlib.pyplot as plt
import numpy as np
import serial
import time

N = 400
data = np.arange(0, N, 1)
x = np.arange(0, N-1, 4)
y = np.arange(1, N, 4)
z = np.arange(2, N, 4)
Tilt = np.arange(3, N, 4)
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200)

'''for i in range(N):
    line = s.readline()
    data[i] = float(line)

for i in range(100):
    x[i] = data[4*i]
    y[i] = data[4*i + 1]
    z[i] = data[4*i + 2]
    Tilt[i] = data[4*i + 3]
'''
Time = np.arange(0, 10.1, 0.1)
#print(len(x), len(y), len(z), len(Tilt))
print(x.shape)
print(y.shape)
print(z.shape)
print(Tilt.shape)
#print(data)
print(data.shape)

plt.subplot(211)
plt.plot(Time, x, color = 'blue', label = "x")
plt.plot(Time, y, color = 'red', label = "y")
plt.plot(Time, z, color = 'green', label = "z")
plt.xlabel("Time")
plt.ylabel("Acc Vector")

plt.subplot(212)
plt.plot(Time, Tilt, "o")
plt.xlabel("Time")
plt.ylabel("Tilt")

plt.show()
s.close