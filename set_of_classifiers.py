


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")
#%%
x=np.array([-1,1,1,2])
y=np.array([1,-1,1,2])
z=np.array([1,1,0.5,0.5])

xoffset=-0.7
yoffset=-0.7
angle = np.linspace( 0 , 2 * np.pi , 150 ) 
radius = 2
xcircle = radius * np.cos( angle ) +xoffset
ycircle = radius * np.sin( angle )+yoffset

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.scatter(x,y,c=z)
ax.grid(True)
ax.axis([-6,6,-6,6])
ax.plot(xcircle,ycircle)
# %%
