from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import ui


def checkFoto(foto):
    return


if __name__ == '__main__':

    driver = webdriver.Chrome('/Users/chromedriver')
    driver.get('http://www.ebay-kleinanzeigen.de/')
    sleep(1)
    cookieAcceptBox = driver.find_element(By.XPATH, '//*[@id="gdpr-banner-accept"]')
    cookieAcceptBox.click()

    searchBox = driver.find_element(By.XPATH, '//*[@id="site-search-query"]')
    searchBox.send_keys('stuhl')
    searchBox.submit()
    sleep(1)
    #TODO: check if
    anzeigen = driver.find_elements(By.CLASS_NAME, 'aditem-image')

    for i in range(6):
        anzeige = driver.find_element(By.CLASS_NAME, 'aditem-image')
        print(anzeige.id)
        driver.get('https://www.google.com?q=python#q=python')
        sleep(2)
        first_result = ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_class_name('rc'))
        first_link = first_result.find_element_by_tag_name('a')

        # Save the window opener (current window, do not mistaken with tab... not the same)
        main_window = driver.current_window_handle

        # Open the link in a new tab by sending key strokes on the element
        # Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
        first_link.send_keys(Keys.CONTROL + Keys.RETURN)

        # Switch tab to the new tab, which we will assume is the next one on the right
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

        # Put focus on current window which will, in fact, put focus on the current visible tab
        driver.switch_to_window(main_window)

        # do whatever you have to do on this page, we will just got to sleep for now
        sleep(2)

        # Close current tab
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

        # Put focus on current window which will be the window opener
        driver.switch_to_window(main_window)
     #   print(anzeige.id)
      #  #anzeige.click()
       # #time.sleep(1)
        ##driver.back()
        #driver.get("https://www.tutorialspoint.com/questions/index.php")
      #  print("Current Page title: " + driver.title)
       # driver.back()


    #option 1, immer die erste anzeige prüfen

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
