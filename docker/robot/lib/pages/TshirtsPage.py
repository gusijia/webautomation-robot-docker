from PageObjectLibrary import PageObject


class TshirtsPage(PageObject):
    PAGE_URL = "/index.php?id_category=5&controller=category"

    _locators = {
        'shirt_img': '//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img',
        'add_to_cart': '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]',
        'continue_shopping': '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span',
        'go_to_cart': '//*[@id="header"]/div[3]/div/div/div[3]/div/a'
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

    def add_to_cart(self):
        self.selib.mouse_over(self.locator.shirt_img)
        self.selib.wait_until_element_is_visible(self.locator.add_to_cart)
        self.selib.click_element(self.locator.add_to_cart)
        self.selib.wait_until_element_is_visible(
            self.locator.continue_shopping)
        self.selib.click_element(self.locator.continue_shopping)

    def go_to_cart(self):
        with self._wait_for_page_refresh():
            self.selib.click_element(self.locator.go_to_cart)
