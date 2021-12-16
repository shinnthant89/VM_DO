from selenium import webdriver
import time, random

links = ["https://ouo.io/Vk6z3C","https://ouo.io/0J1tims","https://ouo.io/oEuOHi"]
count =0;
while True:
    for link in links:
        driver = webdriver.Chrome()
        driver.get(link)
        
        print("Browser is reading...")
        height=driver.execute_script("return document.body.scrollHeight")
        while height==0:pass
            
        time.sleep(random.randint(5,15))
        elem=driver.find_element_by_id("btn-main")
        if elem.text=="I'M A HUMAN":
            elem.click()
        time.sleep(5)
        elem=driver.find_element_by_id("btn-main")
        if elem.text=="GET LINK":
            elem.click()
        time.sleep(10)
        count+=1
        print(count)
        driver.quit()
