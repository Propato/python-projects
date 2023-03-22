import pandas as pd
import plotly.express as px
# Open data base
table = pd.read_csv("clientes.csv", sep=';', encoding='latin')

# Delete null column
table.drop("Unnamed: 8", axis=1, inplace=True)

# The column type was Object, but the correct one is Number
table["Salário Anual (R$)"] = pd.to_numeric(table["Salário Anual (R$)"], errors="coerce")

# print(table[table["Profissão"].isna()])

# Delete rows with null values
table.dropna(inplace=True)

# Create and show the graph for all column
for column in table.columns:
    graph = px.histogram(table, x=column, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=8)
    graph.show()

print(table)
print(table.info())
print(table.describe())