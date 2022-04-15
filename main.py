import requests
import csv
from bs4 import BeautifulSoup

page = requests.get('https://quintaldermocosmeticos.com.br/collections/mascaras')

soup = BeautifulSoup(page.text, 'html.parser')

arquivo = csv.writer(open('mascaras-quintal.csv', 'w', newline=''))
arquivo.writerow(['Nome', 'Preço', 'Link'])

nome_produto_list = soup.find(class_='productList')
nome_produto_list_itens = nome_produto_list.find_all('div', class_='grid-view-item')

for produto in nome_produto_list_itens:
    titulo = produto.find('a', class_='grid-view-item__title')
    valor = produto.find('span', class_='product-price__price')
    preco = valor.contents[0]
    nome = titulo.contents[0]
    links = 'https://quintaldermocosmeticos.com.br/' + titulo.get('href')

    arquivo.writerow([nome, preco, links])