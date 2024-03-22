import math
import re
import time

from modules.web import driver, wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from modules.report import Report

reports_per_page = 50
reports_url = 'https://portal.tcu.gov.br/jurisprudencia/boletins-e-informativos/'

class WebScraper:
    def __init__(self, range):
        self.range = range
        self.page = 1
        self.reports = []
        
    def start(self):
        driver.get(reports_url)
        self.reports_length = int(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'lum-pagination-total-count'))).text)
        self._scrape()
        self._populate_reports()
        
    def _scrape(self):
        if self.page > math.ceil(self.reports_length / 50):
            return
        
        table = wait.until(EC.visibility_of_element_located((By.ID, 'tabelapautas')))
        rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
        
                
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')            
            no_report, urls, release_date = cells[0].text, cells[1].get_attribute('innerHTML'), cells[2].text

            report = int(re.search(r'nº (\d+)', no_report).group(1))                        
            url = re.findall(r'(?<=href=")[^"]*', urls)[1]        
             
            if report <= self.range[1] and report >= self.range[0]:
                self.reports.append(Report(report, release_date, url))
                
            if report <= self.range[0]:
                return
            
        self._next_page()
        self._scrape()
        
    def _populate_reports(self):
        for report in self.reports:
            report.populate()
    
    def _next_page(self):
        next_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'lum-next')))
        next_button.click()
        self.page += 1
        time.sleep(2)
    

        