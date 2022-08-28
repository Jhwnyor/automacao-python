from playwright.sync_api import sync_playwright
from utils.settings import settings, settings_input, settings_button


def login():
    """Faz login no instagram"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(settings.SITE)

        # isso faz ele esperar 700 millesimos de segundos
        page.wait_for_timeout(700)

        page.fill(settings_input.INPUT_EMAIL, settings.EMAIL)
        page.fill(settings_input.INPUT_SENHA, settings.SENHA)
        
        page.click(settings_button.BUTTON_LOGIN)

        # espera 10 seg, tirar depois
        page.wait_for_timeout(10000)

        browser.close()
