from PageObjectLibrary import PageObject


class OrderPage(PageObject):
    PAGE_URL = "/index.php?controller=order"

    _locators = {
        'checkout_button': '//*[@id="center_column"]/p[2]/a[1]',
        'product_count': '//*[@id="summary_products_quantity"]'
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

    def verify_product_in_cart(self):
        self.selib.element_should_be_visible(self.locator.product_count)
        self.selib.element_text_should_be(
            self.locator.product_count, '1 Product')
