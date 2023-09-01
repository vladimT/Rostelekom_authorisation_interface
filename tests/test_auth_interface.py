from selenium.webdriver.common.by import By
from settings import valid_phone, valid_email, valid_password, valid_login
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.auth
def test_auth_form_open(driver):
    '''Тест 01. Проверим, что открывается страница с формой "Авторизация"'''

    driver.get('https://b2c.passport.rt.ru')

    auth_title = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-container__title'))).text
    assert auth_title == "Авторизация"

@pytest.mark.auth
def test_phone_form(driver):
    '''Тест 02. Проверим, что при загрузке страницы авторизации по-умолчнию отображается ввод по мобильному телефону'''
    driver.get('https://b2c.passport.rt.ru')

    phone_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
    assert phone_field == "Мобильный телефон"

@pytest.mark.auth_phone
def test_auth_phone_valid(driver):
    '''Тест 03. Проверим авторизацию с валидными данными номера телефона и пароля'''
    driver.get('https://b2c.passport.rt.ru')
    phone_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-phone')))
    phone_field = driver.find_element(By.CSS_SELECTOR, '.rt-input__placeholder')
    actions = ActionChains(driver)
    actions.move_to_element(phone_button).click(phone_field).perform()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    correct_login = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Тюркин\nВладимир Андреевич'))
    assert driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == "Тюркин"
    assert driver.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text == "Владимир Андреевич"
    logout = driver.find_element(By.CSS_SELECTOR, '#logout-btn')
    actions.click(logout).perform()

@pytest.mark.auth_mail
def test_auth_email_valid(driver):
    '''Тест 04. Проверим авторизацию с валидными данными электронной почты и пароля'''
    driver.get('https://b2c.passport.rt.ru')
    email_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-mail')))
    email_field = driver.find_element(By.CSS_SELECTOR, '.rt-input__placeholder')
    actions = ActionChains(driver)
    actions.move_to_element(email_button).click(email_field).perform()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    correct_login = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Тюркин\nВладимир Андреевич'))
    assert driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == "Тюркин"
    assert driver.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text == "Владимир Андреевич"
    logout = driver.find_element(By.CSS_SELECTOR, '#logout-btn')
    actions.click(logout).perform()

@pytest.mark.auth_login
def test_auth_login_valid(driver):
    '''Тест 05. Проверим авторизацию с валидными данными логина и пароля'''
    driver.get('https://b2c.passport.rt.ru')
    login_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-login')))
    login_field = driver.find_element(By.CSS_SELECTOR, '.rt-input__placeholder')
    actions = ActionChains(driver)
    actions.move_to_element(login_button).click(login_field).perform()
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    correct_login = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Тюркин\nВладимир Андреевич'))
    assert driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == "Тюркин"
    assert driver.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text == "Владимир Андреевич"
    logout = driver.find_element(By.CSS_SELECTOR, '#logout-btn')
    actions.click(logout).perform()

@pytest.mark.auth_email
@pytest.mark.auth_phone
def test_from_phone_to_email(driver):
    '''Тест 06. Проверим смену табов (телефона на почту) при вводе электронной почты в поле ввода мобильного телефона'''
    driver.get('https://b2c.passport.rt.ru')
    phone_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-phone')))
    phone_field = driver.find_element(By.CSS_SELECTOR, '.rt-input__placeholder')
    actions = ActionChains(driver)
    actions.move_to_element(phone_button).click(phone_field).perform()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'password').click()
    phone_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="EMAIL"]')))
    assert driver.find_element(By.XPATH, '//input[@value="EMAIL"]') == phone_button

@pytest.mark.auth_email
@pytest.mark.auth_phone
def test_from_email_to_phone(driver):
    '''Тест 07. Проверим смену табов (почты на телефон) при вводе мобильного телефона в поле ввода электронной почты'''
    driver.get('https://b2c.passport.rt.ru')
    email_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-mail')))
    email_field = driver.find_element(By.CSS_SELECTOR, '.rt-input__placeholder')
    actions = ActionChains(driver)
    actions.move_to_element(email_button).click(email_field).perform()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').click()
    email_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="PHONE"]')))
    assert driver.find_element(By.XPATH, '//input[@value="PHONE"]') == email_button

@pytest.mark.auth_login
@pytest.mark.auth_phone
def test_from_phone_to_login(driver):
    '''Тест 08. Проверим смену табов (телефона на логин) при вводе логина в поле ввода мобильного телефона'''
    driver.get('https://b2c.passport.rt.ru')
    phone_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-phone')))
    phone_field = driver.find_element(By.CSS_SELECTOR, '.rt-input__placeholder')
    actions = ActionChains(driver)
    actions.move_to_element(phone_button).click(phone_field).perform()
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    driver.find_element(By.ID, 'password').click()
    phone_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="LOGIN"]')))
    assert driver.find_element(By.XPATH, '//input[@value="LOGIN"]') == phone_button



@pytest.mark.auth_login
@pytest.mark.auth_phone
def test_from_login_to_phone(driver):
    '''Тест 09. Проверим смену табов (логина на телефон) при вводе номера мобильного телефона в поле ввода логина'''
    driver.get('https://b2c.passport.rt.ru')
    login_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-login')))
    login_field = driver.find_element(By.CSS_SELECTOR, '.rt-input__placeholder')
    actions = ActionChains(driver)
    actions.move_to_element(login_button).click(login_field).perform()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').click()
    login_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="PHONE"]')))
    assert driver.find_element(By.XPATH, '//input[@value="PHONE"]') == login_button

@pytest.mark.auth_login
@pytest.mark.auth_email
def test_from_login_to_email(driver):
    '''Тест 10. Проверим смену табов (логина на почту) при вводе электронной почты в поле ввода логина'''
    driver.get('https://b2c.passport.rt.ru')
    login_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-login')))
    login_field = driver.find_element(By.CSS_SELECTOR, '.rt-input__placeholder')
    actions = ActionChains(driver)
    actions.move_to_element(login_button).click(login_field).perform()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'password').click()
    login_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="EMAIL"]')))
    assert driver.find_element(By.XPATH, '//input[@value="EMAIL"]') == login_button

@pytest.mark.auth_login
@pytest.mark.auth_email
def test_from_login_to_email(driver):
    '''Тест 11. Проверим смену табов (почты на логин) при вводе логина в поле ввода электронной почты'''
    driver.get('https://b2c.passport.rt.ru')
    email_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-mail')))
    email_field = driver.find_element(By.CSS_SELECTOR, '.rt-input__placeholder')
    actions = ActionChains(driver)
    actions.move_to_element(email_button).click(email_field).perform()
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    driver.find_element(By.ID, 'password').click()
    email_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="LOGIN"]')))
    assert driver.find_element(By.XPATH, '//input[@value="LOGIN"]') == email_button

@pytest.mark.reg
def test_sign_up(driver):
    '''Тест 12. Проверим открытие страницы с формой регистрации'''
    driver.get('https://b2c.passport.rt.ru')
    reg_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="kc-register"]')))
    actions = ActionChains(driver)
    actions.click(reg_button).perform()
    title = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(),"Регистрация")]')))
    assert title.text == "Регистрация"

@pytest.mark.auth_login
def test_tabs_auth(driver):
    '''Тест 13. Проверим, что на странице авторизации отображается меню выбора аутентификации, состоящее из: "Телефон", "Почта", "Логин", "Лицевой счёт"'''
    driver.get('https://b2c.passport.rt.ru')
    tabs = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.rt-tabs--small.tabs-input-container__tabs')))
    list_of_tabs = "Телефон\nПочта\nЛогин\nЛицевой счёт"
    for i in range(len(tabs)):
        assert tabs[i].text == list_of_tabs

@pytest.mark.reg
def test_reg_valid(driver):
    '''Тест 14. Проверим появление сообщения об отправки email для подтверждения почты после успешного заполнения формы регистрации валидными данными при использовании электронного адреса'''
    driver.get('https://b2c.passport.rt.ru')
    reg_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="kc-register"]')))
    actions = ActionChains(driver)
    actions.click(reg_button).perform()
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, 'firstName').send_keys('Иван')
    driver.find_element(By.NAME, 'lastName').send_keys('Иванов')
    driver.find_element(By.ID, 'address').send_keys('vladimirandreevichtyurkin@gmail.com')
    driver.find_element(By.ID, 'password').send_keys('dfrb-Swgfg-3-d')
    driver.find_element(By.ID, 'password-confirm').send_keys('dfrb-Swgfg-3-d')
    driver.find_element(By.NAME, 'register').click()
    registration = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-container__title'))).text
    success_registration = "Подтверждение email"
    assert registration == success_registration

@pytest.mark.reg
def test_reg_same_email(driver):
    '''Тест 15. Проверим появление сообщения об уже существующей учетной записи при указании ранее зарегистрированного email'''
    driver.get('https://b2c.passport.rt.ru')
    reg_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="kc-register"]')))
    actions = ActionChains(driver)
    actions.click(reg_button).perform()
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, 'firstName').send_keys('Иван')
    driver.find_element(By.NAME, 'lastName').send_keys('Иванов')
    driver.find_element(By.ID, 'address').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys('dfrb-Swgfg-3-d')
    driver.find_element(By.ID, 'password-confirm').send_keys('dfrb-Swgfg-3-d')
    driver.find_element(By.NAME, 'register').click()
    registration = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-modal__title'))).text
    acount_exist = "Учётная запись уже существует"
    assert registration == acount_exist

@pytest.mark.auth_login
def test_forgot_password_form(driver):
    '''Тест 16. Проверим, что на странице восстановления пароля отображается меню выбора аутентификации, состоящее из: "Телефон", "Почта", "Логин", "Лицевой счёт"'''
    driver.get('https://b2c.passport.rt.ru')
    forgot_pass_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located ((By.XPATH, "//a[@class='rt-link rt-link--orange rt-link--muted login-form__forgot-pwd login-form__forgot-pwd--muted']")))
    actions = ActionChains(driver)
    actions.click(forgot_pass_button).perform()
    tabs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.rt-tabs--small.tabs-input-container__tabs')))
    list_of_tabs = "Телефон\nПочта\nЛогин\nЛицевой счёт"
    for i in range(len(tabs)):
        assert tabs[i].text == list_of_tabs

@pytest.mark.reg
def test_reg_invalid_number(driver):
    '''Тест 17. Проверим регистрацию с невалидным номером мобильного телефона'''
    driver.get('https://b2c.passport.rt.ru')
    reg_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="kc-register"]')))
    actions = ActionChains(driver)
    actions.click(reg_button).perform()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'address').send_keys('123')
    driver.find_element(By.ID, 'password').click()
    error = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, './/span[contains(text(),"Введите телефон в формате +7ХХХХХХХХХХ или +375XXX")]'))).text
    assert error == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

@pytest.mark.reg
def test_reg_invalid_email(driver):
    '''Тест 18. Проверим регистрацию с невалидным email'''
    driver.get('https://b2c.passport.rt.ru')
    reg_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="kc-register"]')))
    actions = ActionChains(driver)
    actions.click(reg_button).perform()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'address').send_keys('упацvg@1ddf23.ys')
    driver.find_element(By.ID, 'password').click()
    error = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, './/span[contains(text(),"Введите телефон в формате +7ХХХХХХХХХХ или +375XXX")]'))).text
    assert error == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

@pytest.mark.reg
def test_reg_invalid_name_code(driver):
    '''Тест 19. Проверим появление сообщения об ошибке при невалидном заполнении имени с использованием латиницы'''
    driver.get('https://b2c.passport.rt.ru')
    reg_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="kc-register"]')))
    actions = ActionChains(driver)
    actions.click(reg_button).perform()
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, 'firstName').send_keys('Ivan')
    driver.find_element(By.NAME, 'lastName').click()
    error = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, './/span[contains(text(),"Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]'))).text
    assert error == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

@pytest.mark.reg
def test_reg_invalid_name_quant(driver):
    '''Тест 20. Проверим появление сообщения об ошибке при невалидном заполнении имени с использованием одного символа'''
    driver.get('https://b2c.passport.rt.ru')
    reg_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="kc-register"]')))
    actions = ActionChains(driver)
    actions.click(reg_button).perform()
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, 'firstName').send_keys('И')
    driver.find_element(By.NAME, 'lastName').click()
    error = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, './/span[contains(text(),"Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]'))).text
    assert error == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."































