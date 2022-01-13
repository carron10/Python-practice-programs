import cmath
import numpy as np
import matplotlib.pyplot as plt
from sympy.plotting import plot3d
from mpl_toolkits import mplot3d
#variables
u1=np.linspace(-2,2,60);
v1=np.linspace(0,2*np.pi,60);
u2=np.linspace(0,np.pi,60);
v2=np.linspace(0,2*np.pi,60);
[u1,v1]=np.meshgrid(u1,v1);
[u2,v2]=np.meshgrid(u2,v2);
fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')

# Two fold Hyperboloid in parametric format

x1 = 2*np.sinh(u1)*np.cos(v1)
y1 = 5*np.sinh(u1)*np.sin(v1)
z1 = 1*np.cosh(u1)

#Ellipsoid in parametric format

x2 = 2*(np.sin(u2)*np.cos(v2))
y2 = 5*(np.sin(u2)*np.sin(v2))
z2 = 1*(np.cos(u2))

# plot for hyperboloid
ax.plot_surface( z1, y1, x1,cstride = 1,color='c')
ax.plot_surface(-z1, y1, x1,cstride = 1,color='c')

#plot for ellipsoid
ax.plot_surface(z2, y2, x2,cstride = 1,color='r')
plt.show()
