import urllib3
from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:/Users/Admin/chromedriver.exe')
driver.get('https://web.whatsapp.com/')
name=input("Enter the name")
msg=input("Enter the message")
count=int(input("Enter the count"))
input("Enter anything after scanning QR code")
user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
msg_box=driver.find_element_by_class_name('_2S1VP')
for i in range(count):
	msg_box.send_keys(msg)
	button=driver.find_element_by_class_name('_35EW6')
	button.click()