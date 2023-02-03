from seleniumpagefactory.Pagefactory import PageFactory


class Garage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "add_car_btn": ("XPATH", "//*[contains(text(), 'Add')]"),
        "user_name": ("CSS", ".username")
    }

    def click_add_car_btn(self):
        self.add_car_btn.click()

    def get_username(self):
        retrieved_username = self.user_name.get_text()
        assert retrieved_username == "demouser"