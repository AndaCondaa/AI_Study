import pandas as pd

lemon_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
lemon_data = pd.read_csv(lemon_path)

boston_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
boston_data = pd.read_csv(boston_path)
 
iris_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
iris_data = pd.read_csv(iris_path)

# print data set shape
print(lemon_data.shape)
print(boston_data.shape)
print(iris_data.shape)

# print columns
print(lemon_data.columns)
print(boston_data.columns)
print(iris_data.columns)

# data seperation
lemon_inde = lemon_data[['온도']]
lemon_de = lemon_data[['판매량']]
print(lemon_inde.shape, lemon_de.shape)

boston_inde = boston_data[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']]
boston_de = boston_data[['medv']]
print(boston_inde.shape, boston_de.shape)

iris_inde = iris_data[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
iris_de = iris_data[['품종']]
print(iris_inde.shape, iris_de.shape)

print(lemon_data.head())
print(boston_data.head())
print(iris_data.head())
