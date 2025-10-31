from selenium import webdriver
import time
from urban_routes_main_page import UrbanRoutesPage

# Create a class for both tests
class TestUrbanRoutes:

    # Initialize the Chrome driver once for the class
    @classmethod
    def setup_class(cls):
        ...

    def test_custom_bike_option(self):
        self.driver.get('https://cnt-8f25f166-edc1-4f8d-b177-7e4079036890.containerhub.tripleten-services.com')
        urban_routes_page = UrbanRoutesPage(self.driver)
        ...
        assert ...

    def test_duration_custom_bike_option(self):
        self.driver.get('https://cnt-8f25f166-edc1-4f8d-b177-7e4079036890.containerhub.tripleten-services.com')
        urban_routes_page = UrbanRoutesPage(self.driver)
        ...
        assert ...

    # Close the browser after all tests are done
    @classmethod
    def teardown_class(cls):
        ...