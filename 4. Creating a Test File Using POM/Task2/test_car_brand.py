import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class


def test_drive_custom_camping_option():
    driver = webdriver.Chrome()
    # Open the app - update the URL after starting the server
    driver.get('https://cnt-41064ba9-4507-4af6-8029-636eaab78c0d.containerhub.tripleten-services.com')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Step 1: Enter the "From" address
    ...

    # Step 2: Enter the "To" address
    ...

    # Step 3: Choose "Custom"
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 4: Click "Drive"
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 5: Click "Book"
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 6: Choose "Camping"
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 7: Check if the text displays "Audi A3 Sedan"
    actual_value = ...
    expected_value = ...
    assert ...
    driver.quit()
