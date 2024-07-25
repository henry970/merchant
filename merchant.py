import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://merchant-portal-dev.tgipay.com/signup")
driver.maximize_window()

Enter_firstName = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[1]/div[1]/div/div/input")
Enter_firstName.send_keys('henry')
time.sleep(5)

Enter_LastName = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[1]/div[2]/div/div/input")
Enter_LastName.send_keys("okolie")
time.sleep(5)

Enter_BusinessName = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[2]/div/div/input")
Enter_BusinessName.send_keys("henry Test")
time.sleep(5)

# replace the email please
Enter_email = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[3]/div/div/input")
Enter_email.send_keys("henryokoliel@gmail.com")
time.sleep(5)

Click_business_type_drop_down = driver.find_element(By.ID, "react-select-3-placeholder")
Click_business_type_drop_down.click()
time.sleep(5)

select_business_type = driver.find_element(By.XPATH, "//div[contains(text(),'Registered')]")
select_business_type.click()
time.sleep(5)

Enter_password = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[5]/div/div/input")
Enter_password.send_keys("Adaobi93@")
time.sleep(5)

Enter_repe = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[6]/div/div/input")
Enter_repe.send_keys("Adaobi93@")
time.sleep(5)
driver.execute_script("window.scrollBy(0, 50000);")
driver.execute_script("window.scrollBy(0, 5000);")

Click_check = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[7]/div/div/input")
Click_check.click()
time.sleep(5)

login_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/form/div[9]/button')
login_button.click()
time.sleep(5)


driver.quit()
