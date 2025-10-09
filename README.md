🌤️ Weather Data Analysis

📘 Overview

This project analyzes a weather dataset using Python and Pandas.
It explores, cleans, and extracts insights from the data based on various weather conditions.

⚙️ Features

1. Loaded and explored the dataset (shape, columns, data types, and null values)
2. Renamed columns and handled missing data
3. Calculated mean, standard deviation, and variance of parameters
4. Filtered data based on weather conditions, wind speed, and visibility
5. Grouped data to find min, max, and mean for each weather condition
6. Extracted insights using logical and conditional queries

📊 Key Pandas Functions Used

Function          	Description
head()            	Shows first 5 rows
shape	          	  Displays total rows and columns
index	          	  Provides index details of DataFrame
columns	          	Lists column names
dtypes	          	Shows data types of each column
unique()	          Shows unique values in a column
nunique()	          Counts unique values in DataFrame
count()	          	Counts non-null values in each column
value_counts()	    Shows unique values with counts
info()	          	Provides basic information about DataFrame
min() / max()	      Finds minimum and maximum values


🧠 Example Insights

1. Number of times weather was Clear
2. Instances of Snow or Fog
3. Mean visibility and pressure deviation
4. Conditions where wind speed > 24 and visibility = 25
5. Data grouped by Weather Condition for statistical summary
