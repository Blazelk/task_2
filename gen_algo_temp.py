%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def polynomial_creator(*coeffs):
    """ coefficients are in the form a_n, a_n_1, ... a_1, a_0
    """
    def polynomial(x):
        res = coeffs[0]
        for i in range(1, len(coeffs)):
            res = res * x + coeffs[i]
        return res
    return polynomial

def polynomial_plotter(polynomial, domain, num_points=100, show_plot = True):
    """ plots the polynomial in the given range with the give number of points
    """
    start, stop = domain
    points = np.linspace(start, stop,num_points)
    func_values = polynomial(points)
    plt.plot(points, func_values)
    if show_plot:
        plt.show()

def multi_creator(*coefs):
    def multivariate_function(x, i):
        poly = polynomial_creator(coefs[i])
        return poly(x)
    #ASSUMING WE PASS A LIST AS ARGUMENTS
    def multinomial_function(y):
        func = 0
        for i in coefs.shape(0)
            func = func + multivariate_function(y[i], i)
        return func
    return multinomial_function

