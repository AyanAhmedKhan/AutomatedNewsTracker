from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
from datetime import datetime 

driver = webdriver.Chrome()  
driver.get("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
                                    
while True: 
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S") 
    print(f'At time : {current_time} IST') 
    c = 1
  
    for x in range(2, 4): 
        curr_path = f'/html/body/c-wiz/div/div[2]/main/div[2]/c-wiz/section/div[2]/div/div[{x}]/c-wiz/c-wiz/div/article/a'
        
        try: 
            title = driver.find_element(By.XPATH, curr_path)
            print(f"Heading {c}: {title.text}") 
            c += 1
        except Exception as e: 
            print(f"Error: {e}")
            continue
          
    time.sleep(20)

# Made by Ayan Ahmed Khan
