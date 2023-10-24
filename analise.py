import pandas as pd
from IPython.display import display


class Analise:
    def __init__(self):
        self.tabela = pd.read_excel('planilha_de_imoveis.xlsx')
    
    def mostrar_tabela(self):
        print(self.tabela)
    

    def casas_por_rua(self, rua):
        logradouros = self.tabela[self.tabela['RUA'] == rua]['LOGRADOURO'].unique()
        for logradouro in logradouros:
            casas_filtradas = self.tabela[(self.tabela['LOGRADOURO'] == logradouro) & (self.tabela['RUA'] == rua)]
            print(f'Logradouro: {logradouro}, Rua: {rua}')
            print(casas_filtradas)


while True:
    rua = input('Qual o nome da rua?:  ')
    print('###'*50)
    analise = Analise()
    analise.casas_por_rua(rua)
    print('###'*50)
    