import time
from selenium import webdriver

from urban_routes_main_page import UrbanRoutesPage  # Import the POM class


def test_add_driver_license_custom_camping_option():
    driver = webdriver.Chrome()
    # Open the app - update the URL after starting the server
    driver.get('https://cnt-932267f3-a263-441e-ac4d-b70fa84058e0.containerhub.tripleten-services.com')

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

    # Step 7: Click “Add a driver’s license”
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 8: Fill out the “First name” field
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 9: Fill out the “Last name” field
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 10: Fill out the “Date of birth” field
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 11: Fill out the “Number” field
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 12: Click "title" to make the Add button clickable
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 13: Click “Add”
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 14: Check that the licence has been added
    actual_value = ...
    expected_value = ...
    assert ...
    driver.quit()


