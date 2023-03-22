from selenium import webdriver
import pandas as pd

# To remove accents
# import unicodedata
# out = unicodedata.normalize("NFKD", input).encode("ascii", errors='ignore').decode()

table = pd.read_excel("./currency.xlsx")

navegator = webdriver.Chrome()

for index in table.index:
    currency = table.loc[index, 'Moeda'].replace(" ", "+")
    
    navegator.get(f"https://www.google.com.br/search?q=preco+{currency}")
    value = navegator.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[2]/input').get_attribute('value')
    table.loc[index, 'Preço Atual'] = float(value)

table["Comprar"] = table["Preço Atual"] <= table["Preço Ideal"]
table.to_excel("./currency_update.xlsx", index=False)

# .click() -> click
# .send_keys("text") -> write
# .get_attribute('attribute') -> get an atributte