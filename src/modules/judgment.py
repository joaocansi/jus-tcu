from config.constants import driver, wait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Judgment:
    def __init__(self, type, judgment, year, header, body, url):
        self.judgment = judgment
        self.year = year
        self.header = header
        self.body = body
        self.url = url
        self.type = type.upper()
        self.session_date = ''
        self.process = ''
        self.rapporteur = ''
        self.subject = ''
        self.retry = False
        
    def populate(self):
        self.push_content()
        return
        
    def push_content(self):
        driver.get(self.url)  
        
        type = self._get_element_text_by_id('conteudo_tipo_processo')        
        if type != '':
            self.type = type
        
        self.session_date = self._get_element_text_by_id('conteudo_data_sessao')
        self.process = self._get_element_text_by_id('conteudo_processo').replace(' launch', '')
        self.rapporteur = self._get_element_text_by_id('conteudo_relator')
        self.subject = self._get_element_text_by_id('conteudo_assunto')
        
        if self.subject == '' and self.retry == False:
            self.retry = True
            self.push_content()
            
    def _get_element_text_by_id(self, id):
        try:
            return wait.until(EC.visibility_of_element_located((By.ID, id))).text
        except:
            return ''