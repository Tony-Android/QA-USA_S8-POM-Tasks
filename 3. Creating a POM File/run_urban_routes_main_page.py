import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage


def test_custom_bike_option():
    driver = webdriver.Chrome()
    driver.get('https://cnt-97436078-66cd-400f-8cb3-7b7fa8418f6a.containerhub.tripleten-services.com/')
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')
    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_bike_icon()
    time.sleep(2)
    actual_value = urban_routes_page.get_bike_text()
    expected_value = "Bike"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
    driver.quit()
