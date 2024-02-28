import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')
print('Data')
print(df)

#1 The functions isnull() and notnull() are used to identify missing data.
print("Finding missing data with notnull())")
print(df.head(10).notnull()) # False is the value is missing
print("Finding missing data with isnull())")
print(df.head(10).isnull()) # True is the value is missing


# Imputation is a conventional technique used to keep valuable data that have missing values.
average = df["Age"].head(10).mean() # Calculate the average value of Age.
print("Average age of the first 10 passengers using mean() method:")
print(average)

med = df["PassengerId"].median() # Calculate the mid of the first 10 values of PassengerId.
print("Median of passengers using median() method:")
print(med)

modde = df["Survived"].mode() # Calculate the most reapeted value of Survived.
print("Mode of passengers Survived using mode() method:")
print(modde)



#2 One-hot encode the data using pandas get_dummies:
one_hoted = pd.get_dummies(df['Survived'])
data_encoded = pd.concat([df, one_hoted], axis=1)
print("One-hot encoded data[Survived]:")
print(data_encoded)
# We can use one-hot encoding to convert the categorical data into a binary vector.
# We use it when we want to include categorical data in our model.



#3 To discover duplicates, we can use the duplicated() method.
print("Duplicated data returning boolean:")
print(df.duplicated()) # Return a boolean series

# to remove duplicates, we can use the drop_duplicates() method.
print("Data without duplicates:")
drop_dup = df.drop_duplicates()
print(drop_dup) # Return a new DataFrame without duplicates.

# duplicated() identifies duplicates, and drop_duplicates() removes duplicates.



#4 Data normalization is the process of bringing different scales and units of measurement to a single view.
# We can use the Min-Max scaling method to normalize the dataset.
# The formula is:
# X = (X - Xmin) / (Xmax - Xmin)
# Where X is the original value, Xmin is the minimum value, and Xmax is the maximum value.

# Z-score normalization is the process of normalizing the dataset using the mean and standard deviation of the data.
# The formula is:
# Z = (X - μ) / σ
# Where Z is the z-score, X is the original value, μ is the mean, and σ is the standard deviation.

# The difference between Min-Max scaling and Z-score normalization is that Min-Max scaling is sensitive to outliers,
# while Z-score normalization is not.


#5  Outliers are data points that are far from other data points.
# Outliers can confuse the machine learning model, and we should remove them from the dataset.

# We can use the Z-score method to identify outliers.
# Also we can use the IQR method to identify outliers.
# The IQR method is based on the IQR score, which is the difference between the 75th and 25th percentiles.
# The formula is:
# IQR = Q3 - Q1
# Where Q1 is the 25th percentile, and Q3 is the 75th percentile.
# And we can use the boxplot to identify outliers.
# The boxplot is a standardized way of displaying the distribution of data based on a five-number summary:
# the minimum, first quartile (Q1), median, third quartile (Q3), and maximum.

# To handle with outliers we can use the following methods:
# - Removing the outliers
# - Transforming the data
# - Imputing the data
# - Using binning
# - Using the Z-score method
# - Using the IQR method
# - Using the boxplot method



