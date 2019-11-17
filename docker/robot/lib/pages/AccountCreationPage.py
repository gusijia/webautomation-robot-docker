from PageObjectLibrary import PageObject

class AccountCreationPage(PageObject):
    PAGE_URL = "/index.php?controller=authentication&back=my-account#account-creation"

    _locators = {
        'sign_in': '//a[@class="login"]',
        'personal_info': {
            'user_firstname':'//*[@id="customer_firstname"]',
            'user_lastname':'//*[@id="customer_lastname"]',
            'passwd':'//*[@id="passwd"]'
        },
        'address': {
            'first_name':'//*[@id="firstname"]',
            'last_name':'//*[@id="lastname"]',
            'user_address':'//*[@id="address1"]',
            'city': '//*[@id="city"]',
            'state': '//*[@id="id_state"]',
            'zip_code':'//*[@id="postcode"]',
            'country': '//*[@id="id_country"]',
            'phone_number':'//*[@id="phone_mobile"]'
        },
        'register_button':'//*[@id="submitAccount"]'
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

    def enter_personal_information(self, firstname, lastname, passwd):
        self.selib.input_text(self.locator.personal_info.user_firstname, firstname)
        self.selib.input_text(self.locator.personal_info.user_lastname, lastname)
        self.selib.input_text(self.locator.personal_info.passwd, passwd)

    def enter_address(self, address, city, state, zip_code, country, phone_number):

        self._verify_name_fields()

        self.selib.input_text(self.locator.address.user_address, address)
        self.selib.input_text(self.locator.address.city, city)
        self.selib.select_from_list_by_index(self.locator.address.state, state)
        self.selib.input_text(self.locator.address.zip_code, zip_code)
        self.selib.select_from_list_by_index(self.locator.address.country, country)
        self.selib.input_text(self.locator.address.phone_number, phone_number)

    def _verify_name_fields(self):
        user_firstname = self.selib.get_text(self.locator.personal_info.user_firstname)
        firstname = self.selib.get_text(self.locator.address.first_name)
        user_lastname = self.selib.get_text(self.locator.personal_info.user_lastname)
        lastname = self.selib.get_text(self.locator.address.last_name)
        self.builtin.should_be_equal(user_firstname, firstname)
        self.builtin.should_be_equal(user_lastname, lastname)

    def click_register_button(self):
        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.register_button)
