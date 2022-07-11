# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    driver = webdriver.Chrome('/Users/password1234/chromedriver')  # Optional argument, if not specified will search path.

    driver.get('http://www.ebay-kleinanzeigen.de/');

    time.sleep(1)  # Let the user actually see something!

    # knopf = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[1]/div")
    Cookie_accept_box = driver.find_element(By.XPATH, '//*[@id="gdpr-banner-accept"]')
    Cookie_accept_box.click()
    #
    time.sleep(1)  # Let the user actually see something!
    # //*[@id="site-signin"]/nav/ul/li[3]/a

    search_box = driver.find_element(By.XPATH, '//*[@id="site-search-query"]')
    search_box.send_keys('stuhl')
    search_box.submit()
    time.sleep(1)

    #pseudocode für einen Suchbegriff
    #anzeige finden
    #wenn werbung, dann überspringen, else
    #wenn anzeigenID nicht im Array gepruefte_Anzeigen enthalten ist, dann gleiches für die nächste Anzeigenid prüfen
    #wenn anzeigenid im Array gepruefte_Anzeigen enthalten ist, dann gehe zu der vorhergehenden Anzeige
    #     #   anklicken
    #     #   3+ fotos bei Google Bildersuche suchen
    #     #   wenn die ersten 10 suchergebnisse eines der stichwörter enthalten, dann anzeigenlink sichern in einer liste (stichwörter müssen wir alle auflisten)
    #     #   anzeigenid sichern in Liste gepruefte_Anzeigen
    #     #   zurück gehen in stuhlsuche bei EK und algorithmus erneut ausführen
    # wenn anzeigenid im Array gepruefte_Anzeigen enthalten ist und es darüber keine neuen Anzeigen gibt, dann
    #     #   sleep für 1200s, dann neu ausführen


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
