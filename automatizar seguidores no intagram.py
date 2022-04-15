from selenium import webdriver
import time

navegador = webdriver.Chrome("chromedriver.exe")

navegador.get("http://intagram.com/") #entrar no site
time.sleep(2)

navegador.find_element_by_xpath('').send_keys("nome") #login
navegador.find_element_by_xpath('').send_keys("senha")
navegador.find_element_by_xpath('').click()
time.sleep(3)

navegador.find_element_by_xpath('').click() #n salvar senha
time.sleep(2)

navegador.find_element_by_xpath('').click() #agora n da notificação
time.sleep(1)

navegador.find_element_by_xpath('').click() #clicar na barra de pesquisa
navegador.find_element_by_xpath('').send_keys("nome_da_pagina")
time.sleep(5)

navegador.find_element_by_class_name('-qQT3').click #classe do elemento
time.sleep(3)

navegador.find_element_by_xpath('').click() #clicar na barra de pesquisao botão seguir
