import time

import discord
import undetected_chromedriver as uc
from discord import Webhook, RequestsWebhookAdapter
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

linki = {
    '1': "https://mbasic.facebook.com/groups/1020756002181896",
    '2': "",
    '3': "",
    '4': "",
    '5': ""
}


def webhook_sender(uzyt, grupa, desc, when, jakagrupa):
    embed = discord.Embed(color=0xff0000)
    embed = discord.Embed(title="Znaleziono nowy post", url=jakagrupa)
    embed.add_field(name="Nazwa użytkownika", value=uzyt, inline=True)
    embed.add_field(name="Grupa", value=grupa, inline=True)
    embed.add_field(name="Czas", value=when, inline=True)
    embed.add_field(name="Opis", value=desc, inline=False)

    webhook = Webhook.from_url(
        "https://discord.com/api/webhooks/953063740952174632/JI10MKVDc7TwubNrOwLtjABdhQr_I0o8A7OgWlP_Y2RGazDjGAyCBCUbZq9zASwv7gdd",
        adapter=RequestsWebhookAdapter())

    webhook.send(content="@everyone", wait=False, username="Facebook Notificator",
                 avatar_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Facebook_f_logo_%282019%29.svg/1024px-Facebook_f_logo_%282019%29.svg.png",
                 tts=False, file=None, files=None, embed=embed, allowed_mentions=None)


def login():
    driver.get("https://www.facebook.com/login")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//button[@title='Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie']"))).click()
    time.sleep(0.5)
    email = driver.find_element_by_xpath("//input[@placeholder='Adres e-mail lub numer telefonu']").send_keys(
        "mikomiki730@gmail.com")
    time.sleep(1)
    passw = driver.find_element_by_xpath("//input[@placeholder='Hasło']").send_keys("")
    time.sleep(0.5)
    complete = driver.find_element(by=By.XPATH, value="//button[@name='login']").click()
    time.sleep(1)


def group():
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//body//div//article[1]")))
    newest = driver.find_element_by_xpath("//body//div//article[1]").text
    newest = newest.splitlines()
    uzyt_grupa = newest[0].split(">")
    desc = newest[1]
    when = newest[2]
    uzyt = uzyt_grupa[0]
    grupa = uzyt_grupa[1]
    return uzyt, grupa, desc, when


def main():
    login()
    driver.execute_script(f"window.open('https://www.google.com', 'new_window')")
    input()
    for i in range(5):
        i = i + 1
        link = str(i)
        driver.execute_script(f"window.open('{linki[link]}', '{i}')")
        print(i)
        time.sleep(0.5)

    time.sleep(0.5)
    olduser = []

    while True:
        for i in range(5):
            i = i + 1
            driver.switch_to.window(driver.window_handles[i])
            driver.refresh()
            time.sleep(1)
            danegrupy = group()
            link = str(i)
            if danegrupy[2] not in olduser:
                webhook_sender(danegrupy[0], danegrupy[1], danegrupy[2], danegrupy[3], linki[link])
                olduser.append(danegrupy[2])
                print(olduser)

        time.sleep(60)


if __name__ == '__main__':
    driver = uc.Chrome()
    driver.maximize_window()
    main()
