from PageObjectLibrary import PageObject
class LoginPage(PageObject):
    PAGE_URL = "/index.php?controller=authentication&back=my-account"

    _locators = {
        "email": "id=email",
        "password": "id=passwd",
        "login_button":  "id=SubmitLogin"
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

    def enter_username(self, email):
        """Type the given text into the username field """
        self.selib.input_text(self.locator.email, email)

    def enter_password(self, password):
        """Type the given text into the password field"""
        self.selib.input_text(self.locator.password, password)

    def click_the_login_button(self):
        """Clicks the submit button on the form
        """

        # since this action causes the page to be refreshed, wrap
        # this in a context manager so it does't return until the
        # new page is rendered

        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.login_button)

    def click_the_login(self):
        """Clicks the submit button on the form

        For illustrative purposes, this uses the low level selenium
        functions for submitting the form
        """

        form = self.driver.find_element_by_xpath("//form[@id='%s']" % self.locator.form_id)

        # since this action causes the page to be refreshed, wrap
        # this in a context manager so it does't return until the
        # new page is rendered

        with self._wait_for_page_refresh():
            form.submit()
