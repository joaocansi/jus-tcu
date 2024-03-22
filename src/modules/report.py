import requests
import docx2txt
import os
import re
import fitz
from  threading import Thread

from utils.file import save_file
from config.file import path

from modules.judgment import Judgment


class Report:
    def __init__(self, report, release_date, url):
        self.report = report
        self.release_date = release_date
        self.url = url
        self.judgments = []
        
    def populate(self):
        self._download()
        self._push_content()
        self._populate_judgments()
        
    def _download(self):
        pdf_response = requests.get(self.url)
        docx_response = requests.get(self.url.replace('&amp;', '&'))    
        
        if pdf_response.status_code != 200 or docx_response.status_code != 200:
            return
        
        filename = 'BJ-' + str(self.report)
        
        save_file(docx_response.content, path, filename, 'docx')
        save_file(pdf_response.content, path, filename, 'pdf')
        
    def _push_content(self):
        texts = self._get_text()
        links = self._get_links()
        
        if len(texts) != len(links):
            return
        
        print('Boletim ' + str(self.report))                        
        for i in range(0, len(texts)):
            content, url = texts[i], links[i]
            
            type = content[2]
            type = re.findall(r'\((.*),.*(?=\))', type)[0] or ''
            
            self._create_judgment(type, content[0], content[1], content[3], content[4], url)
        
        
    def _populate_judgments(self):
        for judgment in self.judgments:
            judgment.populate()
            
    def _create_judgment(self, type, judgment, year, header, body, url):
        judgment_obj = Judgment(type, judgment, year, header, body, url)
        print('    - ' + str(judgment) + ' [Downloading...]')
        judgment_obj.populate()
        self.judgments.append(judgment_obj)
        return judgment_obj
 
    def _get_text(self):
        pattern = r'(?<!.)(?:Acórdão) (?:(\d{1,5})\/(\d{4}))(.*?)(?=\n)\n\n(.*)\n\n(.*?)(?=\n)'
        
        content = docx2txt.process(os.path.join(path, 'BJ-' + str(self.report) + '.docx'))
        content = re.findall(pattern, content)
        
        return content
    
    def _get_links(self):
        links = []
        pdf_document = fitz.open(os.path.join(path, 'BJ-' + str(self.report) + '.pdf'))

        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            page_links = page.get_links()
            for link in page_links:
                url = link.get('uri')
                if not url or not url.startswith('https://contas.tcu.gov.br/pesquisaJurisprudencia/#/detalhamento'):
                    continue
                links.append(url)

        pdf_document.close()
        return links

        