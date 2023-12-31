# -*- coding: utf-8 -*-
"""AI_Mental_Fitness_Tracker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qEn3MLfWm_zWadn1TUiiLj4UIuF70TOG
"""

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

#prevalence-by-mental-and-substance-use-disorder.csv
df1=pd.read_csv("/content/prevalence-by-mental-and-substance-use-disorder (1).csv")

#mental-and-substance-use-as-share-of-diease.csv
df2=pd.read_csv("/content/mental-and-substance-use-as-share-of-disease.csv")

#prevalence-by-mental-and-substance-use-disorder.csv
df1.head()

#mental-and-substance-use-as-share-of-diease.csv
df2.head(10)

data=pd.merge(df1,df2)
data.head(10)

#Missing values in the dataset

data.isnull().sum()

#Drop the column
data.drop('Code',axis=1,inplace=True)

#view the data

data.head(10)

data.size,data.shape

data.set_axis(['Country','Year','Schizophrenia','Bipolar_disorder','Eating_disorder','Anxiety','drug_usage','depression','alcohol','mental_fitness'],axis='columns',inplace=True)

data.head(10)

plt.figure(figsize=(12,6))
sns.heatmap(data.corr(),annot=True,cmap='Blues')
plt.plot()

sns.pairplot(data,corner=True)
plt.show()

mean=data['mental_fitness'].mean()
mean

fig=px.pie(data,values='mental_fitness',names='Year')
fig.show()

#Year wise variations in mental_fitness of different countries

fig=px.line(data,x="Year",y="mental_fitness",color='Country',markers=True,color_discrete_sequence=['red','blue'],template='plotly_dark')
fig.show()

df=data
df.info()

from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
for i in df.columns:
  if df[i].dtype=='object':
    df[i]=l.fit_transform(df[i])

df.shape

x=df.drop('mental_fitness',axis=1)
y=df['mental_fitness']

from sklearn.model_selection import train_test_split
xtrain, xtest,ytrain,ytest=train_test_split(x,y,test_size=.20,random_state=2)

print("xtrain: ",xtrain.shape)
print("xtest: ",xtest.shape)
print("\n ytrain: ",ytrain.shape)
print("ytest: ",ytest.shape)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
lr=LinearRegression()
lr.fit(xtrain,ytrain)  #fit training data

#model evaluation for training set
ytrain_pred=lr.predict(xtrain)
#The mean square Error measures the average difference between values predicted by model the actual
mse=mean_squared_error(ytrain,ytrain_pred)
#Root Mean Square Error measures the average differnce between the observed and predicted values of a variable
rmse=(np.sqrt(mean_squared_error(ytrain,ytrain_pred)))
#The coefficientof determination, or R2, is a measure that provides information about the goodness of a model ,in the context of regression it is a statical measure of
r2=r2_score(ytrain,ytrain_pred)


print("The Linear Regression model performance for training set")
print("-------------------------------------")
print("MSE is {}".format(mse))
print("RMSE is{}".format(rmse))
print('R2 score is[]'.format(r2))

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor()
rf.fit(xtrain,ytrain)
#model evaluation for training set
ytrain_pred=rf.predict(xtrain)
mse=mean_squared_error(ytrain,ytrain_pred)
rmse=(np.sqrt(mean_squared_error(ytrain,ytrain_pred)))
r2=r2_score(ytrain,ytrain_pred)


print("The Random Forest Regressor model performance for training set")
print("--------------------------------------")
print("MSE is{}".format(mse))
print("RMSE is{}".format(rmse))
print("R2 score is{}".format(r2))

#Linear Forest Regression model evaluation for testing set
ytest_pred=lr.predict(xtest)
mse=mean_squared_error(ytest,ytest_pred)
rmse=(np.sqrt(mean_squared_error(ytest,ytest_pred)))
r2=r2_score(ytest,ytest_pred)

print("The Linear Forest Regression model evaluation for testing set")
print("-------------------------------")
print("MSE is{}".format(mse))
print("RMSE is{}".format(rmse))
print("R2 score is{}".format(r2))





#Random Forest Regression model evaluation for testing set
ytest_pred=rf.predict(xtest)
mse=mean_squared_error(ytest,ytest_pred)
rmse=(np.sqrt(mean_squared_error(ytest,ytest_pred)))
r2=r2_score(ytest,ytest_pred)

print("\n The Random Forest Regression model evaluation for testing set")
print("------------------------------------")
print("MSE is{}".format(mse))
print("RMSE is{}".format(rmse))
print("R2 score is{}".format(r2))