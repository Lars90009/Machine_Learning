import matplotlib.pyplot as plt 
from scipy.optimize import minimize, rosen, rosen_der
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

x1 = [0.1,1.0,0.5,0.4,-0.2,0.5,-1.2,-1.1,1.0]
x2 = [1.0,0.4,0.3,0.2,-0.5,0.1,-1.2,-1.3,1.55]

fig, ax = plt.subplots()
def color_plot():
       for i,i2 in zip(x1,x2):
              print(i)
              if i**2+i2**2 <= 1:
                     #ax.scatter(i,i2,color='red')
                     ax.scatter(i**2+i2**2,-1,color='red')
              elif i**2+i2**2 >= 1:
                     ax.scatter(i,i2,color='blue')

def circle_plot():
       for i  in range(-1,2):
              for i2 in range(-1,2):
                     plt.scatter(i,i2)
       circle_plot()

def cost_function():
       observed = 0.2
       
       prediction = np.arange(0.01,1,0.01)
       cost_result = []
       for i in prediction:
              accumulated_error = 0
              cost = -observed*math.log(i)-(1-observed)*math.log(1-i)
              ax.scatter(i,cost,color='blue')
              cost_result.append(cost)
              
       #print(min(cost_result))
cost_function()
#ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.show()
