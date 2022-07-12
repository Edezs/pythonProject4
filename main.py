from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

# variable oben definieren damit sie global ist und nicht einzeln in jede Funktion übergeben werden muss Variablen
# und Funktiontsnamen bitte kleinschreiben, zusammengesetzte Wörter bei jedem Anfangsbuchstaben großschreiben und
# zusammen, wie bruttoSozialProdukt
driver = webdriver.Chrome('/Users/chromedriver')


# TODO: Google Image search funktioniert nur auf dem Handy
# TODO: Captcha
# TODO: Methode um Anzeigen durchzublättern


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


# wenn man die Funktion aufruft, dann für 'username' die Email einsetzen, usw. ist aber aktuell nicht
# funktionstüchtig wegen Captcha
def login(username, password):
    loginStartButton = driver.find_element(By.XPATH, '//*[@id="site-signin"]/nav/ul/li[3]/a')
    loginStartButton.click()
    usernameField = driver.find_element(By.NAME, 'loginMail')
    passwordField = driver.find_element(By.NAME, 'password')
    usernameField.clear()
    usernameField.send_keys(username)
    passwordField.clear()
    passwordField.send_keys(password)
    # TODO: Captcha umgehen?
    # workaround: manuell das captcha machen, ab dann autonom laufen lassen
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


# Diese Line kann man sich theoretisch sparen, wäre vielleicht übersichtlicher aber sie erfüllt wohl irgendein
# Sicherheitsfeature, dass man die Mainmethode nicht ausversehen aufruft

driver.get('https://www.ebay-kleinanzeigen.de/')
driver.find_element(By.XPATH, '//*[@id="gdpr-banner-accept"]').click()
search('stuhl')

anzeige = driver.find_element(By.XPATH, '//*[@id="srchrslt-adtable"]/li[1]/article/div[1]/a/div/img')  # aditem-image
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

# for i in range(6):
#     anzeige = driver.find_element(By.CLASS_NAME, 'aditem-image')
#     print(anzeige.id)
#     driver.refresh()
#     sleep(2)

# option 1, immer die erste anzeige prüfen, dann refreshen
