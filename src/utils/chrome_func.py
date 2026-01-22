from playwright.sync_api import sync_playwright

def open_chrome(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            channel="chrome"
        )
        page = browser.new_page()
        page.goto(url)
        input("종료하려면 엔터")
        browser.close()

open_chrome("https://www.naver.com")