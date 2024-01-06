import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# There are some fake data csv files 
# you can read in as dataframes 
df1 = pd.read_csv('nba.csv', usecols=["Age"], nrows=10) 
# df2 = pd.read_csv('df2') 
plt.style.use('ggplot')

# Plot the histogram
plt.hist(df1['Age'],  edgecolor='black')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

# Show the plot
plt.show()
