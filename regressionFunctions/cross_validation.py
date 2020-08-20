import random
import numpy as np

class cross_validation(object):
       def cv_set(dataset,cv_percentage):
              dataset = dataset
              cv_percentage = cv_percentage
              print('Choosing 20% of the dataset items from observed_x and y')
              len_dataset = int(len(dataset)*cv_percentage)
              cv_set = random.sample(list(dataset),len_dataset)
              return np.array(cv_set)

### Example
dataset = np.arange(0,100,0.5)
cv_percentage = 0.2
cv = cross_validation.cv_set(dataset,cv_percentage)
print(cv)
              
