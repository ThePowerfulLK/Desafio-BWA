#Carregamento do WebDriver;
from selenium import webdriver
#Importação do Pandas;
import pandas as pd

#Leitura do arquivo '.xlsx';
table = pd.read_excel('challenge.xlsx')

#Inicializa o webdriver do Chrome;
web = webdriver.Chrome()

#Abre o site do desafio;
web.get("https://www.rpachallenge.com/")

#Inicialização do desafio;
button = web.find_element_by_xpath('//button[text() = "Start" ]')
button.click

#Função para varrer as linhas e colunas da tabela;
for i, r in table.iterrows():
    first_name = table.loc[i, "First Name"]
    last_name = table.loc[i, "Last Name"]
    company_name = table.loc[i, "Company Name"]
    role_company = table.loc[i, "Role in Company"]
    adress = table.loc[i, "Adress"]
    email = table.loc[i, "Email"]
    phone = table.loc[i, "Phone Number"]

    #Preencher First Name;
    preenche.clear() 
    preenche = web.find_element_by_xpath("//input[@ng-reflect-name='labelFirstName']")
    preenche.send_keys(first_name)
    #Preencher Last Name;
    preenche.clear()
    preenche = web.find_element_by_xpath("//input[@ng-reflect-name='labelLastName']")
    preenche.send_keys(last_name)
    #Preencher Company Name;
    preenche.clear()
    preenche = web.find_element_by_xpath('//input[@ng-reflect-name="labelCompanyName"]')
    preenche.send_keys(company_name)
    #Preencher Role Company;
    preenche.clear()
    preenche = web.find_element_by_xpath('//input[@ng-reflect-name="labelRole"]')
    preenche.send_keys(role_company)
    #Preencher Adress;
    preenche.clear()
    web.find_element_by_xpath('//input[@ng-reflect-name="labelAddress"]')
    preenche.send_keys(adress)
    #Preencher Email;
    preenche.clear()
    web.find_element_by_xpath('//input[@ng-reflect-name="labelEmail"]')
    preenche.send_keys(email)
    #Preencher Phone Number;
    preenche.clear()
    web.find_element_by_xpath('//input[@ng-reflect-name="labelPhone"]')
    preenche.send_keys(phone)
    #Pressionar botão de envio de formulário;
    button = web.find_element_by_xpath('//input[@value = "Submit"]')
    button.click