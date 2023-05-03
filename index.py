from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import sys
import time
import unidecode 
#for encode the all characters this is require
dataFile = ""

print("dan tikakin facebook load wela ei e enne m.facebook.com eka")
print("itapasse log wela adala page ekata yanna")
print("itapasse page eka poddak pahalata scroll karanna post 1k 2k load wenna")
print("itapasse ganna one post gana danna post godak dana page ekk nam ithin 1000k dammath awlak na me danne scan karanna one post gana")
print("itapasse hari aye enter ekk gahala balagena inna browser eka close karanna epa minimize karanna epa")
browser = webdriver.Chrome('chromedriver')
(browser.page_source).encode('utf-8')
browser.get("https://m.facebook.com")
time.sleep(20)
linkCount = int(input("how much link you need [page eke nathi tharam danna epa huthta 100k wage dapan parana ekak nam]"))

input('hit enter when need to start')
links = browser.find_elements(By.CLASS_NAME,"_5rgt")
print(links)

while linkCount > len(links):
      htmlPage = browser.find_element(By.TAG_NAME, "html")
      for i in range(20):
          time.sleep(0.5)
          htmlPage.send_keys(Keys.END)
      print(len(links))
      links = browser.find_elements(By.CLASS_NAME,"_5rgt")
    
links = browser.find_elements(By.CLASS_NAME,"_5rgt")
postLink = browser.find_elements(By.CLASS_NAME,"_5msj")
postTime = browser.find_elements(By.CLASS_NAME,"_36xo")
counter =0
for i in links:
    dataFile = open("items.txt", 'a', newline=' ', encoding='utf-8')
    writer = csv.writer(dataFile)
    writer.writerow([i.text,postLink[counter].get_attribute("href"), postTime[counter].text])
    dataFile.close()
    print(i.text)
    print(postLink[counter].get_attribute("href"))
    print(postTime[counter].text)
    counter +=1
