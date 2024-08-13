import numpy as np
from matplotlib import pyplot as plt

def logistic_plot(r, n: "iterations", x_0: "Intial value"):

    x = x_0

    logistic_plot_data = []

    for i in range(n): 
        
        y = r * x * (1-x)

        x = y

        logistic_plot_data.append(x)

    return logistic_plot_data[200:] #Ignoring the first 200 data points helps clean up any fringing effects

x_0=0.9
n=1000
for r in np.arange(1, 4, 0.001):
    plt.plot(r*np.ones(len(logistic_plot(r, n, x_0))), logistic_plot(r, n, x_0), ',k', alpha=0.1)

plt.xlabel('r')
plt.ylabel('x')
plt.title('Bifurcation Diagram')
plt.show()

