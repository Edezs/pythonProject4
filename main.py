from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
import pyautogui

# variable oben definieren damit sie global ist und nicht einzeln in jede Funktion übergeben werden muss Variablen
# und Funktiontsnamen bitte kleinschreiben, zusammengesetzte Wörter bei jedem Anfangsbuchstaben großschreiben und
# zusammen, wie bruttoSozialProdukt
driver = webdriver.Chrome('/Users/chromedriver')


# TODO: Ebay Kleineanzeigen hat imer eine andere REihenfolge wegen Werbung
# TODO: Methode um Anzeigen durchzublättern auswählen
# TODO: Telegrambot der die Anzeigen informiert


# Hier die Befehle ablegen die man ab und zu benutzt und nicht immer googlen muss
def usefulSyntax():
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')  # allgemeine Form für cmd +t eintippen
    driver.refresh()  # site aktualisieren
    driver.back()  # geht eine Seite zurück, allerdings nicht sure wie es genau funktioniert
    driver.execute_script("window.open('http://bings.com', '_blank');")  # neuen Tab öffnen
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()  # funktioniert nicht
    driver.execute_script("window.open('http://bings.com');")
    driver.switch_to.window(driver.window_handles[1])
    # if __name__ == '__main__': #aus convienience erstmal gelöscht
    print(pyautogui.size())
    print(pyautogui.onScreen(1504, 0))



def login(username, password):
    loginStartButton = driver.find_element(By.XPATH, '//*[@id="site-signin"]/nav/ul/li[3]/a')
    loginStartButton.click()
    usernameField = driver.find_element(By.NAME, 'loginMail')
    passwordField = driver.find_element(By.NAME, 'password')
    usernameField.clear()
    usernameField.send_keys(username)
    passwordField.clear()
    passwordField.send_keys(password)

    # TODO: Captcha
    driver.find_element(By.ID, 'login-submit').click()
    return


# just experimenting with opening a new tab
def newTab(url):
    driver.execute_script(f"window.open('https://{url}');")  # String interpolation
    driver.switch_to.window(driver.window_handles[1])
    # driver.get(f'http://{url}')
    sleep(3)


# gibt Probleme, weil ebay dann immer wieder fragt
def denyCookie():
    cookieDenyBox = driver.find_element(By.ID, 'gdpr-banner-cmp-button')
    cookieDenyBox.click()
    driver.find_element(By.XPATH, '//*[@id="ConsentManagementPage"]/div[1]/button[1]').click()


def search(name):
    searchBox = driver.find_element(By.XPATH, '//*[@id="site-search-query"]')
    searchBox.send_keys(name)
    searchBox.submit()


def oldGoogleSearch(anzeige):
    ImgSrc = anzeige.get_attribute('src')  # kopiert den Link zum Bild
    newTab('images.google.com')
    driver.find_element(By.ID, 'W0wltc').click()  # Google Cookie box ablehnen
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'ZaFQO').click()  # Die kleine Kamera bei Google bilder
    sleep(1)
    googleImageSearchBox = driver.find_element(By.ID, 'Ycyxxc')  # Google Suchfeld
    googleImageSearchBox.clear()
    print(ImgSrc)
    googleImageSearchBox.send_keys(ImgSrc)
    googleImageSearchBox.submit()


# Diese Line kann man sich theoretisch sparen, wäre vielleicht übersichtlicher aber sie erfüllt wohl irgendein
# Sicherheitsfeature, dass man die Mainmethode nicht ausversehen aufruft

driver.get('https://www.ebay-kleinanzeigen.de/')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="gdpr-banner-accept"]').click()
sleep(2)
search('stuhl')
sleep(3)

#anzeige = driver.find_element(By.XPATH, '//*[@id="srchrslt-adtable"]/li[1]/article/div[1]/a/div/img')  # aditem-image
anzeigen = driver.find_elements(By.CLASS_NAME, 'aditem-image')
#oldGoogleSearch(anzeige)
#driver.close()

action = ActionChains(driver)

pyautogui.moveTo(600, 370)
pyautogui.scroll(-25)

action.context_click(anzeigen[2]).perform() #klickt die 3. Anzeige an (1. wirkliche Anzeige)
pyautogui.move(30,280) #moved die Maus auf den Lens knopf
pyautogui.leftClick()
sleep(1)
#pyautogui.moveTo(300,40)
#pyautogui.leftClick()

