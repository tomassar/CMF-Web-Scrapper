from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


def getNombresEmpresas():
    print("Entré a getNombresEmpresas")

    options = Options()
    options.headless = True
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    print(driver.get('https://www.cmfchile.cl/institucional/mercados/novedades_envio_sa_ifrs.php?mm_ifrs=12&aa_ifrs=2021'))
    
    # to identify the table rows
    table = driver.find_elements(By.XPATH,'//*[@id="tabla_resultado"]/tbody/tr')
    lengthTable = len(table)
    nombresEmpresasArr = []
    for i in range(1,1+lengthTable):
        nombreEmpresa = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[4]/table/tbody/tr["+str(i)+"]/td[3]").text
        nombresEmpresasArr.append({'value': nombreEmpresa, 'label': nombreEmpresa})
    return nombresEmpresasArr

def getLiquidezGeneral(nombreEmpresa):
    print("Entré a getliquidezgenerl")
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get('https://www.cmfchile.cl/institucional/mercados/novedades_envio_sa_ifrs.php?mm_ifrs=12&aa_ifrs=2021')
    element = driver.find_element(By.LINK_TEXT,nombreEmpresa)
    driver.execute_script("arguments[0].click();", element)
    '''
    #Set year
    selectYear = Select(driver.find_element(By.ID, 'aa'))
    selectYear.select_by_visible_text("2021")
    #Set balance type
    selectBalanceType = Select(driver.find_element(By.NAME, 'tipo'))
    selectBalanceType.select_by_visible_text("Individual")
    #Set norm type
    normType = Select(driver.find_element(By.NAME, 'tipo_norma'))
    normType.select_by_value("IFRS")
    #Click consultar
    buttonConsultar = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[4]/input')
    time.sleep(0.5)
    buttonConsultar.click()
    '''
    #Retrieving table with finance information
    activoCorrienteTotalElement = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[3]/div[4]/div[1]/div/div[1]/div/table/tbody/tr[14]/td[2]")
    pasivoCorrienteTotalElement = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[3]/div[4]/div[1]/div/div[1]/div/table/tbody/tr[45]/td[2]")
    #Should create a separate file to have all ratios formulae. But since this is a prototype I'm not gonna...
    activoCorrienteTotal = int(activoCorrienteTotalElement.text.replace('.',''))
    pasivoCorrienteTotal = int(pasivoCorrienteTotalElement.text.replace('.',''))

    liquidezGeneral = str(round(activoCorrienteTotal/pasivoCorrienteTotal,2))+" veces"
    print(liquidezGeneral)
    return liquidezGeneral

def hola():
    print("estoy en hola")
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('chromedriver', chrome_options=options)

    print(driver)
    print(driver.get('https://www.google.com/'))
    return "hola"