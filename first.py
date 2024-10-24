import pandas as pd

remon_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
remon_data = pd.read_csv(remon_path)

boston_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
boston_data = pd.read_csv(boston_path)
 
iris_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
iris_data = pd.read_csv(iris_path)

print(remon_data)
print(boston_data)
print(iris_data)