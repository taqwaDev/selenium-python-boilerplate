import csv
# import sele
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

# # sesuaikan dengan driver browser
# option = webdriver.ChromeOptions()
# # komment ketika tidak ingin menampilkan browser
# option.add_argument('headless')
# driver = webdriver.Chrome(
#     './chromedriver_win32/chromedriver.exe', options=option)

# uncoment ketika ingin menampilkan browser
driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
# input URL nya disini
driver.get("http://13.250.157.96/")

# test laoding time dan speed time....
navigationStart = driver.execute_script(
    "return window.performance.timing.navigationStart")
domContentLoadedEventEnd = driver.execute_script(
    "return window.performance.timing.domContentLoadedEventEnd")
loadEventEnd = driver.execute_script(
    "return window.performance.timing.loadEventEnd")

backendPerformance = (domContentLoadedEventEnd - navigationStart)/1000
frontendPerformance = (loadEventEnd - navigationStart)/1000

# csv output

# open file / inisialisasi filenya
f = open('./csv_output/test.csv', 'w')

header = ['page', 'duration load', 'page load', 'status']
data = [driver.title, backendPerformance, frontendPerformance, 'success']

# buat CSV nya
writer = csv.writer(f)

# header
writer.writerow(header)
# wire data
writer.writerow(data)

# generate datanya
print(writer)
f.close()

print(backendPerformance, "load script data", driver.title)
print(frontendPerformance, "load performance page", driver.title)
print()
driver.close()
