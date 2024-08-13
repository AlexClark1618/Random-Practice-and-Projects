import numpy as np
from matplotlib import pyplot as plt

def circle(theta, r):

    x = r * np.cos(theta)

    y = r * np.sin(theta)

    return x, y


def deltoid_curve(theta):

    x = 2 * np.cos(theta) + np.cos(2 * theta)

    y = 2 * np.sin(theta) - np.sin(2 * theta)

    return x, y

def plot_deltoid_curve():
    deltoid_plotting_data = [deltoid_curve(theta) for theta in np.linspace(0, 2*np.pi, num=100, endpoint=True)]
    x_data, y_data = zip(*deltoid_plotting_data)
    x_data = list(x_data)
    y_data = list(y_data)

    circle_plotting_data = [circle(theta, 3) for theta in np.linspace(0, 2*np.pi, num=100, endpoint=True)]
    x_circle_data, y_circle_data = zip(*circle_plotting_data)
    x_circle_data = list(x_circle_data)
    y_circle_data = list(y_circle_data)

    plt.plot(x_data, y_data)
    plt.plot(x_circle_data, y_circle_data)
    plt.grid()
    plt.show()

#plot_deltoid_curve()

def galilean_spiral(theta):

    r = theta**2

    x = r * np.cos(theta)

    y = r * np.sin(theta)

    return x, y

def plot_galilean_curve():
    galilean_plotting_data = [galilean_spiral(theta) for theta in np.linspace(0, 10*np.pi, num=500, endpoint=True)]
    x_data, y_data = zip(*galilean_plotting_data)
    x_data = list(x_data)
    y_data = list(y_data)

    plt.plot(x_data, y_data)
    plt.grid()
    plt.show()

plot_galilean_curve()

def feys_function(theta):

    r = np.exp(np.cos(theta)) - 2*np.cos(4*theta) + (np.sin(theta/12))**5
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)