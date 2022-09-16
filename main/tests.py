import pytest
from django.conf import settings
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    pytestmark = pytest.mark.django_db

    @classmethod
    def setUpClass(cls):
        # Selenium specific
        selenium_driver_path = getattr(
            settings,
            'SELENIUM_DRIVER_EXECUTABLE_PATH',
            None
        )
        selenium_driver_options = getattr(
            settings,
            'SELENIUM_DRIVER_OPTIONS',
            None
        )
        cls.driver = webdriver.Firefox()

        super(PlayerFormTest, cls).tearDownClass()

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except Exception as err:
            print(err)

        super(PlayerFormTest, cls).tearDownClass()

    def test_form(self):
        # Choose your url to visit
        self.driver.get('http://localhost:8000')
        # find the elements you need to submit form
        player_name = self.driver.find_element(By.ID, 'id_name')
        player_height = self.driver.find_element(By.ID, 'id_height')
        player_team = self.driver.find_element(By.ID, 'id_team')
        player_ppg = self.driver.find_element(By.ID, 'id_ppg')

        submit = self.driver.find_element(By.ID, 'submit_button')

        # populate the form with data
        player_name.send_keys('Lebron James')
        player_team.send_keys('Los Angeles Lakers')
        player_height.send_keys('6 feet 9 inches')
        player_ppg.send_keys('25.7')

        # submit form
        submit.send_keys(Keys.RETURN)

        # check result; page source looks at entire html document
        assert 'Lebron James' in self.driver.page_source
