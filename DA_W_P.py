import pandas as pd

df=pd.read_csv("Your_Path")

"""              Q. DATA FRAMES              """
#print(df.head()) 
#print(df.shape) 
#print(df.index) 
#print(df.columns) 
#print(df.dtypes) 
#print(df['Weather'].unique()) 
#print(df.nunique())
#print(df.count()) 
#print(df['Weather'].value_counts()) 
#print(df.info()) 


""" Q1. Find all the unique "Wind Speed" values in the data. """

#print(df['Wind Speed_km/h'].nunique()) 
#print(df['Wind Speed_km/h'].unique())


""" Q2. Find the number of times when the 'Weather is exactly Clear'. """

#print(df[df.Weather=="Clear"])                             OR
#print(df.groupby("Weather").get_group("Clear")) 


""" Q3. Find the number of times when the 'Wind Speed was exactly 4 km/h' . """

#print(df[df['Wind Speed_km/h']==4])


""" Q4. Find out all nun values in the data' . """

#print(df.isnull().sum())                                 OR
#print(df.notnull().sum()) 


""" Q5. Rename the column name "Weeather" of the dataframe to "Weather Condition" . """

dt=df.rename(columns={'Weather':'Weather Condition'})
#print(dt)


""" Q6. What is the mean "Visibility". """

#print(dt['Visibility'].mean())      or    
# print(dt.Visibility_km.mean())


""" Q7. What is the Standard Deviation of "Pressure" in this data. """

#print(dt['Press_kPa'].std())


""" Q8. What is the Variance of 'Relative Humidity' in this data. """

#print(dt['Rel Hum_%'].var())


""" Q9. Find all instances when 'Snow' was recovered. """

#   print(dt[dt['Weather Condition']=='Snow'])     OR
#   print(dt['Weather Condition'].value_counts())      OR
#   print(dt[dt['Weather Condition'].str.contains("Snow")])


""" Q10. Find all instances when 'Wind Speed is abovve 24' and 'Visibility is 25. """

#print(dt[(dt['Wind Speed_km/h']>24) & (dt['Visibility_km']==25)])


""" Q11. What is the Mean value of each column against each "Weather Condition. """

#print(dt.groupby('Weather Condition').mean(numeric_only=True)) 



""" Q12. What is the Min and Max value of each column against each "Weather Condition. """

#print(dt.groupby('Weather Condition').min()) 
#print(dt.groupby('Weather Condition').max()) 


""" Q13. Show all the Records where Weather Condition is Fog. """

#print(dt[dt['Weather Condition']=="Fog"])


""" Q14. Find all instances when 'Weather is Clear' or 'Visibility is above 40'. """

#print(dt[(dt['Weather Condition']=="Clear") | (dt['Visibility_km'] > 40)])


""" Q15. Find all instances when :
A. 'Weather is Clear' and 'Relative Humidity is greater than 50 or
B.'Visibility is above 40 """


print(dt[(dt['Weather Condition']=='Clear') & (dt['Rel Hum_%']>50) | (dt['Visibility_km']>40)])
