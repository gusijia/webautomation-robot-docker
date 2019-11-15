from abc import ABCMeta

from PageObjectLibrary import PageObject

class BasePage(PageObject, metaclass=ABCMeta):

    _locators = {
        'sign_in': '//*[@id="header"]/div[2]/div/div/nav/div[1]/a[@class="login"]',
    }

    def click_sign_in(self):
        self.selib.wait_until_element_is_visible(self.locator.sign_in)
        with self._wait_for_page_refresh():
            self.selib.click_element(self.locator.sign_in)
