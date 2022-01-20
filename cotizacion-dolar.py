from os import system
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
import pywhatkit as pw

#Generamos el browser
browser = webdriver.Chrome("./drivers/win32/chrome/chromedriver.exe")

# Logueo
dni = '' 
user = ''
pas = ''

# Maximiza tamaño de pantalla
browser.maximize_window()

# Carga de la pagina
browser.get("https://login.sailinginversiones.com/")

# Esperamos a que no se vea el aviso de cargando
WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "form-login")))

# Esperamos a que se vea el boton de login del formulario 
WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "usuario")))
browser.find_element(By.NAME, "Dni").send_keys(dni)
browser.find_element(By.ID, "usuario").send_keys(user)
browser.find_element(By.ID, "passwd").send_keys(pas)
browser.find_element(By.ID, "loginButton").click()

print("Ingresamos a la página")

# Esperamos a que carguen los datos
WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/section/section/div/div[2]/div[1]/div/div[1]/h3")))

# Vamos a la página de precios y esperamos
browser.get("https://login.sailinginversiones.com/Prices/Stocks")
WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "table_stocks-accionesLideres")))

# Clic en el botón de Favoritos y esperamos
browser.find_element(By.ID, "favoritos").click()
WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "lista-fav")))

# Extraemos datos
# CompraMEP
AL30Dcompra = browser.find_element_by_xpath("/html/body/div[4]/div[1]/section/section/div/div[1]/div[3]/div/div/div[2]/div[12]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[3]/td[8]").text 
AL30compra = browser.find_element_by_xpath("/html/body/div[4]/div[1]/section/section/div/div[1]/div[3]/div/div/div[2]/div[12]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[1]/td[7]").text   

# Eliminamos ','
AL30compra = AL30compra.replace(".", "")
AL30compra = AL30compra.replace(",", ".")
AL30Dcompra = AL30Dcompra.replace(".", "")
AL30Dcompra = AL30Dcompra.replace(",", ".")
mepcompra = float(AL30compra)/float(AL30Dcompra)

# VentaMEP
AL30venta = browser.find_element_by_xpath("/html/body/div[4]/div[1]/section/section/div/div[1]/div[3]/div/div/div[2]/div[12]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[1]/td[8]").text
AL30Dventa = browser.find_element_by_xpath("/html/body/div[4]/div[1]/section/section/div/div[1]/div[3]/div/div/div[2]/div[12]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[3]/td[7]").text

# Eliminamos $
AL30venta = AL30venta.replace(".", "")
AL30venta = AL30venta.replace(",", ".")
AL30Dventa = AL30Dventa.replace(".", "")
AL30Dventa = AL30Dventa.replace(",", ".")
mepventa = float(AL30venta)/float(AL30Dventa)

# CompraCCL
al30Ccompraccl = browser.find_element_by_xpath("/html/body/div[4]/div[1]/section/section/div/div[1]/div[3]/div/div/div[2]/div[12]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[5]/td[8]").text  
al30compraccl = browser.find_element_by_xpath("/html/body/div[4]/div[1]/section/section/div/div[1]/div[3]/div/div/div[2]/div[12]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[4]/td[7]").text

# Eliminamos $
al30compraccl = al30compraccl.replace(".", "")
al30compraccl = al30compraccl.replace(",", ".")
al30Ccompraccl = al30Ccompraccl.replace(".", "")
al30Ccompraccl = al30Ccompraccl.replace(",", ".")
cclcompra = float(al30compraccl)/float(al30Ccompraccl)

# VentaCCL
al30ventaccl = browser.find_element_by_xpath("/html/body/div[4]/div[1]/section/section/div/div[1]/div[3]/div/div/div[2]/div[12]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[4]/td[8]").text
al30Cventaccl = browser.find_element_by_xpath("/html/body/div[4]/div[1]/section/section/div/div[1]/div[3]/div/div/div[2]/div[12]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[5]/td[7]").text 

# Eliminamos $
al30ventaccl = al30ventaccl.replace(".", "")
al30ventaccl = al30ventaccl.replace(",", ".")
al30Cventaccl = al30Cventaccl.replace(".", "")
al30Cventaccl = al30Cventaccl.replace(",", ".")
if al30ventaccl and al30Cventaccl != "-":
    cclventa = float(al30ventaccl)/float(al30Cventaccl)
else: cclventa = 0

# Agregamos comisiones
mepcompra = mepcompra-(mepcompra*0.005)
mepventa = mepventa+(mepventa*0.005)
cclcompra = cclcompra-(cclcompra*0.005)
cclventa = cclventa+(cclventa*0.005)

# Carga de la pagina
browser.get("https://www.bna.com.ar/Personas")

# Esperamos a que se vea la cotización
WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "billetes")))

compranacion = browser.find_element_by_xpath("/html/body/main/div/div/div[4]/div[1]/div/div/div[1]/table/tbody/tr[1]/td[2]").text
ventanacion = browser.find_element_by_xpath("/html/body/main/div/div/div[4]/div[1]/div/div/div[1]/table/tbody/tr[1]/td[3]").text
compranacion = compranacion.replace(",", ".")
ventanacion = ventanacion.replace(",", ".")

solidario = float(ventanacion)+float(ventanacion)*0.35+float(ventanacion)*0.30

datos = ( "Hola, estas son las cotizaciones del dolar: ",
    "Compra DOLAR BANCO NACION:", compranacion,
    "Venta DOLAR BANCO NACION:", ventanacion,
    "SOLIDARIO (Venta Banco Nacion + Impuestos):", solidario,
    "Compra DOLAR MEP:", "$"+str(mepcompra),  
    "Venta DOLAR MEP:", "$"+str(mepventa),  
    "Compra CCL:", cclcompra,  
    "Venta CCL:", cclventa)
# Enviamos los datos
pw.sendwhatmsg_instantly("+541132935611",str(datos))