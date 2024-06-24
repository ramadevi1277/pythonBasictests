from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(ChromeDriverManager().install())


driver.maximize_window()
driver.get("https://www.amazon.in/")
search_field = driver.find_element(By.ID, "twotabsearchtextbox")
search_field.send_keys("dresses for women")
search_field.send_keys(Keys.ENTER)


elements = driver.find_elements(By.XPATH, "//span[@class='a-price']//span[@class='a-price-whole']")
for price_text in elements:
    text = price_text.text
    if text == "499":
        item_name = price_text.find_element(By.XPATH, "preceding::h2[3]").text
        print(item_name)