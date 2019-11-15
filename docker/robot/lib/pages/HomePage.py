from PageObjectLibrary import PageObject
class HomePage(PageObject):
    PAGE_URL = "/index.php"

    _locators = {
        'sign_in': '//a[@class="login"]',
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
        return True

    def click_sign_in(self):
        self.selib.wait_until_element_is_visible(self.locator.sign_in)
        with self._wait_for_page_refresh():
             self.selib.click_element(self.locator.sign_in)
