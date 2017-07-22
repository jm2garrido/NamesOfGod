#https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly

import matplotlib.pyplot as plt
import scipy
import scipy.optimize
import numpy as np
import math

def calcula(x,yn):
    cof1 = np.polyfit(x, np.log(yn), 1)
    #print(cof1)
    #y_cof1 = numpy.exp(cof1[1]+cof1[0]*x)

    y_cof1 = math.exp(cof1[1]) * (np.exp(cof1[0]*x))
    #print("{:f} * exp({:f} * x)".format(math.exp(cof1[1]),cof1[0]))
    #print(y_cof1)

    cof2, corr = scipy.optimize.curve_fit(lambda t,a,b: a*np.exp(b*t),  x,  yn,  p0=(0.0001, 0.2))
    #print(cof2)
    print("{:f} * exp({:f} * x)".format(cof2[0],cof2[1]))
    y_cof2 = cof2[0] * (np.exp(cof2[1]*x))
    print(y_cof2)

x = np.array([6,7,8,9])
yn = np.array([22,351,5617,89798])
calcula(x,yn)
# en AMD
#yn2 = np.array([130,1740,14840,248770])
#1.5
yn2 = np.array([30,440,6090,85446])
calcula(x,yn2)
#1.6
yn3 = np.array([24,355,5364,78183])
calcula(x,yn3)

plt.figure()
plt.semilogy(x, yn, 'o-', label="Data")
plt.semilogy(x, yn2, 'x-', label="Data 1.5")
plt.semilogy(x, yn3, '+-', label="Data 1.6")
#plt.plot(x, func(x, *popt), 'r-', label="Fitted Curve")
plt.legend(loc=2)
plt.show()
