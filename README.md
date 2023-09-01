# Rostelekom_authorisation_interface
Итоговый проект по автоматизации тестирования

В рамках выполнения дипломного проекта необходимо протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии. 

→ [Требования по проекту (.doc)](https://docs.google.com/document/d/1Dj5SPqbdxAhikzC1mW5WBj78GOk2aorq/edit?usp=sharing&ouid=108321920590172667184&rtpof=true&sd=true)

→ Объект тестирования: https://b2c.passport.rt.ru



Заказчик передал вам следующее задание:

1. Протестировать требования.
2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
4. Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)



Ожидаемый результат

1. Перечислены инструменты, которые применялись для тестирования.

   * Почему именно этот инструмент и эту технику.
   * Что им проверялось.
   * Что именно в нем сделано.
   
2. К выполненному заданию прикреплены:

   * Набор тест-кейсов;
   * Набор автотестов на GitHub. Обратите внимание, что в репозитории должен находиться файл README.md, где будет описано, что именно проверяют данные тестовые сценарии и какие команды необходимо выполнить для запуска тестов. Описанные команды должны работать на любом компьютере с установленными Python3 и PyTest;
   * Описание оформленных дефектов.
  

**В корневом каталоге проекта содержатся:**
* [README.md](https://github.com/vladimT/Rostelekom_authorisation_interface/blob/master/README.md) - содержит информацию в целом о проекте;
* [requirements.txt](https://github.com/vladimT/Rostelekom_authorisation_interface/blob/master/requirements.txt) - содержит все библиотеки проекта.
* [pytest.ini](https://github.com/vladimT/Rostelekom_authorisation_interface/blob/master/pytest.ini) - содержит маркировку автотестов.
* [setting.py](https://github.com/vladimT/Rostelekom_authorisation_interface/blob/master/settings.py) - настройки/переменные учетных данных.
* [.env](https://github.com/vladimT/Rostelekom_authorisation_interface/blob/master/.env) - учетные данные.
* [chromedriver.exe](https://github.com/vladimT/Rostelekom_authorisation_interface/blob/master/chromedriver.exe) - драйвер для управления браузером Chrome.

***
**Директория tests содержит:**
* [test_auth_interface.py](https://github.com/vladimT/Rostelekom_authorisation_interface/blob/master/tests/test_auth_interface.py) - файл автотестов;
* [conftest.py](https://github.com/vladimT/Rostelekom_authorisation_interface/blob/master/tests/conftest.py) - условия для выполнения тестовых задач.
***
→ [Тест-кейсы, баги (.excel)](https://docs.google.com/document/d/1t_J-Egd7ABMViIbvhhZAqJXhzZJ5CnqA/edit?usp=sharing&ouid=108321920590172667184&rtpof=true&sd=true) - приведены тест-кейсы и баги.  

### При разработке тест-кейсов были применены следующие техники тест-дизайна: 
 
* эквивалентное разбиение
* анализ граничных значений
* предугадывание ошибки


### Инструменты, которые применялись для тестирования.

* Для тестирования сайта был использован 
интсрумент [Selenium](https://www.selenium.dev/);
* Для определения локаторов использовались 
следующие инструменты: DevTools, [ChroPath](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo). 

### Запуск тестов:
* установить все библиотеки и зависимости: `pip install -r requirements.txt`;
* загрузить [Selenium WebDriver](https://chromedriver.chromium.org/downloads) (выбрав версию, совместимую с вашим браузером).
