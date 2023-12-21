# Importing the required libraries
import pandas as pd 
import numpy as np


import math



data = pd.read_excel('SHG_Booking_Data.xlsx') # importing Data for Splendor Hotel Groups (SHG)
# print(data)
# print(data.isnull().sum())
clean_data = data.dropna() # remove empty values
# print(clean_data)
# Checking the trend in the monthly booking pattern
# Converting 'Booking Date' to month


# Convert date columns to datetime format
data['Booking Date'] = pd.to_datetime(data['Booking Date'])
data['Arrival Date'] = pd.to_datetime(data['Arrival Date'])

import matplotlib.pyplot as plt
import seaborn as sns
# Set the 'Booking Date' as the index for time series analysis
data.set_index('Booking Date', inplace=True)

# Create a time series plot for overall booking trends
plt.figure(figsize=(12, 6))
data.resample('M').size().plot()
plt.title('Monthly Booking Trends')
plt.xlabel('Date')
plt.ylabel('Number of Bookings')
plt.show()


