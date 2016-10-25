def plot_pos():
    from numpy import loadtxt, zeros, ones, array, linspace, logspace, arange, linalg
    import numpy as np
    from pylab import scatter, show, title, xlabel, ylabel, plot, contour
    import matplotlib.pyplot as plt

    # Load the dataset
    data = loadtxt('workshop_data.csv', delimiter=',')

    # assign the data arrays
    x = data[:, 0]
    y = data[:, 1]

    A = np.vstack([x, np.ones(len(x))]).T

    m, c = np.linalg.lstsq(A, y)[0]

    plt.plot(x, y, 'o', label='Original data', markersize=5)
    plt.plot(x, m*x + c, 'r', label='Fitted line')
    plt.legend()
    plt.show()
