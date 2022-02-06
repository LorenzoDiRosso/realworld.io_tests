from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
from time import sleep

from datetime import datetime
now = datetime.now()
unique_number = now.strftime("%Y%m%d%H%M%S")

usernameString = 'User '+unique_number
emailString = 'test+'+unique_number+'@test.com'
passwordString = '1234'

driver = webdriver.Chrome('drivers/chromedriver')

driver.get('https://demo.realworld.io/#/register')

# Sets element to username
UsernameTextField = driver.find_element(By.CSS_SELECTOR, 'fieldset:nth-of-type(1) > .form-control.form-control-lg.ng-empty.ng-pristine.ng-untouched.ng-valid')
UsernameTextField.send_keys(usernameString)

EmailField = driver.find_element(By.CSS_SELECTOR, '.form-control.form-control-lg.ng-empty.ng-pristine.ng-untouched.ng-valid.ng-valid-email')
EmailField.send_keys(emailString)
# Add get year, month, day, time function later

PasswordField = driver.find_element(By.CSS_SELECTOR, '.form-control.form-control-lg.ng-empty.ng-pristine.ng-untouched.ng-valid')
PasswordField.send_keys(passwordString)
PasswordField.send_keys(Keys.ENTER)

##### ---------- #####

driver.implicitly_wait(50)

SettingsLink = driver.find_element(By.LINK_TEXT, 'Settings')
SettingsLink.click()

##### ---------- #####

UpdatedPasswordString = 'updated'+passwordString

#UsernameTextField_Settings = driver.find_element(By.CSS_SELECTOR, '[ng-disabled] .form-group:nth-of-type(2) [type]')
PasswordField_Settings = driver.find_element(By.CSS_SELECTOR, "[type='password']")
PasswordField_Settings.send_keys(UpdatedPasswordString)

updateSettingBtn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.pull-xs-right')
updateSettingBtn.click()

driver.get("https://demo.realworld.io/#/settings")

sleep(5) #temporary solution
#driver.implicitly_wait(500)

logOutBtn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-danger')
logOutBtn.click()

driver.implicitly_wait(50)

SignInLink = driver.find_element(By.LINK_TEXT, 'Sign in')
SignInLink.click()

driver.implicitly_wait(50)

emailField_SignIn = driver.find_element(By.XPATH, "//input[@type='email']")
passwordField_SignIn = driver.find_element(By.XPATH, "//input[@type='password']")

emailField_SignIn.send_keys(emailString)
passwordField_SignIn.send_keys(UpdatedPasswordString)
passwordField_SignIn.send_keys(Keys.ENTER)

assert (driver.find_element(By.LINK_TEXT, 'Settings'))
assert (driver.find_element(By.LINK_TEXT, 'Your Feed'))

driver.close()