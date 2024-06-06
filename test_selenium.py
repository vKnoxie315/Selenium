from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configura il percorso del WebDriver
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

try:
    # Apri la pagina JSP
    driver.get("http://localhost:8080/index.jsp")

    # Trova l'elemento per l'input del nome utente
    input_element = driver.find_element_by_id("username")
    input_element.send_keys("Mario Rossi")

    # Invia il form
    input_element.send_keys(Keys.RETURN)

    # Aspetta un po' per vedere i risultati
    time.sleep(2)

    # Verifica l'output atteso nella pagina di risposta
    greetings = driver.find_element_by_tag_name("h1").text
    assert "Bentornato, Mario Rossi" in greetings
    print("Test Passed: Username is displayed correctly.")
except Exception as e:
    print("Test Failed:", e)
finally:
    driver.quit()
