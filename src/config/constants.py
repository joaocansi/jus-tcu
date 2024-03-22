import os

from openpyxl.styles import Alignment
from openpyxl.cell.text import InlineFont
from openpyxl.cell.rich_text import TextBlock, CellRichText
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_argument('log-level=3')
options.add_argument("start-maximized")
options.add_argument("--disable-gpu")

driver = Chrome(options, service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

output_path = os.path.join(os.getcwd(), 'out')
download_path = os.path.join(output_path, 'downloads')

bold = InlineFont(b=True)
b = TextBlock

class Column:
    def __init__(self, width, alignment):
        self.width = width
        self.alignment= alignment

columns = (
    CellRichText(b(bold, "Tipo")), 
    CellRichText(b(bold, "Assunto")),
    CellRichText(b(bold, "Acórdão")),
    CellRichText(b(bold, "Data / Sessão")),
    CellRichText(b(bold, "Relator")),
    CellRichText(b(bold, "Processo")),
    CellRichText(b(bold, "Boletim")),
    CellRichText(b(bold, "Decisão")),
    CellRichText(b(bold, "Data da Publicação")),
    CellRichText(b(bold, "Ano")),
)
        
columns_settings = {
    'A': Column(18.29, Alignment(wrap_text=True, vertical='center', horizontal='center')),
    'B': Column(36.57, Alignment(wrap_text=True, vertical='center')),
    'C': Column(12.00, Alignment(wrap_text=True, vertical='center', horizontal='center')),
    'D': Column(19.57, Alignment(wrap_text=True, vertical='center', horizontal='center')),
    'E': Column(15.57, Alignment(wrap_text=True, vertical='center', horizontal='center')),
    'F': Column(19.29, Alignment(wrap_text=True, vertical='center', horizontal='center')),
    'G': Column(10.71, Alignment(wrap_text=True, vertical='center', horizontal='center')),
    'H': Column(66.00, Alignment(wrap_text=True, vertical='center')),
    'I': Column(16.86, Alignment(wrap_text=True, vertical='center', horizontal='center')),
    'J': Column(11.86, Alignment(wrap_text=True, vertical='center', horizontal='center'))
}

