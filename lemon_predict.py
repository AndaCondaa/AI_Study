import pandas as pd
import tensorflow as tf

path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
data = pd.read_csv(path)
print(data.head())

# data seperation
x = data[['온도']]
y = data[['판매량']]
print(x.shape, y.shape)

# make model
X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

# train using GPU
with tf.device('/GPU:0'):
    model.fit(x, y, epochs=10000)
    model.fit(x, y, epochs=10)
    pass

# using model
print(model.predict(x))

print(y)