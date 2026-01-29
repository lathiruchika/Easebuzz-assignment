from playwright.sync_api import sync_playwright
import os

def test_ui_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")

        page.check("input[value='radio2']")
        page.select_option("#dropdown-class-example", "option2")
        page.check("#checkBoxOption1")

        assert page.is_checked("#checkBoxOption1")
        
        os.makedirs("screenshots", exist_ok=True)

        page.screenshot(path="screenshots/ui_test_result.png", full_page=True)
        
        browser.close()