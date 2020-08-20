import matplotlib.pyplot as plt 
from scipy.optimize import minimize, rosen, rosen_der
import numpy as np
import pandas as pd
import random
import math

class Regression():              
       def random_array(self,iterations,randomx1,randomx2,randomy1,randomy2):
              self.observed_x = []
              self.observed_y = []
              for i in range(iterations):
                     valuex = random.uniform(randomx1,randomx2)
                     valuey = random.uniform(randomy1,randomy2)
                     self.observed_x.append(valuex)
                     self.observed_y.append(valuey)
              return self.observed_x,self.observed_y
       
       # To understand teta_a and teta_b look at a linear function:
       #      y=a*x+b
       # During this function a = teta_a and b = teta_b
       # X is predefined in 
      
       def logistic():
              h = 1/(1+math.exp(-np.transpose(theta)*x)

       def linear_plot(self,observed_x,observed_y,teta_a,teta_b,\
                       randomx1,randomx2,randomy1,randomy2,mae_error):
              x1 = []
              y1 = []
              for i in range(int(randomx1),int(randomx2)+1):
                     y = teta_a*i+teta_b
                     y1.append(y)
                     x1.append(i)
              plt.plot(x1,y1,color='red',label='Mae Error '+str(mae_error))
              plt.scatter(observed_x,observed_y,label = 'Dataset')
              plt.xlim(0,randomx2+5)
              plt.ylim(0,randomy2+5)
              plt.legend()
              plt.show()

       def polynomial_plot(self,observed_x,observed_y,observed_x2,observed_y2,\
                           observed_x3,observed_y3,teta_1,teta_2,teta_3):
              x1 = []
              y1 = []
              for i in range(0,15):
                     y = teta_1+teta_2*i + teta_3*(i**(1/2))
                     x1.append(i)
                     y1.append(y)
              plt.plot(x1,y1,color='red')
              plt.scatter(observed_x,observed_y,label = 'X1')
              plt.scatter(observed_x2,observed_y2,label = 'X2')
              plt.scatter(observed_x3,observed_y3,label = 'X3')
              plt.xlim(0,20)
              plt.ylim(0,100)
              plt.legend()
              plt.show()     
       

