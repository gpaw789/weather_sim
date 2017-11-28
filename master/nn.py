
# http://scikit-learn.org/stable/modules/neural_networks_supervised.html

from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# open csv
df = pd.read_csv("master3.csv")

# split into features and outputs
df_x = df[["lat", "long", "ele"]]
df_y = df.loc[:, "value"]       # this is the temperature

# produce training data
#x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=1)
x_train = df_x
y_train = df_y

# set up neural network parameters
nn = MLPRegressor(
    hidden_layer_sizes=(1000,),  activation='relu', solver='adam', alpha=0.001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=200, shuffle=True,
    random_state=None, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

# train neural network
n = nn.fit(x_train, y_train)

# save the neural network fit
pickle.dump(n,open("n_fit.p", "wb"))

# example
'''
my_object = {"lat": -33.8607, "long": 151.205, "ela": 39}

df_new = pd.DataFrame(my_object,index=[0])

yy = nn.predict(df_new)
print(yy)
'''