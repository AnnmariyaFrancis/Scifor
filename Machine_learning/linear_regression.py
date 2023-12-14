# -*- coding: utf-8 -*-
"""Linear_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_xEo8EvQnIuixifxCH_tUvix8-qFRBvD
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df=pd.read_csv("/content/advertising.csv")
df.head()

x=df['Radio'].values
y=df['Sales'].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=30)

x_train=np.vstack((np.ones_like(x_train),x_train)).T
x_test=np.vstack((np.ones_like(x_test),x_test)).T

def linear_regression(x,y,learning_rate,epochs):
     m,n=x.shape
     weights=np.zeros(n)
     cost_list=[]

     for i in range(epochs):
      predictions=np.dot(x,weights)
      error=predictions-y
      gradient=np.dot(x.T,error)/m
      weights-=learning_rate*gradient

      cost=(1/(2*m))*np.sum(error*2)
      cost_list.append(cost)
     return weights,cost_list

learning_rate=0.00001
epochs=1000
weights,cost_list=linear_regression(x_train,y_train,learning_rate,epochs)
y_pred_test=np.dot(x_test,weights)
mse=np.mean((y_test-y_pred_test)**2)
rmse=np.sqrt(mse)
mae=np.mean(np.abs(y_test-y_pred_test))
total_variance=np.sum((y_test-np.mean(y_test))**2)
r_squared=1-(mse/total_variance)

print("mean squared error:",mse)
print("mean absolute error:",mae)
print("root mean squared error",rmse)
print("r-squared:",r_squared)

res_df=pd.DataFrame({"actual_values":y_test,"predicted_values":y_pred_test,"difference":y_test-y_pred_test})
print(res_df)

plt.figure(figsize=(10,6))
plt.plot(res_df['actual_values'][:5],res_df['predicted_values'][:5],color='red')
plt.xlabel("Actual values")
plt.ylabel("predicted values")
plt.title("Actual vs predicted")
plt.show()