from playwright.sync_api import Playwright, sync_playwright, expect
from POM.loginPageElementa import LoginPage
from POM.PimPageElements import PimPage
import pytest


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def test_valid_user(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(page)
    pim_page = PimPage(page)
    login_page.fill_username("Admin")
    login_page.fill_password("admin123")
    pim_page.test_access_pim("John Tan")

def test_an_invalid_user(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(page)
    pim_page = PimPage(page)
    login_page.fill_username("Admin")
    login_page.fill_password("admin123")
    pim_page.test_access_pim("Test test ")









    # expect(page.get_by_placeholder("Password")).to_be_visible()

    # page.get_by_placeholder("Type for hints...").first.click()
    # page.get_by_placeholder("Type for hints...").first.fill("manager1")
    # expect(page.get_by_role("button", name="Search")).to_be_visible()
    # page.get_by_role("button", name="Search").click()
    # page.locator("div:nth-child(2) > .oxd-table-row > div:nth-child(3) > div").click()
    # page.locator("form").filter(has_text="Employee Full NameNicknameEmployee IdOther IdDriver's License NumberLicense Expi").get_by_role("button").click()

    print("Yaay!")
    # ---------------------
    context.close()
    browser.close()



