import numpy as np
class support_vector_machine(object):
       def __init__(self):
              pass
       def sigmoid(z):
              g = 1.0 / (1.0 + np.exp(-z))
              return g
       def cost1(h_x):
              cost1 = -np.log(h_x)
              return cost1
       def cost0(h_x):
              cost0 = -np.log(1-h_x)
              return cost0
       def regularization(theta):
              regularization = (1/2)*sum(np.power(theta,2))
              return regularization
       def logistic_regression(cost0,cost1,observed_y):
              log_reg = (1.0)*sum(observed_y * cost1 +\
                                         (1-observed_y)*cost0)
              return log_reg
       def support_vector_machine(lambda_,logistic_regression,regularization):
              A = logistic_regression
              B = regularization
              C = 1/lambda_
              log_reg = C*A+B
              return log_reg

lambda_ = 10
observed_y = 1,2,3,4,5
observed_y = np.array(observed_y)
m = len(observed_y)
x0 = 1,1,1,1,1
x1 = 0,1,3,2,4
x2 = 1,2,3,4,5
x = np.array([x0,x1,x2])
theta = np.array([-1,-1,-1])
print(theta)
maxiterations = 100
learning_rate = 0.1
for i in range(0,maxiterations):
       z = theta.dot(x)
       h_x = support_vector_machine.sigmoid(z)
       cost1 = support_vector_machine.cost1(h_x)
       cost0 = support_vector_machine.cost0(h_x)
       log_reg = support_vector_machine.logistic_regression(cost0,cost1,observed_y)
       regularization = support_vector_machine.regularization(theta)
       log_reg = support_vector_machine.support_vector_machine(lambda_,log_reg,regularization)    
       derivative_error_theta = sum((h_x-observed_y)*x)
       theta = np.subtract(theta,-0.1)
       print(theta)
       print(log_reg)
