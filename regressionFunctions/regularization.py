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

       def regularization(self,x0,observed_x,observed_x2,observed_y,teta\
                             ,learning_rate,maxIterations):
              teta = [1,1,2]
              matrix_x = [x0,observed_x,observed_x2]
              for i in range(0,maxIterations):
                     h1 = []
                     accumulated_error = 0
                     part_of_theta_J = 0
                     m = len(observed_x)
                     for i,j in zip(observed_x,observed_x2):
                            h = teta[0] + teta[1]*i + teta[2]*j
                            h1.append(h)
                     number_of_features = 3
                     labda = 0.1
                     for x in matrix_x:
                            for i,j in zip(teta,x):
                                   teta1 = []
                                   for prediction,target in zip(h1,
                                                 observed_y):
                                          accumulated_error += (prediction-target)**2\
                                                               +labda*i**2
                                          part_of_theta_J += (prediction-target)*j
                                          #print(part_of_theta_J)
                                   mae_error = 1.0/(2*m)*accumulated_error
                                   teta -= (i)*(1-learning_rate*(labda/m))\
                                          -learning_rate*(1/m)*np.transpose(part_of_theta_J)
                                   teta1.append(teta)
                            print(teta1)
              return 

       def normal_equation_reg(self,observed_x,observed_x2,observed_y):
              x0 = [1,1,1,1,1,1]
              X = np.matrix([np.transpose(x0),
                             np.transpose(observed_x),
                             np.transpose(observed_x2),
                             ])
              N=3
              res = np.eye(N)
              res[0,0]=0
              labda = 0.1
              A = np.transpose(X)*X
              print(A)
              teta = (1/(A+labda*res))*np.transpose(X)*observed_y
              print(teta)
x0 = [1,1,1,1,1,1]       
observed_x =  [1,2,3,4,5,6]
observed_x2 = [2,3,4,5,6,7]
observed_y =  [4,5,5,4,6,4]
teta = [1,1,1]
alpha = 0.01
maxIterations = 100
teta = Regression().regularization(x0,observed_x,observed_x2,observed_y,teta,alpha,maxIterations)
#NE = Regression().normal_equation_reg(observed_x,observed_x2,observed_y)
#print(NE)
