#Carregamento do WebDriver;
from selenium import webdriver
from selenium.webdriver.common.by import By
#Importação do Pandas;
import pandas as pd

#Leitura do arquivo '.xlsx';
table = pd.read_excel('challenge.xlsx')

#Inicializa o webdriver do Chrome;
web = webdriver.Chrome()

#Abre o site do desafio;
web.get("https://www.rpachallenge.com/")

#Inicialização do desafio;
button = web.find_element(By.XPATH,'//button[text() = "Start" ]').click()

#Função para varrer as linhas e colunas da tabela;
for i, r in table.iterrows():        
    role = r['Role in Company']
    email = r['Email']
    first_name = r['First Name']
    last_name = r['Last Name']
    phone = r['Phone Number']
    company = r['Company Name']
    address = r['Address']

    #Preencher First Name;
    preenche.clear() 
    preenche = web.find_element(By.XPATH,"//input[@ng-reflect-name='labelFirstName']")
    preenche.send_keys(first_name)
    #Preencher Last Name;
    preenche.clear()
    preenche = web.find_element(By.XPATH,"//input[@ng-reflect-name='labelLastName']")
    preenche.send_keys(last_name)
    #Preencher Company Name;
    preenche.clear()
    preenche = web.find_element(By.XPATH,'//input[@ng-reflect-name="labelCompanyName"]')
    preenche.send_keys(company)
    #Preencher Role Company;
    preenche.clear()
    preenche = web.find_element(By.XPATH,'//input[@ng-reflect-name="labelRole"]')
    preenche.send_keys(role)
    #Preencher Adress;
    preenche.clear()
    web.find_element(By.XPATH,'//input[@ng-reflect-name="labelAddress"]')
    preenche.send_keys(address)
    #Preencher Email;
    preenche.clear()
    web.find_element(By.XPATH,'//input[@ng-reflect-name="labelEmail"]')
    preenche.send_keys(email)
    #Preencher Phone Number;
    preenche.clear()
    web.find_element(By.XPATH,'//input[@ng-reflect-name="labelPhone"]')
    preenche.send_keys(phone)
    #Pressionar botão de envio de formulário;
    button = web.find_element(By.XPATH,'//input[@value = "Submit"]')
    button.click()