import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service("drivers/chromedriver.exe"))
    driver.maximize_window()
    yield driver
    driver.quit()

# 1-Prueba automatizada para el login en la pagina web
    def test_login_success(driver):
        driver.get("https://aceenlinea.com/login") 
        time.sleep(10) 

    email_field = driver.find_element(By.NAME, "email")  
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".css-yv6mh2")  
 
    email_field.send_keys("guillermorotestanp@gmail.com")
    password_field.send_keys("1609Ga@2")
    login_button.click()

    element_present = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiBox-root.css-e8gita"))
    )

    assert element_present.is_displayed(), "El elemento con las clases MuiBox-root css-e8gita no se encontró o no está visible."

    driver.save_screenshot("screenshots/login_success.png")

# 2-Prueba automatizada para el login fallido
    def test_login_failure(driver):
        driver.get("https://aceenlinea.com/login")  
        time.sleep(5) 

    email_field = driver.find_element(By.NAME, "email")  
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".css-yv6mh2") 
 
    email_field.send_keys("correo_invalido@gmail.com")
    password_field.send_keys("contraseña_incorrecta")
    login_button.click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, ".MuiTypography-root.MuiDialogContentText-root.css-dj396x"))
    )

    assert error_message.is_displayed(), "No se mostró el mensaje de error esperado en el intento de inicio de sesión fallido."

    driver.save_screenshot("screenshots/login_failure.png")

# 3-Prueba automatizada para boton de registro
    def test_register_button_and_form(driver):
        driver.get("https://aceenlinea.com/login")  
        time.sleep(5)  

    register_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.css-seamqp"))
    )

    assert register_button.is_displayed(), "El botón de 'Registrarme' no se encontró o no está visible."

    register_button.click()

    registration_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedSecondary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-fullWidth.css-thaccl"))
    )

    assert registration_form.is_displayed(), "El formulario de registro no se mostró después de hacer clic en 'Registrarme'."

    first_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputSizeSmall.css-1o6z5ng"))
    )

    assert first_name_field.is_displayed(), "El campo de entrada para el primer nombre no está visible."

    driver.save_screenshot("screenshots/register_form_and_field_displayed.png")

# 4-Prueba automatizada para restablecer contraseña
    def test_reset_password_link(driver):
        driver.get("https://aceenlinea.com/login")  
        time.sleep(5) 

    reset_password_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-inherit.MuiLink-root.MuiLink-underlineNone.css-lgibdp"))
    )

    assert reset_password_link.is_displayed(), "El enlace de 'Restablecer contraseña' no se encontró o no está visible."

    reset_password_link.click()

    email_field_reset = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputSizeSmall.css-1o6z5ng"))
    )

    assert email_field_reset.is_displayed(), "El campo de entrada para restablecer la contraseña no está visible."

    driver.save_screenshot("screenshots/reset_password_form_displayed.png")

#  5-Prueba automatizada de la presencia de un logo
    def test_logo_presence(driver):
        driver.get("https://aceenlinea.com/login")  
        time.sleep(5) 

    logo_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, "img[src='/static/media/ace-logo-blue.d933257547751a06c2e1.jpg']"))
    )

    assert logo_image.is_displayed(), "El logo no está visible en la página de login."

    driver.save_screenshot("screenshots/logo_present.png")