from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook
from openpyxl.styles import Font
from datetime import datetime
import requests

chrome_options = Options()
#chrome_options.add_argument("--headless")  # Headless mód
chrome_options.add_argument("--disable-gpu")  # GPU kizárása
chrome_options.add_argument("--window-size=1920x1080")  # Ablakméret

# ChromeDriver service létrehozása
service = Service(ChromeDriverManager().install())

# WebDriver létrehozása a beállított opciókkal
driver = webdriver.Chrome(service=service, options=chrome_options)

# A lapozható oldal URL-je
url = "https://www.eudiakok.hu/diakmunka"

# Az "Érdekel" gombok linkjeinek gyűjtése
munkak_url_lista = []

while True:
    driver.get(url)
    time.sleep(3)  # Oldal betöltésének várakoztatása
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # "Érdekel" gombok URL-jeinek hozzáadása a listához
    munkak_url_lista.extend([a['href'] for a in soup.find_all('a', href=True, string='Érdekel')])

    # Lapozás kezelése
    tovabb_gomb = soup.find('a', string='Tovább')
    if tovabb_gomb and 'href' in tovabb_gomb.attrs:
        url = tovabb_gomb['href']
    else:
        break

# WebDriver bezárása
driver.quit()

# Excel létrehozása
wb = Workbook()
ws = wb.active

# Fejlécek beállítása
fejlecek = ["Munkavégzés helye", "Fizetés", "Elvárt óraszám", "Munkakör", "Céginformáció", "Feladat", "Munkaidő", "Elvárás", "Egyéb infó"]
ws.append(fejlecek)
for cell in ws["1:1"]:
    cell.font = Font(bold=True)

# Az összegyűjtött URL-ek feldolgozása és adatok hozzáadása az Excelhez
for url in munkak_url_lista:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    munka_info = {key: '' for key in fejlecek}
    for key in fejlecek:
        element = soup.find('h5', string=lambda text: text and key in text)
        if element:
            detail_element = element.find_next_sibling('div', class_='details') or element.find_next('div', class_='info-desc')
            if detail_element:
                munka_info[key] = ' '.join(detail_element.stripped_strings).replace('\n', ' ')
    ws.append(list(munka_info.values()))


# Oszlopszélesség beállítása
for column_cells in ws.columns:
    length = max(len(str(cell.value)) for cell in column_cells)
    ws.column_dimensions[column_cells[0].column_letter].width = length


# Excel fájl mentése
current_date = datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
file_name = f"Eudiákok_{current_date}.xlsx"
wb.save(file_name)

