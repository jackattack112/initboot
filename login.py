import undetected_chromedriver as uc
import time
import os

driver = uc.Chrome()
##driver.get("https://account.proton.me/login")
##input("Press any value after logging in: ")
##driver.switch_to.new_window('tab')
driver.get("https://github.com/login")
input("Press any value after logging in: ")

os.system('curl -fsSL https://tailscale.com/install.sh | sh')
os.system('sudo tailscale up --accept-routes')

#keep windows open forever
while (1):
    time.sleep(999999999)
