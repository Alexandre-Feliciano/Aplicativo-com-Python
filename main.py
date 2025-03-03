from kivy.app import App 
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):   
        
        self.root.ids["moeda_1"].text = f"Dólar: R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda_2"].text = f"Euro: R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda_3"].text = f"Bitcoin: R${self.pegar_cotacao('ETH')}"
        self.root.ids["moeda_4"].text = f"Ethereum: R${self.pegar_cotacao('USD')}"
    
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao       
        
# sempre quando o "self" é colocado, ele está fazendo referência ao seu aplicativo.

MeuAplicativo().run()

# Estrutura do arquivo .kv

# Item que você quer adicionar: 
#   configurações do Item: valor do item

# para a criação do app com kivy a estrutura tem que respeitar as indentações, pois pode dar erro.
# dentro de um arquivo .kv o app fica dentro de um:
# 
# "GridLayout: 
#      cols: n° colunas" 
# 
# para definir como vai funcionar a estrutura do mesmo.

# criando funcionalidades

# Para alterar os atributos no arquivo.kv de forma dinâmica podemos atribuir ID's a eles (ID's são únicos!)
# 
# ex:
# Label:
#   id: texto_1
#   text: "meu primeiro texto"
# 