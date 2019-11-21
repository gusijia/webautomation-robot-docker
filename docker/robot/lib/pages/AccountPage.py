from PageObjectLibrary import PageObject


class AccountPage(PageObject):
    PAGE_URL = "http://automationpractice.com/index.php?controller=my-account"

    _locators = {
        'home_button': '//*[@id="center_column"]/ul/li/a'
    }

    def _is_current_page(self):
        ''' override the function to check the page location, and
        raise an appropriate error if we are not on the correct page

        '''
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
            return False
        return True

    def click_the_home_button(self):
        """Clicks the home button on the page to go back to home page
        """
        with self._wait_for_page_refresh():
            self.selib.click_element(self.locator.home_button)
