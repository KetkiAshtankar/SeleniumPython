from selenium import webdriver
# from selenium.webdriver.common.proxy import Proxy,ProxyType
import time

# change 'ip:port' with your proxy's ip and port
proxy_ip_port = 'http://35.185.196.38:3128'


# Create ChromeOptions object 
options = webdriver.ChromeOptions()
options.add_argument(f'--proxy-server= {proxy_ip_port}')

# Pass options to the Chrome WebDriver constructor
driver = webdriver.Chrome(options=options)

driver.get('https://mylocation.org/')

time.sleep(8)

driver.quit()