from selenium import webdriver

# Provide the path to your ChromeDriver executable
driver = webdriver.Chrome('/path/to/chromedriver')

driver.get('https://app.duocards.com/')

username_input = driver.find_element_by_id('username')  # Replace 'username' with the actual ID of the username/email input
password_input = driver.find_element_by_id('password')  # Replace 'password' with the actual ID of the password input
login_button = driver.find_element_by_id('login')  # Replace 'login' with the actual ID of the login button

# Fill in the form inputs
username_input.send_keys('your_username')
password_input.send_keys('your_password')

# Submit the form
login_button.click()