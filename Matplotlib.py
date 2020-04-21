import matplotlib.pyplot as plt
import numpy as np
import serial
import time

N = 400
data = np.arange(0, N, 1.0)
x = np.arange(0, N, 4.0)
y = np.arange(1, N, 4.0)
z = np.arange(2, N, 4.0)
Tilt = np.arange(3, N, 4.0)
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200)

for i in range(N):
    line = s.readline()
    data[i] = float(line)
    #print(data[i])

for i in range(100):
    x[i] = data[4*i]
    y[i] = data[4*i + 1]
    z[i] = data[4*i + 2]
    Tilt[i] = data[4*i + 3]
    #print(Tilt[i])


'''for i in range(100):
    x.append(data[4*i])
    y.append(data[4*i + 1])
    z.append(data[4*i + 2])
    Tilt.append(data[4*i + 3])
'''
Time = np.arange(0.1, 10.1, 0.1)
#print(len(x), len(y), len(z), len(Tilt))
#print(x.shape)
#print(y.shape)
#print(z.shape)
#print(Tilt.shape)
#print(Time.shape)
#print(data)
#print(data.shape)

'''fig, ax = plt.subplots(2, 1)
ax[0].plot(Time, x, color = 'blue', label = "x")
ax[0].plot(Time, y, color = 'red', label = "y")
ax[0].plot(Time, z, color = 'green', label = "z")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Acc Vector")
ax[1].plot(Time, Tilt, "o")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Tilt")'''


plt.subplot(211)
plt.plot(Time, x, color = "blue", label = "x")
plt.ylim(-1.5, 1.5)
plt.plot(Time, y, color = "red", label = "y")
plt.plot(Time, z, color = "green", label = "z")
plt.xlabel("Time")
plt.ylabel("Acc Vector")
plt.legend(loc = 'lower left')

plt.subplot(212)
plt.plot(Time, Tilt, "o")
plt.ylim(0, 1)
plt.xlabel("Time")
plt.ylabel("Tilt")

plt.show()
s.close