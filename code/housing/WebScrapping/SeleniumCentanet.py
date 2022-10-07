from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://hk.centanet.com/findproperty/en/list/buy?q=zUUqjvuFikoEGFwhqTFA&keyword='
driver.get(url)

housing_info_list = []
while True:
    driver.implicitly_wait(3)
    next_page = driver.find_elements(By.CLASS_NAME,'btn-next')
    housing_list = driver.find_elements(By.CSS_SELECTOR, '.property-text')
    for house in housing_list:
        try:
            title = house.find_elements(By.CSS_SELECTOR, '.title-lg')[0].text
            floor = house.find_elements(By.CSS_SELECTOR, '.title-sm')[0].text
            location = house.find_elements(By.CSS_SELECTOR, '.tag-adress')[0].text
            price = house.find_elements(By.CSS_SELECTOR, '.price')[0].text
            area = house.find_elements(By.CSS_SELECTOR, '.usable-area')[0].text
            housing_info = {
                'title': title,
                'floor': floor,
                'location': price,
                'area': area
            }
            housing_info_list.append(housing_info)
            print(len(housing_info_list))
        except:
            pass
    if len(next_page) < 1:
        print('no more pages left')
        break
    else:
        next_page_click = driver.find_elements(By.CLASS_NAME,'btn-next')[0]
        next_page_click.click()

housing = pd.DataFrame(housing_info_list)
housing.to_csv('centanet.csv', encoding='utf-8')