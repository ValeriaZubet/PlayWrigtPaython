class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_locator = 'input[placeholder="Username"]'
        self.password_locator = 'input[placeholder="Password"]'

    def fill_username(self, value):
        self.page.fill(self.username_locator, value)

    def fill_password(self, value):
        self.page.fill(self.password_locator, value)
        self.page.press(self.password_locator, "Enter")
