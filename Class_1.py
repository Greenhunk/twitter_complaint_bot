from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.down = 0
        self.up = 0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        button_reject = self.driver.find_element(By.ID, value="onetrust-reject-all-handler")
        button_reject.click()
        time.sleep(2)
        button_go = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        button_go.click()
        time.sleep(55)
        download_value = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = download_value.text
        print(f"Down: {self.down}")
        upload_value = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = upload_value.text
        print(f"Up: {self.up}")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        button_refuse_cookies = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]/div')
        button_refuse_cookies.click()
        time.sleep(2)
        button_sign_in = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a')
        time.sleep(3)
        button_cross = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div[2]/div/div/div/button')
        button_cross.click()
        time.sleep(2)
        button_sign_in.click()
        time.sleep(2)
        email_box = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        time.sleep(2)
        email_box.send_keys("Tanvir34975")
        time.sleep(2)
        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        next_button.click()
        time.sleep(1)
        password = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys('v%Fyr8Ea$o4y6X8(Y')
        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_button.click()
        time.sleep(4)
        twitter_post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        twitter_post.send_keys(f'Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when i pay for 100down/10up')
        time.sleep(2)
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()







