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
        self.site_link = 'https://www.zapimoveis.com.br/venda/imoveis/pe+recife/?__ab=exp-aa-test:B,new-discover-zap:alert,vas-officialstore-social:enabled,deduplication:control&transacao=venda&onde=,Pernambuco,Recife,,,,,city,BR>Pernambuco>NULL>Recife,-8.05774,-34.882963,&pagina=1'
        
    def main(self):
        self.entra()
        sleep(5)
        self.raspagem()
        sleep(12831830)


    def entra(self):
        self.driver.get(self.site_link)
        self.driver.maximize_window()

    def raspagem(self):
        contador = 1
        
        while True:
            try:
                xpats = {
                    'XP': {
                        'logradouro': f'/html/body/div[1]/main/section/div/form/div[2]/div[2]/div[1]/div[2]/div[{contador}]/div/a/div/div/div[2]/div[1]/section/div/h2',
                        'rua': f'/html/body/div[1]/main/section/div/form/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/div/div/div[2]/div[1]/section/p',
                        'descricao': f'/html/body/div[1]/main/section/div/form/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/div/div/div[2]/div[2]/p',
                        'metragem': f'/html/body/div[1]/main/section/div/form/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/div/div/div[2]/section/p[1]',
                        'comodos': f'/html/body/div[1]/main/section/div/form/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/div/div/div[2]/section/p[2]',
                        'banheiros': f'/html/body/div[1]/main/section/div/form/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/div/div/div[2]/section/p[3]',
                        'vagas': f'/html/body/div[1]/main/section/div/form/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/div/div/div[2]/section/p[4]',
                        'valor': f'/html/body/div[1]/main/section/div/form/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/div/div/div[2]/div[3]/div[1]/p',
                    }
                }

                logradouro = self.driver.find_element(By.XPATH, xpats['XP']['logradouro'])
                rua = self.driver.find_element(By.XPATH, xpats['XP']['rua'])
                descricao = self.driver.find_element(By.XPATH, xpats['XP']['descricao'])
                metragem = self.driver.find_element(By.XPATH, xpats['XP']['metragem'])
                comodos = self.driver.find_element(By.XPATH, xpats['XP']['comodos'])
                banheiros = self.driver.find_element(By.XPATH, xpats['XP']['banheiros'])
                vagas = self.driver.find_element(By.XPATH, xpats['XP']['vagas'])
                valor = self.driver.find_element(By.XPATH, xpats['XP']['valor'])

                print(logradouro.text)
                print(rua.text)
                print(descricao.text)
                print(metragem.text)
                print(comodos.text)
                print(banheiros.text)
                print(vagas.text)
                print(valor.text)

            except NoSuchElementException:
                print('nao tem mais elementos nesta pagina')


imovel = Imovel()
imovel.main()