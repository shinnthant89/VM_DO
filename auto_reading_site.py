from selenium import webdriver
import time, random

links = ["http://latepyar.xyz/index.php/2021/12/09/usps-mail-carriers-allegedly-stole-credit-cards-as-part-of-huge-identity-theft-ring/",
         "http://latepyar.xyz/index.php/2021/12/09/amazon-fined-1-3-billion-for-abusing-market-position-in-italy/",
         "http://latepyar.xyz/index.php/2021/12/09/hello-world/"]
count =0;
while True:
    for link in links:
        driver = webdriver.Chrome()
        driver.get(link)
        print("Browser is reading...")
        height=driver.execute_script("return document.body.scrollHeight")
        Y=height/5
        for i in range(0,5):
            driver.execute_script("window.scrollTo(0,{})".format(Y))
            time.sleep(random.randint(5,15))
            Y+=Y
        count+=1
        print(count)
        driver.quit()
