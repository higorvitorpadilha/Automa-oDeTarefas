import pyautogui
import time
#pyautogui.write -> escrever um texto 
#pyautogui,click -> clicar com o mouse 
#pyautogui.press -> apertar uma tecla
#pyautogui.hotkey -> apertar um atalho do teclado(ctrl, c)

pyautogui.PAUSE = 0.2

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#dar uma pausa em um lugar especifico e clicando em eixos especificos 
time.sleep(0.4)
pyautogui.click(x=621, y=410)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")   

pyautogui.write("minhasenha")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(x=530, y=309)


#importando a base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")
linha= 0

for linha in tabela.index:
    pyautogui.click(x=497, y=291)

    #cadastrando um produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca 
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo
    tipo= tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #categoria  Mouse 
    categoria= tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preco_unitario
    preco_unitatrio=tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitatrio))
    pyautogui.press("tab")
    #custo
    custo= tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)


    print(tabela)