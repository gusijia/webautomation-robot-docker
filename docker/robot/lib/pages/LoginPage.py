from PageObjectLibrary import PageObject
class LoginPage(PageObject):
    PAGE_URL = "/index.php?controller=authentication&back=my-account"

    _locators = {
        "email": "id=email",
        "password": "id=passwd",
        "login_button":  "id=SubmitLogin",
        "email_create": "id=email_create",
        "create_account": "id=SubmitCreate",
        "create_account_error": '//*[@id="create_account_error"]/ol/li'
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

    def create_account_with(self, email):
        """Type the given text into the email field to create a new account"""
        self.selib.input_text(self.locator.email_create, email)
        self.selib.click_button(self.locator.create_account)

    def verify_account_exist_or_not(self):
        try:
            self._is_current_page()
        except Exception:
            return False
        
        count = self.selib.get_element_count(self.locator.create_account_error)
        result = self.selib.get_text(self.locator.create_account_error)
        if count and ("registered" in result):
            self.logger.info(f"An account has already been registered")
            return True

    def enter_email_address(self, email):
        """Type the given text into the email field to login"""
        self.selib.input_text(self.locator.email, email)

    def enter_password(self, password):
        """Type the given text into the password field"""
        self.selib.input_text(self.locator.password, password)

    def click_the_login_button(self):
        """Clicks the login button on the page
        """

        # since this action causes the page to be refreshed, wrap
        # this in a context manager so it does't return until the
        # new page is rendered

        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.login_button)
