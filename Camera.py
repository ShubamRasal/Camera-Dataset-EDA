# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 12:09:34 2022

@author: Shubham
"""

import pandas as pd

import numpy as np

import os

os.chdir(r"D:\Data Analyst\Python Project")
os.listdir()

# Create a dataframe “Camera_data” using Camera.csv

camera_data = pd.read_csv("Camera.csv")
camera_data

camera_data.head()

camera_data.shape

camera_data.index

camera_data.columns

camera_data.dtypes

# Find out the percentage of blank values in each column.

percent_blank = camera_data.isnull().sum() * 100 / len(camera_data)
percent_blank

#  View the statistical summary of the data

camera_data.describe()

# Replace all the blank values with NaN.

camera_data[camera_data==" "]=np.NaN
camera_data.isnull().sum()

#  Now replace all the Blank values with the column median.

camera_data.isnull().sum()

camera_data.mean()

camera_data.fillna(camera_data.mean(), inplace=True)

#  Add a new column “Discounted_Price” in which give a discount of 
#  5% in the Price column.

camera_data['Discounted_Price'] = camera_data.apply(lambda row: row.Price - 
                                                    (row.Price * 0.05), axis = 1)
 
camera_data                                 

#  Drop the columns Zoom Tele & Macro Focus range

camera_data.drop(['Zoom tele (T)'], axis=1, inplace=True)

camera_data.drop(['Macro focus range'], axis=1, inplace=True)

#  Replace the Model Name “Agfa ePhoto CL50” with “Agfa ePhoto CL250”

camera_data['Model']= camera_data['Model'].replace(['Agfa ePhoto CL50'],'Agfa ePhoto CL250')

camera_data.head(7)

#  Rename the column name from Release Date to Release Year.

camera_data.rename(columns = {"Release date" : "Release Year"}, inplace=True) 

camera_data

#  Which is the most expensive Camera?

camera_data['Price'].max()

camera_data[camera_data['Price'] == 7999]

#  Which camera have the least weight?

camera_data['Weight (inc. batteries)'].min()

camera_data[camera_data['Weight (inc. batteries)'] == 100]

# Group the data on the basis of their release year.

camera_data.groupby('Relese Year').mean()
camera_data.groupby('Relese Year').count()
camera_data.groupby('Relese Year').std()
camera_data.groupby('Relese Year').max()
camera_data.groupby('Relese Year').min()

# Extract the Name, Storage Include, Price, Disounted_Price & Dimensions columns.

camera_data.columns

camera_data[['Model','Storage included','Discounted_Price','Dimensions']]

# Extract the records for the cameras released in the year 2005 & 2006

camera_data[(camera_data['Relese Year'] == 2005)] 

camera_data[(camera_data['Relese Year'] == 2006)]

# Find out 2007’s expensive & Cheapest Camera.

camera_data[(camera_data['Relese Year'] == 2007)].min()

camera_data[(camera_data['Relese Year'] == 2007)].max()

# Which Year maximum number of models is released?

camera_data['Relese Year'].value_counts()

