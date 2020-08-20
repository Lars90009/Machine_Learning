from linear_regression import Regression
import numpy as np

# Variables to change and build a randomized data set
iterations = 10
randomx1 = 1
randomx2 = 10
randomy1 = 5
randomy2 = 12
teta_a = 0
teta_b = 0
wanted_x = [10,20,30,40]    # Insert the wanted x-value for your dataset
learning_rate = 0.01        #Use steps with increasing approximately 0.02, or 0.2 etc.
maxIterations = 20        #Learning length
global_optimum = True

#Create randomized observed x and y values
#If you don't want it to be randomized then you have to deliver your own
# input in array form for both x and y
GD = True
if GD == True:
       observed_x,observed_y = Regression().random_array(iterations,randomx1,randomx2,randomy1,randomy2)

       #Obtain the optimization with the minimum mae_error
       #It returns mae_error, teta_a (a) and teta_b (b)
       mae_error,a,b = Regression().\
                       linear_regression_vector(observed_x,observed_y,\
                                         teta_a,teta_b,learning_rate,maxIterations,global_optimum)
       print('Y=teta_a*x+teta_b: MAE error = ',round(mae_error,2),\
             'Teta_a =',round(a,2),'Teta_b = ',round(b,2))
       for x in wanted_x:
              y_value = round(Regression().linear_result(a,b,x),2)
              print('Predicted Value = ',y_value)
       plot = Regression().linear_plot(observed_x,observed_y,a,b,randomx1,randomx2,randomy1,randomy2,round(mae_error,2))

NE = False
if NE == True:
       print('       ')
       #Linear Regression with Normal Equation
       observed_x,observed_y = Regression().random_array(iterations,randomx1,randomx2,randomy1,randomy2)
       observed_x2,observed_y2 = Regression().random_array(iterations,randomx1+1,randomx2+1,randomy1+1,randomy2+1)
       observed_x3,observed_y3 = Regression().random_array(iterations,randomx1-1,randomx2-1,randomy1-1,randomy2-1)
       observed_x = [1,1,1,1,1,1,1,1,1,1]
       t1,t2,t3 = Regression().linear_regression_NE(observed_x,observed_y,observed_x2,observed_x3)
       plot = Regression().polynomial_plot(observed_x,observed_y,observed_x2,observed_y2,\
                                           observed_x3,observed_y3,t1,t2,t3)
       #print(t1,t2,t3)
