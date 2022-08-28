from playwright.sync_api import sync_playwright
from utils.settings import settings, settings_input


def login(email: str, senha: str):
    """Faz login no instagram"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(settings.SITE)

        # isso faz ele esperar 700 millesimos de segundos
        page.wait_for_timeout(700)

        # TODO colocar esses caras no .env e usar o InputsSettings para pegar
        input_email = "//html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"
        input_senha = "//html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"
        button_login = "//html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]"

        page.fill(input_email, settings_input.EMAIL)
        page.fill(input_senha, senha)

        page.click(button_login)

        # espera 10 seg, tirar depois
        page.wait_for_timeout(10000)

        browser.close()
