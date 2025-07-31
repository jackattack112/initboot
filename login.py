import undetected_chromedriver as uc
import time
driver = uc.Chrome()
driver.get("https://account.proton.me/login")
driver.switch_to.new_window('tab')
driver.get("https://github.com/login")
#keep windows open forever
while (1):
    time.sleep(999999999)
