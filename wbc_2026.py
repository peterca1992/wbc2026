from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#%%
#peterca19920909@gmail.com
#C@810909ca
#pin : 0909


url = "https://tradead.tixplus.jp/wbc2026/buy/bidding/listings/1517"
login_url = "https://tradead.tixplus.jp/wbc2026/login"

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()

#登入
driver.get(login_url)

user_input = driver.find_element(By.XPATH, '//*[@id=":r0:"]')
user_input.send_keys("peterca19920909@gmail.com")

password_input = driver.find_element(By.XPATH, '//*[@id=":r1:"]')
password_input.send_keys("C@810909ca")

login_go =  driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/form/div[2]/button')
login_go.click()


#刷票
driver.get(url)

end_code = "開始買進"
try_time = 0

while(end_code == "開始買進"):
    
    driver.get(url)
    time.sleep(1)
    check_sale_out = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[2]/div/div[1]/div/div[1]')
    
    if(check_sale_out.text.find('取引完了') == -1):
        
        select_ticket_type = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[2]/div/div[1]/div/div[1]')
        select_ticket_type.click()
        
        time.sleep(0.1)
        
        buy_it = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/div/a')
        buy_it.click()
        
        agree_1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[3]/div/label/span[1]/input')
        agree_1.click()
        
        agree_2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[3]/div[3]/label/span[2]')
        agree_2.click()
        
        next_page_agree = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[3]/div[3]/button[1]')
        next_page_agree.click()
        
        time.sleep(0.1)
        
        cridet_card_select = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[2]/div[1]/div/div/div/label/span[1]/input')
        cridet_card_select.click()
        
        next_page_cridet_card = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[2]/div[2]/div/button')
        next_page_cridet_card.click()
        
        time.sleep(1)
        
        cridet_card_check = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[2]/div[1]/div/div/div/div/div/label/span[1]/input')
        cridet_card_check.click()
        
        next_page_buy_it = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[2]/div[2]/div/button')
        next_page_buy_it.click()
        
        end_code = "水拉買到"

    try_time = try_time + 1    
    time.sleep(29)
    
    


















































