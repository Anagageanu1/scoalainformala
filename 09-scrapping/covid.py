import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())
for zi in range(20, 27, 1):

    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{zi}-ianuarie-ora-13-00/")
    tabel = browser.find_element(by=By.CSS_SELECTOR, value='table')
    lista = tabel.text.split(' ')
    judet = lista[18:146:4] + lista[147:186:4]
    cazuri = lista[20:143:4] + lista[145:184:4] + lista[186:187:1]
    Dictionar = {'Județ': judet,  zi : cazuri}

    df = pd.DataFrame(Dictionar, columns=['Județ', zi])