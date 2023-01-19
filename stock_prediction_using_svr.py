# -*- coding: utf-8 -*-
"""Stock_prediction_using_SVR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nk2m5RfNL0aGUPp1bJCv4QPHoOgyiESV

Import Libraries
"""

import  pandas as pd
import numpy as np

"""Load dataset from Local directory"""

from google.colab import files
uploaded = files.upload()

"""Load dataset"""

dataset = pd.read_csv("data.csv")

"""Summarize dataset"""

print(dataset.shape)
print(dataset.head(5))

"""Segregate x and y:"""

x = dataset.iloc[:, :-1].values
print(x)
y = dataset.iloc[:, -1].values
print(y)

"""Splitting dataest for testing model"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state=0 )

"""Training dataset using Support Vector Regression"""

from sklearn.svm import SVR
model= SVR(kernel = "linear", tol = 0.2 , C = 2)
model.fit(x_train,y_train)

"""Prediction for all test data for validation"""

y_pred = model.predict(x_test)

from sklearn.metrics import r2_score,mean_squared_error
# root mean square error
mse = mean_squared_error(y_test, y_pred)
rmse  = np.sqrt(mse)
print("Root Mean Square Error :" , rmse)
#r2score
r2score = r2_score(y_test, y_pred)
print("R2Score : ",r2score*100)

