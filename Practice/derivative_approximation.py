import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def gradient_checking():
       ## J = teta*x**2
       n = 100
       theta = [0,1,1,2,3]
       EPSILON = 0.1
       grad_approx = []
       x_values = [15,9,2,6,1]
       
       for i,x in zip(theta,x_values):
              thetaminus,thetaplus = theta,theta
              thetaminus[i] = thetaminus[i]-EPSILON
              thetaplus = theta
              thetaplus[i] = thetaplus[i]+EPSILON
              
              
              #print(thetaminus[i])
              #gradApprox = ((thetaplus*x**2 + i) - ((thetaminus*x**2)+i))/(2*EPSILON)
              #grad_approx.append(gradApprox)
       print(grad_approx)
       gradient_checking()

x = 1
J = 2*x**4+2

der = ((2*(1+0.01)**4+2)-(2*(1-0.01)**4+2))/(2*0.01)

print(der)
