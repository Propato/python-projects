# importar as bibliotecas
from string import Formatter
import pandas as pd
import smtplib
import email.message

# INSIRA DADOS DOS E-MAILS
email_from = ''
email_to = ''
password_from = ''

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
#pd.set_option('display.max_columns', None)
#print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
#print(faturamento)
#print('\n'+'*'*44+'\n')

# quantidade de produtos vendidos por loja
produtos = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#print(produtos)
#print('\n'+'*'*44+'\n')

# ticket medio por loja (faturamento/quantidade)
ticket = (faturamento['Valor Final'] / produtos['Quantidade']).to_frame()
ticket = ticket.rename(columns={0: 'Ticket Médio'})
#print(ticket)
#print('\n')

# enviar um email com relatório
corpo_email = f'''
<p>Seguem relatórios sobre todos os Shoppings:</p>
<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R$ {:,.2f}'.format})}
<p>Quantidades de produtos vendidos</p>
{produtos.to_html()}
<p>Média de valor por quantidade de produtos</p>
{ticket.to_html(formatters={'Ticket Médio': 'R$ {:,.2f}'.format})}
'''

msg = email.message.Message()
msg['Subject'] = "Teste 2.1 Mini Curso Python"
msg['From'] = email_from
msg['To'] = email_to
password = password_from
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
#login
s.login(msg['From'], password)
s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
print('Relatórios enviados!!\n')