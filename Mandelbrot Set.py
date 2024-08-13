import numpy as np

x = np.linspace(-2, 2, 4)
y = np.linspace(-2, 2, 4)
X, Y = np.meshgrid(x, y)
c = X + 1j * Y
for value in c:
    print(value[:,0])

def mandelbrot_set(z_0, N: "grid size"):

    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y

    z = z_0

    for value in c:
        for i in range(100):
            z = z**2 + c

            if abs(z) > 2:
                
   