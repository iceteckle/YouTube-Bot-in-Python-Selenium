from selenium import webdriver
import time


number_of_drivers = int(input("10 : " ))
time_to_refresh = int(input("1 : " ))
url = input("Enter URL : https://m.youtube.com/@copane_azus4521" )
drivers =[]

for i in range(number_of_drivers):
    drivers.append(webdriver.Chrome(executable_path = "chromedriver"))
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(number_of_drivers):
        drivers[i].refresh()
