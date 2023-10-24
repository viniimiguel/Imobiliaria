from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class Imovel():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.site_link = 'https://www.vivareal.com.br/venda/'
        self.site_map = {
            'XP': {
                'pesquisa': '/html/body/main/div[2]/div[1]/nav/div/div/form/fieldset[1]/div[1]/div/div/input',
            }
        }
    def main(self):
        self.entra()
        sleep(5)
        self.raspagem()
        sleep(12831830)


    def entra(self):
        self.driver.get(self.site_link)
        self.driver.maximize_window()
        pesq = input('digite oque voce quer procurar: ')
        rua = self.driver.find_element(By.XPATH, self.site_map['XP']['pesquisa'])
        rua.send_keys(pesq)
        sleep(3)
        rua.send_keys(Keys.ENTER)

    def raspagem(self):
        contador = 1
        while True:
            definicoes = {
                'XP': {
                    'rua': f'/html/body/main/div[2]/div[1]/section/div[2]/div[1]/div[{contador}]/div/article/a/div/h2/span[2]/span[1]',
                    'descricao': f'/html/body/main/div[2]/div[1]/section/div[2]/div[1]/div[{contador}]/div/article/a/div/h2/span[1]',
                    'metragem': f'/html/body/main/div[2]/div[1]/section/div[2]/div[1]/div[{contador}]/div/article/a/div/ul[1]',
                    'valorizacao': f'/html/body/main/div[2]/div[1]/section/div[2]/div[1]/div[{contador}]/div/article/a/div/ul[2]',
                    'valor': f'/html/body/main/div[2]/div[1]/section/div[2]/div[1]/div[{contador}]/div/article/a/div/section/div'
                }
            }
            try:
                localizacao = self.driver.find_element(By.XPATH, definicoes['XP']['rua'])
                descricao = self.driver.find_element(By.XPATH, definicoes['XP']['descricao'])
                metragem = self.driver.find_element(By.XPATH, definicoes['XP']['metragem'])
                valorizacao = self.driver.find_element(By.XPATH, definicoes['XP']['valorizacao'])
                valor = self.driver.find_element(By.XPATH, definicoes['XP']['valor'])

                print(localizacao.text)
                print(descricao.text)
                print(metragem.text)
                print(valorizacao.text)
                print(valor.text)
                print('###'*25)
                contador += 1
                if contador == 10:
                    break
            except NoSuchElementException:
                print('elemento nao encontrado')


        




imovel = Imovel()
imovel.main()