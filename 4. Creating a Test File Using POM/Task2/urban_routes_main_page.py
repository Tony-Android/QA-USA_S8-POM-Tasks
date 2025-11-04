from selenium.webdriver.common.by import By


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    DRIVE_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    CAMPING_LOCATOR = (By.XPATH, '//img[@src="/static/media/camping.075c6361.svg"]')
    AUDI_TEXT_LOCATOR = (By.XPATH, '//div[@class="drive-preview-title"]')

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_custom_option(self):
        # Click Custom
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_drive_icon(self):
        # Click Drive Icon
        self.driver.find_element(*self.DRIVE_ICON_LOCATOR).click()

    def click_book_button(self):
        # Click Book Button
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    def click_camping(self):
        # Click Camping
        self.driver.find_element(*self.CAMPING_LOCATOR).click()

    def get_audi_text(self):
        # Return the "Audi" text
        return self.driver.find_element(*self.AUDI_TEXT_LOCATOR).text
