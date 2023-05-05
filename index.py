from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import sys
import time
import random
import hashlib
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
time.sleep(10)
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
    
links = browser.find_elements(By.CLASS_NAME,"_5msj")
postLinks = []
for link in links:
     postLinks.append(link.get_attribute("href"))
#going through all the post links and grab the data
for index, link in enumerate(postLinks):
     browser.get(link)
     time.sleep(3)
     post_text = browser.find_element(By.CLASS_NAME, "_5rgt").text
     browser.get(link.replace("m.facebook.com", "mbasic.facebook.com")) #open the link
     post_images = browser.find_elements(By.CSS_SELECTOR, ".z.ba [data-ft] img")
     time.sleep(5)
     if len(post_images) >= 2:
          post_images = post_images.pop()

     imageUrls = []   
     if len(post_images) >0:
          for post in post_images:
               imageUrls.append(post.get_attribute("src"))

     imageNames= []
     if len(imageUrls) > 0:
          for image in imageUrls:
               browser.get(image)
               time.sleep(3)
               browser.save_screenshot("ss/"+str(index) + hashlib.sha256(image.encode("utf-8")).hexdigest() +".png")
               imageNames.append(str(index) + hashlib.sha256(image.encode("utf-8")).hexdigest() +".png")

     dataFile = open("items.csv", 'a', newline='\n', encoding='utf-8')
     writer = csv.writer(dataFile)
     writer.writerow([index, link, post_text, imageNames])
     dataFile.close()


# for i in links:
#     dataFile = open("items.txt", 'a', newline=' ', encoding='utf-8')
#     writer = csv.writer(dataFile)
#     writer.writerow([i.text,postLink[counter].get_attribute("href"), postTime[counter].text])
#     dataFile.close()
#     counter +=1
