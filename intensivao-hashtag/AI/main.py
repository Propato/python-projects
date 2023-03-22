# Translation of the codes referring to the types of boat, type of sail and materials are in the tables.png

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

table = pd.read_csv("./barcos_ref.csv")
#print(table.info())

# See correlations between prices and the other columns
correlations = table.corr()[['Preco']]

# sns.heatmap(correlations, cmap="Greens", annot=True)
# plt.show()

# we divide the table between the inputs (all columns) and the output we want (output of Prices, as we want to predict prices)
y = table["Preco"]
x = table.drop("Preco", axis=1)

# we split the tables in two, one for training data and one for test data
x_training, x_test, y_training, y_test = train_test_split(x, y)

# AIs
prev = 0
while(prev < 0.8):
    model_linearRegression = LinearRegression()
    model_forestRegressor = RandomForestRegressor()

    model_linearRegression.fit(x_training, y_training)
    model_forestRegressor.fit(x_training, y_training)

    prevision_linearRegression = model_linearRegression.predict(x_test)
    prevision_forestRegressor = model_forestRegressor.predict(x_test)

    prev = r2_score(y_test, prevision_forestRegressor)

print(r2_score(y_test, prevision_linearRegression))
print(r2_score(y_test, prevision_forestRegressor))

new_table = pd.DataFrame()
new_table["y_test"] = y_test
new_table["forestRegressor"] = prevision_forestRegressor
new_table["linearRegression"] = prevision_linearRegression

# view accuracy of test predictions
# sns.lineplot(data=new_table)
# plt.show()

new_boats_table = pd.read_csv("./novos_barcos.csv")

prev = model_forestRegressor.predict(new_boats_table)
print(prev)