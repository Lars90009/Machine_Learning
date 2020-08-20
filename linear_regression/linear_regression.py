import matplotlib.pyplot as plt 
from scipy.optimize import minimize, rosen, rosen_der
import numpy as np
import pandas as pd
import random

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
       def linear_regression(self,observed_x,observed_y,teta_a\
                             ,teta_b,learning_rate,maxIterations,global_optimum):
              print('Linear Regression Function')
              mae_error1 = [100]
              a1 = []
              b1 = []
              accumulated_errorpractice = 0
              for i in range(0,maxIterations):
                     
                     accumulated_error = 0
                     derivative_error_teta_a = 0
                     derivative_error_teta_b = 0
                     m = len(observed_x)
                     
                     h1 = []
                     if linear == True:
                            for j in observed_x:
                                   h = teta_a*j+teta_b
                                   h1.append(h)
                     elif logistic == True:
                            for j in observed_x:
                                   h = 1/(1+math.exp(-np.transpose(teta)*x))
                     for prediction,target,x_axis in zip(h1,observed_y,observed_x):
                            accumulated_error += (prediction-target)**2
                            derivative_error_teta_a += (prediction-target)*x_axis
                            derivative_error_teta_b += (prediction-target)
                     #print(accumulated_error)
                     mae_error = 1.0/(2*m)*accumulated_error
                     #print(mae_error)
                     mae_error1.append(mae_error)
                     
                     a1.append(teta_a)
                     b1.append(teta_b)
                     print(i,mae_error1[i],mae_error1[i+1],a1[i])
                     if mae_error == 0.0:
                            return mae_error,teta_a,teta_b
                     elif i == maxIterations-1:
                            print('Maximum number of iterations is reached :',i)
                            print(mae_error,teta_a,teta_b)
                            return(mae_error,teta_a,teta_b)
                     elif mae_error1[i] - mae_error1[i+1] < 0.001:
                            print('Global Minimum at iteration number : ',i)
                            return(mae_error,teta_a,teta_b)
                     else:
                            teta_a -= learning_rate*(1.0/m)*derivative_error_teta_a
                            teta_b -= learning_rate*(1.0/m)*derivative_error_teta_b
                     
       def linear_regression_vector(self,observed_x,observed_y,teta_a\
                             ,teta_b,learning_rate,maxIterations,global_optimum):
              print('Linear Regression Function')
              mae_error1 = [100]
              a1 = []
              b1 = []
              accumulated_errorpractice = 0
              for i in range(0,maxIterations):
                     print(i)
                     accumulated_error = 0
                     derivative_error_teta_a = 0
                     derivative_error_teta_b = 0
                     m = len(observed_x)
                     observed_x = np.array(observed_x)
                     h = teta_a*observed_x+teta_b
                     h,observed_y,observed_x
                     mae_error = 1.0/(2*m)*sum((h-observed_y)**2)
                     derivative_error_teta_a = sum((h-observed_y)*observed_x)
                     derivative_error_teta_b = sum((h-observed_y))
                     teta_a -= learning_rate*(1.0/m)*derivative_error_teta_a
                     teta_b -= learning_rate*(1.0/m)*derivative_error_teta_b

                     a1.append(teta_a)
                     b1.append(teta_b)
                     mae_error1.append(mae_error)
                     print(mae_error1[i])
                     if mae_error1[i] - mae_error1[i+1] < 0.001:
                            break
                     else:
                            continue
              mae_error,teta_a,teta_b = mae_error1[i-1],a1[i],b1[i]
              return mae_error,teta_a,teta_b
              '''
              if mae_error == 0.0:
                     return mae_error,teta_a,teta_b
              elif mae_error1[i-1] - mae_error1[i] > 0.001:
                     print('Global Minimum at iteration number : ',i)
                     return(mae_error,teta_a,teta_b)                    
              '''

       #For obtained output of the linear regression, you are able to obtain a
       # predicted value based on the linear function
       def linear_result(self,teta_a,teta_b,x_value):
              y_value = teta_a*x_value + teta_b
              return y_value
               

       def linear_regression_NE(self,observed_x0,observed_y0,observed_x1,\
                                observed_x2):
              #print('Linear Regression Function with the Normal Equation')
              X = np.transpose(np.matrix([observed_x0,observed_x1,observed_x2]))
              print(X)
              A = 1/(np.transpose(X)*X)
              #print(A)
              Y = np.transpose([observed_y0])
              print(Y)
              B = np.transpose(X)*Y
              #print(B)
              teta = A*B
              print(teta)
                     
              teta_1,teta_2,teta_3 = round(teta.item(0),2),round(teta.item(1),2),\
                                     round(teta.item(2),2)
              #print(teta_1,teta_2,teta_3)
              return teta_1,teta_2,teta_3

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
       

