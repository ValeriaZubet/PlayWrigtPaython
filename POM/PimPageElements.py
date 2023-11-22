class PimPage:
    def __init__(self, page):
        self.page = page
        self.pim_locator = 'a[href="/web/index.php/pim/viewPimModule"]'
        self.employee_name_locator = 'input[placeholder="Type for hints..."]'
        self.submit_button_locator = 'button[type="submit"]'
        self.delete_button_locator = 'i[class="oxd-icon bi-trash"]'




    def test_access_pim(self, name):
        self.page.click(self.pim_locator)
        self.page.fill(self.employee_name_locator, name)
        self.page.click(self.submit_button_locator)
        self.page.click(self.delete_button_locator)






