import numpy as np
import matplotlib.pyplot as plt
import math


def Spline(x, y):
    '''
     S = MySpline(x, y)

     Input:
       x and y are arrays (or lists) of corresponding x- and y-values,
       specifying the points in the x-y plane.  The x-values
       must be in increasing order.

     Output:
       S is a function that takes x or an array (or list) of x-values
         It evaluates the cubic spline and returns the interpolated value.
    '''
    n = len(x)
    # 'h' here represents the gap between consecutive x-values
    h = np.zeros(n-1)
    # coefficient vectors
    a = np.zeros(n)
    b = np.zeros(n-1)
    c = np.zeros(n-1)
    M = np.zeros((n-2,n-2))
    r = np.zeros(n-2)
    
    # The h vector has its index starting at 1.
    for i in range(n-1):
        h[i] = x[i+1] - x[i]
    
    # Constructing the matrix to solve for a
    for i in range(n-2):
      start = 0 if i - 1 < 0 else i - 1
      end = n - 2 if i + 2 > n - 2 else i + 2
      for j in range(start, end):
        # Center
        if i == j:
          M[i][j] = (h[i] + h[i+1])/3
        # Left
        elif i == j+1:
          M[i][j] = h[i]/6
        # Right
        elif i == j-1:
          M[i][j] = h[i+1]/6
        else:
          M[i][j] = 0
    
    # Constructing the result vector. 
    for i in range(n - 2):
      r[i] = (y[i+2] - y[i+1])/h[i+1] - (y[i+1] - y[i])/h[i]

    # Solve for a using numpy linalg solve
    a[1:-1] = np.linalg.solve(M, r)

    for i in range(n-1):
      b[i] = y[i]/h[i] - a[i] * h[i]/6 
      c[i] = y[i+1]/h[i] - a[i+1] * h[i]/6
    #======================================
    #
    # This is the function that gets returned.
    # It evaluates the cubic spline at xvals.
    #
    #======================================
    def spline(xvals, x=x, a=a, b=b, c=c):
        '''
         S = spline(xvals)
         
         Evaluates the cubic spline at xvals.
         
         Inputs:
          xvals can be list-like, or a scalar (**must be in ascending order**)
          
         Output:
          S is a list of values with the same number of elements as x
        '''
        # Turn non-list-like input into list-like
        if type(xvals) not in (list, np.ndarray,):
            xvals = [xvals]
        
        S = []  # The return list of values
        
        # 
        k = 0   # this is the current polynomial piece
        hk = x[k+1] - x[k]

        for xx in xvals:

            # If the next x-value is not on the current piece...
            if xx>x[k+1]:
                # ... Go to next piece
                k += 1
                hk = x[k+1] - x[k]

            S_of_x = a[k]*(x[k+1]-xx)**3/(6*hk) + a[k+1]*(xx-x[k])**3/(6*hk) + b[k]*(x[k+1]-xx) + c[k]*(xx-x[k])

            S.append(S_of_x)
        
        return S
    #======================================
    
    return spline




# Below are some samples
# Simple data points to interpolate
# Feel free to change what t and y are and see what this function does!!!
t = range(0, 20)
y = [math.sin(x) for x in t]
# Call the function
sp = Spline(t,y)
# Plot the spline and the interpolation points
xx = np.linspace(t[0], t[-1], 100)
plt.plot(xx, sp(xx))
plt.plot(t,y,'ro')
plt.show()
