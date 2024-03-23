<p align="center">
  <img width="400px" src="./.github/tcu-logo-tribunal-de-contas-da-uniao.png" href="TCU" />
</p>

JUS-TCU is a web-scraping project designed to retrieve data from the Brazilian Federal Court of Accounts. It accesses the website, downloads reports within a specified range chosen by the user, and utilizes regular expressions to extract decisions (known as acórdãos) from PDF files, saving them into an Excel file. These reports, posted weekly, hold significant importance for the Federal Court of Accounts and related entities.

I started this project because I was tired of manually adding reports to my department's spreadsheet at the Court of Accounts of the State of Rio de Janeiro. Seeing the opportunity to make things easier to me, I learned about regex (a way to find patterns in text), got over my initial doubts (everyone's scared of regex, right?), and decided to create a Python program to do the job automatically. It ended up doing about 95% of the work for me.

## How can I run?
1. Clone this repository:
   ```sh
   git clone https://github.com/joaocansi/jus-tcu.git
   ```

2. Access the project folder:
   ```sh
   cd jus-tcu
   ```

3. Install project dependencies:
   ```sh
   pip install openpyxl selenium docx2txt PyMuPDF webdriver-manager
   ```

4. Run the project:
   ```sh
   python src/main.py <from> <to>
   ```

Note: **&lt;from&gt;** and **&lt;to&gt;** are the range of reports. For example, if **&lt;from&gt;** equals 10 and **&lt;to&gt;** equals 20, the script will return the data from report number 10 to report number 20.
