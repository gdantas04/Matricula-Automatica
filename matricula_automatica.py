# Leia https://motorscript.com/install-selenium-arch-linux/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from urllib.request import urlopen
from urllib.error import *


driver = webdriver.Chrome()

link = 'https://sigaa.unb.br/sigaa/portais/discente/discente.jsf'

driver.get(link);

login = 'sua_matricula'
senha = 'sua_senha'
data_nascimento = 'dd/mm/yyyy'
codigo_componente = 'codigo_da_materia'
horario = 'horario_da_materia'
nome_prof = 'primeiro_nome_do_professor'

def check(url):
    try:
        html = urlopen(url)        
    except Exception as e:
        return 0
    else:
        return 1

# Efetuar login
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(login)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
driver.find_element(By.XPATH, '//*[@id="login-form"]/button').click()

while True:
    try:
        if check(link) == 0:
            driver.refresh()
            time.sleep(5)
        else:
            # Acessar aba de matricula extraordinaria
            driver.find_element(By.XPATH, '//*[@id="menu_form_menu_discente_j_id_jsp_340461267_98_menu"]/table/tbody/tr/td[1]/span[2]').click()
            driver.find_element(By.XPATH, '//*[@id="cmSubMenuID1"]/table/tbody/tr[13]/td[2]').click()
            driver.find_element(By.XPATH, '//*[@id="cmSubMenuID3"]/table/tbody/tr[3]/td[2]').click()

            # Buscar disciplina
            driver.find_element(By.XPATH, '//*[@id="form:txtCodigo"]').send_keys(codigo_componente)
            driver.find_element(By.XPATH, '//*[@id="form:txtHorario"]').send_keys(horario)
            driver.find_element(By.XPATH, '//*[@id="form:txtNomeDocente"]').send_keys(nome_prof)
            driver.find_element(By.NAME, 'form:buscar').send_keys("\n")
            driver.find_element(By.XPATH, '//*[@id="form:selecionarTurma"]/img').click()

            # Confirmar matrícula
            driver.find_element(By.XPATH, '//*[@id="j_id_jsp_334536566_1:Data"]').send_keys(data_nascimento)
            driver.find_element(By.XPATH, '//*[@id="j_id_jsp_334536566_1:senha"]').send_keys(senha)
            driver.find_element(By.XPATH, '//*[@id="j_id_jsp_334536566_1:btnConfirmar"]').click()
            Alert(driver).accept()
            
    except Exception as e:
        pass
