from modules.scraper import WebScraper
from modules.spreadsheet import Spreadsheet
from config.constants import download_path, output_path

import sys 
import os

def main():
  args = sys.argv
  x, y = int(args[1]), int(args[2])

  if not os.path.exists(download_path):
    os.makedirs(download_path)

  web_scraper = WebScraper((x, y))
  web_scraper.start()

  spreadsheet = Spreadsheet(web_scraper.reports)
  spreadsheet.populate()

if __name__ == '__main__':
  main()