import numpy as np
import matplotlib.pyplot as plt
from curvefitgui import curve_fit_gui

datafile = '$PATH/TO/FILE.csv'
csv = np.genfromtxt (datafile, delimiter=",")
y_data = csv[:,0]
y_data = np.delete(y_data, 0) #cut first word
x_data = csv[:,1]
x_data = np.delete(x_data, 0) #cut first word
#produce error
Y_ERROR=0
X_ERROR=0

err_y = y*(Y_ERROR)
err_x = x*(X_ERROR)
# define a function for fitting
def f(x, a, b):
    '''
    Linear fit
    function: y = ax + b
    a: slope
    b: intercept
    '''
    return a * x + b

# execute the function
curve_fit_gui(f, x_data, y_data, xerr=err_x, yerr=err_y, xlabel='Voltage (V)', ylabel='Current (A)')
