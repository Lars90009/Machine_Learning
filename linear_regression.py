import matplotlib.pyplot as plt 
from scipy.optimize import minimize, rosen, rosen_der
import numpy as np
import pandas as pd
import random

iterations = 100
randomx1 = 1
randomx2 = 10
randomy1 = 1
randomy2 = 10
teta_a = 1
teta_b = 1

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
       def linear_regression(self,observed_x,observed_y,teta_a,teta_b):
              print('Linear Regression Function')
              learning_rate = 0.1
              mae_error1 = [10000]
              a1 = []
              b1 = []
              for i in range(1,10000):
                     accumulated_error = 0
                     derivative_error_teta_a = 0
                     derivative_error_teta_b = 0
                     m = len(observed_x)
                     
                     h1 = []
                     for j in observed_x:
                            h = teta_a*j+teta_b
                            h1.append(h)
                     
                     for prediction,target,x_axis in zip(h1,observed_y,observed_x):
                            accumulated_error += (prediction-target)**2
                            derivative_error_teta_a += (prediction-target)*x_axis
                            derivative_error_teta_b += (prediction-target)
                     mae_error = 1.0/(2*m)*accumulated_error
                     mae_error1.append(mae_error)
                     a1.append(teta_a)
                     b1.append(teta_b)
                     teta_a -= learning_rate*(1.0/m)*derivative_error_teta_a
                     teta_b -= learning_rate*(1.0/m)*derivative_error_teta_b
                     if mae_error1[i] > mae_error1[i-1]:
                            return(mae_error1[i-1],a1[i-1],b1[i-1])
                     
       def linear_plot(self,observed_x,observed_y,teta_a,teta_b,\
                       randomx1,randomx2,randomy1,randomy2):
              x1 = []
              y1 = []
              for i in range(int(randomx1),int(randomx2)+1):
                     y = teta_a*i+teta_b
                     y1.append(y)
                     x1.append(i)
              plt.plot(x1,y1,color='red',label='Mae Error '+str(round(mae_error,2)))
              plt.scatter(observed_x,observed_y,label = 'Dataset')
              plt.xlim(randomx1-5,randomx2+5)
              plt.ylim(randomy1-5,randomy2+5)
              plt.legend()
              plt.show()

observed_x,observed_y = Regression().random_array(iterations,randomx1,randomx2,randomy1,randomy2)
mae_error,a,b = Regression().\
                linear_regression(observed_x,observed_y,teta_a,teta_b)
print('Y=teta_a*x+teta_b: MAE error = ',round(mae_error,2),\
      'Teta_a =',round(a,2),'Teta_b = ',round(b,2))
plot = Regression().linear_plot(observed_x,observed_y,teta_a,teta_b,randomx1,randomx2,randomy1,randomy2)
