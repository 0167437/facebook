import os
import pyautogui
import time
import io
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import BD
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
import random




# Connected
opts = Options()
opts.add_argument("User-Agent=Mozilla/5.0")
driver = webdriver.Chrome(options = opts)
# wait = WebDriverWait(driver, 20)
driver.get("https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F")



# Copy - Paste the elements
tell = str('+380669303253')
password = str('1402200111')
time.sleep(3)



facebooc = ['https://www.facebook.com/groups/6555603937866634/', 'https://www.facebook.com/groups/1221102742146899/', 'https://www.facebook.com/groups/selydove.city/', 'https://www.facebook.com/groups/904626769747692/',
             '#@kram_slav_chat', '#@pokrovsk_sale', '#@dobropolie2023', '#@bazarkrhw', '#@fishka1787', '#@kypiprodaidonbass',
             '#@baraxolkadobropillya', '#@tovarka_go', '#@ludild']
massenge_tg = str("""
        Привет! Меня зовут Виталина, и я сертифицированный мастер маникюра. Приглашаю вас на процедуры,которые подарят вашим ручкам и ножкам нежность и красоту.Работаю только качественным и стерильным инструментом. \nЯ предлагаю: \n• Маникюр (Коррекция гелем/Полигелем) \n• Наращивание ногтей \n• Дизайны на любой вкус \n• Педикюр \n• Обработку стоп \nМой INSTAGRAM: beauty_zona.dobropillya \n📲Запись в личные сообщения или по номеру телефона 380667365346.\nАдрес:ул. Банковая, 28, г. Доброполье. \nБуду рада видеть вас!""")
time.sleep(4)
# Search start body and click
# driver.find_element(By.XPATH, "//*[@id=\"auth-pages\"]/div/div[2]/div[3]/div/div[2]/button[2]/div").click()D




conteinerStart = driver.find_element(by = By.XPATH, value = '//*[@id="email_container"]')
conteinerStart.click()
pyautogui.write(tell, interval=0.15)

conteinerStart = driver.find_element(by = By.XPATH, value = '//*[@id="loginform"]/div[2]')
conteinerStart.click()
pyautogui.write(password, interval=0.15)

driver.find_element(by = By.CLASS_NAME, value = '_xkt').click()
time.sleep(15)


name = None

# Выбор файла, для пиара онлайн или офлайн групп
with open("D:/LeViNailSTUDIO/academy-py/txt/ProccesingParsForFaceBook.txt", "r", encoding="utf-8") as FileOnOrOff:
    for PrintOnOff in FileOnOrOff:
        print(PrintOnOff)
    FileOnOrOff.close

times = random.randint(17, 25)
time.sleep(times)

proccesing = int(input("Виберіть будь-ласко один з варіантів: "))
file_proccesing = str(None)
# В файле БД подклюает список ссылок групп Донецкой области, если пользователь нажмет на 1
if proccesing == 1:
    name = BD.facebooc
# В файле БД подключается к списку всех групп по Украине, если пользователь нажмет на 2
elif proccesing == 2:
    name = BD.facebook_offline
else:
    print("Оберіть будьласко один із наступних варіантів")

time.sleep(2)

# Главный цикл
# Тут передается знаачение со списка файла БД, в переменную Имя
for file in name:

    # Подключение БД, к программе. А так-переход по ссылке с БД
    driver.get(file)
    time.sleep(3)
    # Перезагрузка страницы
    times = random.randint(17, 50)
    time.sleep(times)
    driver.refresh()

    # work piar
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 250);")
    time.sleep(2)
    # print("Сейчая я ввойду в чат группы ", group)
    try:
        # Входит в чат
        times = random.randint(6, 25)
        time.sleep(times)

        driver.find_element(by = By.XPATH, value = '//*[@class=\'xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe\']').click()
    except NoSuchElementException:
        continue
    except ElementNotInteractableException:
        continue
    except ElementClickInterceptedException:
        continue









    time.sleep(4)
    # pyautogui.write('222', interval=0.15)
    try:
        times = random.randint(4, 25)
        time.sleep(times)
        # Нажимает на Анонимне сообщение
        driver.find_element(by = By.XPATH, value = '//*[@class=\'x1i10hfl x9f619 xggy1nq x1s07b3s x1ypdohk x5yr21d x17qophe xdj266r x11i5rnm xat24cr x1mh8g0r x1w3u9th x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd x10l6tqk x13vifvy xh8yej3\']').click()
        # Нажимает Понятно
        times = random.randint(10, 30)
        time.sleep(times)
        driver.find_element(by = By.XPATH, value = '//*[contains(@class, \'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft\') and text()=\'Понятно\']').click()
        # x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67
        time.sleep(2)
    except NoSuchElementException:
        continue
    except ElementNotInteractableException:
        continue
    except ElementClickInterceptedException:
        continue
    try:
        times = random.randint(9, 17)
        time.sleep(times)
        driver.find_elements(by = By.XPATH, value = '//*[@class=\'x6s0dn4 x78zum5 xl56j7k x1n2onr6 x5yr21d xh8yej3\']')[1].click()
        time.sleep(3 )
        pyautogui.write('A.jpg', interval=0.35)
        pyautogui.press('enter')
        # os.path.split(driver.send_keys("D:\LeViNailSTUDIO\src")[0])
        # os.path.split("D:\LeViNailSTUDIO\src")[0]
        # Отправка пути к файлу
        # img = driver.find_element(by = By.XPATH, value = '//*[@class=\'_1mf _1mj\']')
        # img.send_keys(os.path.abspath("D:\LeViNailSTUDIO\src\12572952_SL-091319-23370-27.jpg"))
        times = random.randint(4, 12)
        time.sleep(times)
        driver.find_element(by = By.XPATH, value = '//*[@class=\'_1mf _1mj\']').send_keys(BD.massange_facebook)
        times = random.randint(8, 50)
        time.sleep(times)
        driver.find_element(by = By.XPATH, value='//*[contains(@class, \'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft\') and text()=\'Отправить\']').click()
        times = random.randint(10, 60)
        time.sleep(times)
    except NoSuchElementException:
        continue
    except ElementNotInteractableException:
        continue
    except ElementClickInterceptedException:
        continue
    time.sleep(3)




time.sleep(10)


# QUIT WINDOW DRIVER
driver.quit()











