import matplotlib.pyplot as plt 
from scipy.optimize import minimize, rosen, rosen_der
import numpy as np
import pandas as pd
from random import randint
observed = []
x = []
for i in range(10):
       value = randint(5,10)
       observed.append(value)
       valuex = randint(5,10)
       x.append(valuex)

def linear_regression(observed,x):
       a = np.arange(-2,2,0.01)
       #b = np.arange(-5,5,1)
       mae_error1 = []
       j1 = []
       k1 = []
       #x = [1,2,3,4,5,6,7,8]
       a = -2
       b = -2      
       mae_error1 = [100000]
       for i in range(1,100):
              accumulated_error=0
              h1 = []
              for j in x:
                     h = a*j+b
                     h1.append(h)
              m = len(x)
              for prediction,target in zip(h1,observed):
                     accumulated_error += (prediction-target)**2
              mae_error = 1.0/(2*m)*accumulated_error
              mae_error1.append(mae_error)
              
              a+= 0.1
              b+= 0.1
              if mae_error1[i] > mae_error1[i-1]: #and mae_error1[i] < mae_error1[i+1]:# < mae_error1[i+1]:
                     return mae_error1[i-1],a,b            
mae_error,a,b = linear_regression(observed,x)
print(round(mae_error,2),'    ',round(a,2),'  ',round(b,2))

y1 = []
x1 = []
for i in range(5,11):
       y = a*i+b
       y1.append(y)
       x1.append(i)
plt.plot(x1,y1,color='red',label='Mae Error '+str(round(mae_error,2)))
plt.scatter(x,observed,label = 'Dataset')
plt.xlim(0,14)
plt.ylim(0,14)
plt.legend()
plt.show()
print(observed)
print(x)
