from selenium.webdriver.common.by import By


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = ...
    TO_LOCATOR = ...
    CUSTOM_OPTION_LOCATOR = ...
    DRIVE_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = ...
    CAMPING_LOCATOR = ...
    AUDI_TEXT_LOCATOR = ...

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        ...

    def enter_to_location(self, to_text):
        # Enter To
        ...

    def click_custom_option(self):
        # Click Custom
        ...

    def click_drive_icon(self):
        # Click Drive Icon
        ...

    def click_book_button(self):
        # Click Book Button
        ...

    def click_camping(self):
        # Click Camping
        ...

    def get_audi_text(self):
        # Return the "Audi" text
        ...
