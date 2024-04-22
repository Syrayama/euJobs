from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import time
from datetime import datetime




chrome_options = Options()
#chrome_options.add_argument("--headless")  # Headless mód
chrome_options.add_argument("--disable-gpu")  # GPU kizárása
chrome_options.add_argument("--window-size=1920x1080")  # Ablakméret

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://cloud.qdiak.hu/munkak"

# Excel munkafüzet és munkalap inicializálása
wb = Workbook()
ws = wb.active
# Excel fejlécek beállítása
ws.append(["Munka URL-je", "Munka neve", "Alapbér", "Heti óraszám", "Kategória"])

munkak_url_lista = []

driver.get(url)
time.sleep(2)

while True:
    elements = driver.find_elements(By.CSS_SELECTOR, 'a.MuiLink-underlineHover, a.MuiTypography-h6')
    for element in elements:
        full_url = f"{element.get_attribute('href')}"
        if full_url not in munkak_url_lista:  # Ellenőrizzük, hogy az URL már szerepel-e a listában
            munkak_url_lista.append(full_url)

    try:
        next_button = driver.find_element(By.XPATH, '//button[@aria-label="Go to next page"]')
        if next_button.is_enabled():  # Csak akkor kattintson, ha a gomb kattintható
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(2)  # Adjon időt az oldalnak a frissítésre
        else:
            break  # Ha a gomb nem kattintható, kilép a ciklusból
    except NoSuchElementException:  # Ha nincs "következő oldal" gomb, kilép a ciklusból
        break

for url in munkak_url_lista:
    driver.get(url)
    time.sleep(2)
    try:
        munka_neve = driver.find_element(By.CSS_SELECTOR, 'h1.MuiTypography-root.MuiTypography-h3').text
        alapber_szoveg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(), 'Alapbér')]/following-sibling::p"))).text
        oraszam_szoveg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//h6[contains(text(), 'Heti óraszám')]/following-sibling::p"))).text
        kategoria_szoveg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//h6[contains(text(), 'Kategória')]/following-sibling::p"))).text
    except (NoSuchElementException, TimeoutException):
        munka_neve = alapber_szoveg = oraszam_szoveg = kategoria_szoveg = "Nem található"

    # Adatok hozzáadása az Excelhez
    ws.append([url, munka_neve, alapber_szoveg, oraszam_szoveg, kategoria_szoveg])

driver.quit()

# Oszlopszélesség beállítása
for column_cells in ws.columns:
    length = max(len(str(cell.value)) for cell in column_cells)
    ws.column_dimensions[column_cells[0].column_letter].width = length

# Excel fájl mentése
current_date = datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
file_name = f"quantumdiak_{current_date}.xlsx"
wb.save(file_name)
