#Linear Reg + Poly Reg
#Submitted April 2018
#last edited 06/08/2020 (for descriptive purposes)
#
#Given: a dataset where each point has 3 values.
#  The middle value is the frequency, or essentially the group it belongs to
#I can't recall what t[] and s[] represented but they were basically (x,y) pairs
#
#Going in, I knew one frequency had to be linear, one had to be quadratic, and the rest was nonsense
#If there was a strong enough correlation (>.7) between a frequency's x & y values, then it had to be one of the two that made sense
#
#Output: Color-coded graph of points, with both a linear regression and poly regression on the two that made sense

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import time

def linear(a, b):
    slope = np.corrcoef( a, b )[0][1] * np.std( b ) / np.std( a )
    b = np.mean(b) - ( np.mean(a) * slope )
    y = []
    for i in range(0, 100):
        y.append((slope*i) + b)
    return y


data = open("PuceFinch.csv", 'r')
data = data.read()
data = data.split("\n")
data.pop()
freq = []
t = []
s = []

for line in data:
    line = line.split(',')
    line = np.float32(line)
    t.append(line[0])
    freq.append(line[1])
    s.append(line[2])

ufreq = list(set(freq))
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []

for i in range(0, len(t)):
    if freq[i] == ufreq[0]:
        x1.append(t[i])
        y1.append(s[i])
    if freq[i] == ufreq[1]:
        x2.append(t[i])
        y2.append(s[i])
    if freq[i] == ufreq[2]:
        x3.append(t[i])
        y3.append(s[i])
    if freq[i] == ufreq[3]:
        x4.append(t[i])
        y4.append(s[i])
    if freq[i] == ufreq[4]:
        x5.append(t[i])
        y5.append(s[i])

x = np.linspace(0, 100, 100)
deg = 4
linreg = []
polyreg = []

if np.abs(np.corrcoef(x1,y1)[0][1]) > .7:
    linreg.append(linear(x1,y1))
    polyreg.append(np.polyval(np.polyfit(x1, y1, deg), x))
if np.abs(np.corrcoef(x2,y2)[0][1]) > .7:
    linreg.append(linear(x2,y2))
    polyreg.append(np.polyval(np.polyfit(x2, y2, deg), x))
if np.abs(np.corrcoef(x3,y3)[0][1]) > .7:
    linreg.append(linear(x3,y3))
    polyreg.append(np.polyval(np.polyfit(x3, y3, deg), x))
if np.abs(np.corrcoef(x4,y4)[0][1]) > .7:
    linreg.append(linear(x4,y4))
    polyreg.append(np.polyval(np.polyfit(x4, y4, deg), x))
if np.abs(np.corrcoef(x5,y5)[0][1]) > .7:
    linreg.append(linear(x5,y5))
    polyreg.append(np.polyval(np.polyfit(x5, y5, deg), x))


plt.scatter(x1,y1, color = "orangered")
plt.scatter(x2,y2, color = "gold")
plt.scatter(x3,y3, color = "green")
plt.scatter(x4,y4, color = "steelblue")
plt.scatter(x5,y5, color = "mediumorchid")
plt.plot(x, linreg[0], color = "red")
plt.plot(x, linreg[1], color = "red")
plt.plot(x, polyreg[0], color = "blue")
plt.plot(x, polyreg[1], color = "blue")
plt.show()
