#Least Squares Variables
from matplotlib import pyplot as plt
import numpy as np

#Processing the data
data_list = []

with open('millikan.txt', 'r') as data_file:
    for line in data_file:
        parts = line.strip().split()

        data_tuple = (float(parts[0]), float(parts[1]))

        data_list.append(data_tuple)
    
x_data = [tup[0] for tup in data_list]
y_data = [tup[1] for tup in data_list]

#Variables
N = len(x_data)

def plot_raw_data(show_plot: bool):

    plt.scatter(x_data, y_data)
    plt.xlabel('Frequency')
    plt.ylabel('Energy')
    plt.title('Photoelectric Effect Raw Data')

    if show_plot==True:
        plt.show()

plot_raw_data(False)

def E_x(x_data, N):

    return (1 / N) * sum(x_data)

def E_y(y_data, N):

    return (1 / N) * sum(y_data)

def E_xx(x_data, N):

    squared_x_data = [x**2 for x in x_data]
    return (1 / N) * sum(squared_x_data)

def E_xy(x_data, y_data, N):

    xy_data = [x * y for x, y in zip(x_data, y_data)]
    return (1 / N) * sum(xy_data)

def m(x_data, y_data, N):

    return (E_xy(x_data, y_data, N) - (E_x(x_data, N) * E_y(y_data, N))) / (E_xx(x_data, N) - E_x(x_data, N)**2)

def c(x_data, y_data, N):

    return ((E_xx(x_data, N) * E_y(y_data, N)) - (E_x(x_data, N) * E_xy(x_data,y_data, N))) / (E_xx(x_data, N) - E_x(x_data, N)**2)

m = m(x_data, y_data, N)
c = c(x_data, y_data, N)

x_best_fit_data = [x for x in np.linspace(min(x_data), max(x_data), 100)]
y_best_fit_data = [(m*x + c) for x in x_best_fit_data]

plt.plot(x_best_fit_data, y_best_fit_data)
plt.show()