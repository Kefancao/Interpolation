import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import make_interp_spline

def ParametricSpline(Sx,Sy):
    '''
     x_cs, y_cs, t = ParametricSpline(Sx,Sy)

       Takes an array of x- and y-values, and returns a parametric
       cubic spline in the form of two piecewise-cubic data structures
       (one for the x-component and one for the y-component), as well as
       the corresponding parameter values.
       
       The splines use natural boundary conditions.

       Input:
        Sx   array of x-values
        Sy   array of y-values

       Output:
        x_cs function that evaluates the cubic spline for x-component
        y_cs function that evaluates the cubic spline for y-component
        t is the array of parameter values use for the splines

       Note that x_cs(t) and y_cs(t) give Sx and Sy, respectively.
    '''


    pts = len(Sx) # How many points?

    # Construct t array using the arclength method
    t = np.zeros(pts)
    t[0] = 0
    for i in range(1,pts):
        t[i] = t[i-1] + math.sqrt((Sx[i]-Sx[i-1])**2 + (Sy[i]-Sy[i-1])**2)
    # Construct the x-component spline
    x_cs = make_interp_spline(t, Sx)

    # Construct the y-component spline
    y_cs = make_interp_spline(t, Sy)


    return x_cs, y_cs, t


# This displays an image of my name!
item = plt.imread("nickname.jpeg")
fig, ax = plt.subplots()
ax.imshow(item)
plt.show()

# These are the (x, y) points that encode my name

k_vert = [(81.0380265490966, 106.59579719173826),
 (81.98210092490532, 207.61175540326838),
 (81.98210092490532, 358.6636555326593),
 (81.98210092490532, 480.44925001198067)]

k_curve = [(189.60657976709635, 125.47728470791208),
 (124.46544783629648, 200.05916039679886),
 (88.59062155556617, 292.5784492260508),
 (119.74507595725302, 386.98588680692006),
 (218.8728854171658, 472.89665500551115)]

e = [(377.47738055302636, 319.95660612450285),
 (450.17110749029575, 291.63437485024207),
 (509.64779316624333, 234.04583792591183),
 (511.5359419178608, 201.94730914841625),
 (479.43741314036515, 189.67434226290322),
 (455.8355537451479, 197.2269372693728),
 (403.91146307566976, 239.71028418076395),
 (374.64515742560025, 303.9073417357551),
 (371.8129342981741, 388.87403555853746),
 (397.30294244500885, 434.1896055973547),
 (447.33888436286963, 445.51849810705903),
 (506.8155700388173, 425.6929362150765),
 (568.1804044663824, 382.2655149278766)]

f_vert = [(858.9553122154598, 97.15505343365135),
 (744.722312742608, 108.4839459433556),
 (723.008602099008, 147.19099535151202),
 (723.008602099008, 308.62771361479855),
 (708.8474864618777, 480.44925001198067)]

f_in = [(724.8967508506254, 315.2362342454594),
 (752.2749077490776, 303.9073417357551),
 (791.9260315330428, 301.07511860832903),
 (809.8634446734079, 309.5717879906072)]


# Construct the splines for each segment
segments = [k_vert, k_curve, e, f_vert, f_in]
segment_x = [[first[0] for first in segment] for segment in segments]
segment_y = [[first[1] for first in segment] for segment in segments]

result = [ParametricSpline(segment_x[i],segment_y[i]) for i in range(len(segment_x))]
result_x = [item[0] for item in result]
result_y = [item[1] for item in result]
result_t = [item[2] for item in result]

# Plot the spline k_vert and the interpolation points
spacing = [np.linspace(time[0], time[-1], 1000) for time in result_t]
# plt.plot(x_cs_vert(xx), y_cs_vert(xx), label='x-component')
for i in range(len(spacing)):
	plt.plot(result_x[i](spacing[i]), result_y[i](spacing[i]), label='y-component')

# Use the same x- and y-axis as the original image
plt.axis('equal')
# Invert the y-axis for the right orientation
plt.gca().invert_yaxis()
# plot the original interpolation points
for i in range(len(segments)):
	plt.plot(segment_x[i], segment_y[i], 'ro')
plt.show()
