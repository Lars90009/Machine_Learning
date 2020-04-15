from linear_regression import Regression

# Variables to change
iterations = 100
randomx1 = 1
randomx2 = 10
randomy1 = 4
randomy2 = 7
teta_a = 1
teta_b = 1
wanted_x = [10,20,30,40] # Insert the wanted x-value for your dataset


#Create randomized observed x and y values
#If you don't want it to be randomized then you have to deliver your own
# input in array form for both x and y 
observed_x,observed_y = Regression().random_array(iterations,randomx1,randomx2,randomy1,randomy2)

#Obtain the optimization with the minimum mae_error
#It returns mae_error, teta_a (a) and teta_b (b)
mae_error,a,b = Regression().\
                linear_regression(observed_x,observed_y,teta_a,teta_b)
print(mae_error)
print('Y=teta_a*x+teta_b: MAE error = ',round(mae_error,2),\
      'Teta_a =',round(a,2),'Teta_b = ',round(b,2))
for x in wanted_x:
       y_value = round(Regression().linear_result(a,b,x),2)
       print('Predicted Value = ',y_value)
plot = Regression().linear_plot(observed_x,observed_y,a,b,randomx1,randomx2,randomy1,randomy2,round(mae_error,2))
