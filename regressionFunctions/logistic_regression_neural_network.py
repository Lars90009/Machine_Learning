import numpy as np
import math
import pandas as pd
import csv

###Two Nodes in a neural network that can, for example
### result in or/and/not functions

def or_and_not(theta,x):
       h_x = sigmoid(theta.dot(x))
       return h_x

def alpha3(teta_a,alpha0,alpha1,alpha2):
       teta = np.transpose(teta_a)
       h_x = []
       for i,j in zip(alpha1,alpha2):
              g_x = 1/(1-np.exp(-(teta[0]+teta[1]*i+teta[2]*j)))
              h_x.append(round(g_x))
       return h_x

### To Note for the cost function: it is essential to have
### a single dimension array for theta and y
def sigmoid(z):
       g = 1.0 / (1.0 + np.exp(-z))
       return g

def logistic_regression(theta,x,y,lambda_):
       m = len(y)
       h_x = sigmoid(theta.dot(x))
       J = 0
       sum_for_J = sum(-(y)*np.log(h_x)-(1-y)*np.log(1-h_x))
       reg_for_J = (lambda_/(2*m))*sum(theta[1:len(theta)]**2)
       J = (1/m)*sum_for_J + reg_for_J
       sum_for_grad = sum(x.dot(h_x-y))
       grad = (1/m)*sum_for_grad
       return J,grad,h_x

#Returns and
x0 = 1,1,1,1,1
x1 = 1,2,2,2,1
x2 = 1,0,1,1,1

x_or_1 = np.array([x0,x1,x2])
theta = -10,10,20
theta2 = -10,20,-20

x0 = 1,1,1,1,1
x1 = 1,1,1,1,1
x2 = 1,1,1,1,1

x_or_2 = np.array([x0,x1,x2])

or_0 = np.array(np.ones(len(x0)))
or_1 = or_and_not(np.array(theta),x_or_1)
or_2 = or_and_not(np.array(theta2),x_or_2)

teta_a = -10,20,-10

h_x = alpha3(teta_a,or_0,or_1,or_2)
print(h_x)
theta = [-10,-10,20]
theta = np.array(theta)
y = 0,1,2,1,0
y = np.array(y)
lambda_ = 0.1
#print(theta.shape)
#print(x_or_1.shape)
#print(y.shape)
range_array = np.arange(0,3,1)
theta = np.array(range_array)
#print(theta)
J,grad,h_x = logistic_regression(theta,x_or_1,y,lambda_)
print(J,grad,h_x)
#print('Theta0=',i,'Theta1=',j,'Theta2=',k,'h_x=',h_x)


### 
x0 = 1,1,1,1,1,1,1,1,1,1,1,1,1
x1 = 0,0,0,1,1,0,0,1,1,0,0,1,1
x2 = 0,0,0,1,1,0,0,0,0,0,0,0,0
x = np.array([x0,x1,x2])
y =  2,2,2,2,2,2,2,2,2,2,2,2,2
y = np.array(y)
theta = -30,10,10
theta = np.array(theta)
lambda_ = 0.1
#print(theta.shape)
#print(x.shape)
#print(y.shape)
#J,grad = cost_function(theta,x,y,lambda_)
#print(round(J),round(grad))
###

x = pd.read_csv(r"C:\Users\Lars__000\Documents\Online_courses\Machine_learning\Coursera\machine-learning-ex3\x.csv",delimiter = ';')
y = pd.read_csv(r"C:\Users\Lars__000\Documents\Online_courses\Machine_learning\Coursera\machine-learning-ex3\y.csv",delimiter = ';')
x = np.transpose(x.to_numpy())
y = y.to_numpy()
y = np.squeeze(y)
x = x[0:5,:]
theta = -2,1,-2,1,-2
theta = np.array(theta)
#print(theta.shape)
#print(x.shape)
#print(y.shape)
#J,grad = cost_function(theta,x,y,lambda_)
#print(J,grad)
#print(J)
#print(grad)



