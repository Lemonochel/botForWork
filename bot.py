import pyautogui
import time
from pywinauto.keyboard import send_keys

#----пути к картинкам для анализа изображений
path_label_number = r'D:\bot_work\label_number.PNG'
path_label_whatsapp = r'D:\bot_work\label_whatsapp.PNG'
path_label_email = r'D:\bot_work\label_email.PNG'
path_label_msg_email = r'D:\bot_work\label_sms_email1.PNG'
path_button_send = r'D:\bot_work\button_send.PNG'
path_label_topic_email = r'D:\bot_work\label_topic_email.PNG'
path_button_email = r'D:\bot_work\button_email.PNG'
path_button_task = r'D:\bot_work\button_task.PNG'
path_label_connection = r'D:\bot_work\label_connection.PNG'


client_name = ''
tariff_end_date = ''
selection_of_scenarios = ''

#----текста для отправки клиентам
def first_sms():
    send_keys(client_name + ''',{VK_SPACE}добрый{VK_SPACE}день!{ENTER} 
Меня{VK_SPACE}зовут{VK_SPACE},{VK_SPACE}компания{VK_SPACE}-{VK_SPACE},{VK_SPACE}сервис{VK_SPACE}по{VK_SPACE}интеграции{VK_SPACE}Instagram,{VK_SPACE}WhatsApp{VK_SPACE}и{VK_SPACE}CRM.{ENTER}
Вы{VK_SPACE}недавно{VK_SPACE}зарегистрировали{VK_SPACE}тестовый{VK_SPACE}кабинет,{VK_SPACE}на{VK_SPACE}нашем{VK_SPACE}сервисе.{ENTER}
Хочу{VK_SPACE}узнать,{VK_SPACE}как{VK_SPACE}у{VK_SPACE}Вас{VK_SPACE}проходит{VK_SPACE}тестирование?{ENTER}
Нужна{VK_SPACE}ли{VK_SPACE}Вам{VK_SPACE}помощь{VK_SPACE}с{VK_SPACE}настройкой{VK_SPACE}нашего{VK_SPACE}сервиса,{VK_SPACE}для{VK_SPACE}общения{VK_SPACE}по{VK_SPACE}whatsapp{VK_SPACE}и{VK_SPACE}instagram?{ENTER}
Если{VK_SPACE}возникнут{VK_SPACE}вопросы{VK_SPACE}-{VK_SPACE}можете{VK_SPACE}обращаться{VK_SPACE}в{VK_SPACE}этот{VK_SPACE}чат.{ENTER}
{ENTER}
--
{ENTER}
С{VK_SPACE}уважением,{VK_SPACE}{VK_SPACE}{ENTER}
Менеджер{VK_SPACE}по{VK_SPACE}работе{VK_SPACE}с{VK_SPACE}клиентами{VK_SPACE}–{VK_SPACE}{ENTER}
Телефон{VK_SPACE}{+}7{VK_SPACE}{VK_SPACE}{VK_SPACE}|{VK_SPACE}Сайт:{VK_SPACE}''', pause = 0)

def the_and_sms():
    send_keys(client_name + ''',{VK_SPACE}добрый{VK_SPACE}день!{ENTER}На{VK_SPACE}связи{VK_SPACE}команда{VK_SPACE}I2CRM.{VK_SPACE}Ваш{VK_SPACE}менеджер{VK_SPACE}.{ENTER}
Хотели{VK_SPACE}уточнить,{VK_SPACE}удалось{VK_SPACE}ли{VK_SPACE}воспользоваться{VK_SPACE}бесплатным{VK_SPACE}тестовым{VK_SPACE}доступом{VK_SPACE}от{VK_SPACE}нашего{VK_SPACE}сервиса?{ENTER}
Планируете{VK_SPACE}продолжить{VK_SPACE}им{VK_SPACE}пользоваться{VK_SPACE}на{VK_SPACE}платной{VK_SPACE}подписке?{ENTER}
Оплатить{VK_SPACE}можно{VK_SPACE}2-мя{VK_SPACE}способами:{ENTER}
С{VK_SPACE}карты{VK_SPACE}в{VK_SPACE}личном{VK_SPACE}кабинете:{VK_SPACE}перейдите{VK_SPACE}по{VK_SPACE}ссылке{VK_SPACE}-{VK_SPACE}{ENTER}
Или{VK_SPACE}прислать{VK_SPACE}мне{VK_SPACE}Ваши{VK_SPACE}реквизиты{VK_SPACE}для{VK_SPACE}оплаты{VK_SPACE}:{)}{ENTER}
{ENTER}
Плюс,{VK_SPACE}если{VK_SPACE}будете{VK_SPACE}подключать{VK_SPACE}сервис{VK_SPACE}на{VK_SPACE}длительный{VK_SPACE}срок{VK_SPACE}-{VK_SPACE}у{VK_SPACE}вас{VK_SPACE}будут{VK_SPACE}очень{VK_SPACE}хорошие{VK_SPACE}скидки!{ENTER}
По{VK_SPACE}поводу{VK_SPACE}всех{VK_SPACE}возникающих{VK_SPACE}вопросов{VK_SPACE}Вы{VK_SPACE}можете{VK_SPACE}написать{VK_SPACE}сюда.{ENTER}
Хорошего{VK_SPACE}дня!{ENTER}
{ENTER}
--
{ENTER}
С{VK_SPACE}уважением,{VK_SPACE}{ENTER}
Менеджер{VK_SPACE}по{VK_SPACE}работе{VK_SPACE}с{VK_SPACE}клиентами{VK_SPACE}–{VK_SPACE}{ENTER}
Телефон{VK_SPACE}{+}{VK_SPACE}|{VK_SPACE}Сайт:{VK_SPACE}''', pause = 0)

def reference_information():
    send_keys(client_name + ''',{VK_SPACE}добрый{VK_SPACE}день!{VK_SPACE}Это{VK_SPACE}ваш{VK_SPACE}менеджер{VK_SPACE}{ENTER}
В{VK_SPACE}сообщении{VK_SPACE}высылаю{VK_SPACE}вам{VK_SPACE}ссылку{VK_SPACE}на{VK_SPACE}наш{VK_SPACE}справочный{VK_SPACE}материал{VK_SPACE}https://help.i2crm.ru/hc/ru{VK_SPACE}для{VK_SPACE}ознакомления.{ENTER}
Также{VK_SPACE}если{VK_SPACE}у{VK_SPACE}вас{VK_SPACE}есть{VK_SPACE}вопросы{VK_SPACE}или{VK_SPACE}проблемы{VK_SPACE}-{VK_SPACE}вы{VK_SPACE}можете{VK_SPACE}писать{VK_SPACE}их{VK_SPACE}в{VK_SPACE}этот{VK_SPACE}чат,{VK_SPACE}или{VK_SPACE}позвонить{VK_SPACE}нам{VK_SPACE}на{VK_SPACE}горячую{VK_SPACE}линию.{ENTER}
Мы{VK_SPACE}всегда{VK_SPACE}рады{VK_SPACE}вам{VK_SPACE}помочь!{ENTER}
VK_SPACE}на{VK_SPACE}наш{VK_SPACE}ютуб{VK_SPACE}канал{VK_SPACE}c{VK_SPACE}видео{VK_SPACE}инструкциями{ENTER} 
Хорошего{VK_SPACE}дня!{ENTER}
{ENTER}
--
{ENTER}
С{VK_SPACE}уважением,{VK_SPACE}{ENTER}
Менеджер{VK_SPACE}по{VK_SPACE}работе{VK_SPACE}с{VK_SPACE}клиентами{VK_SPACE}–{VK_SPACE}i2CRM{ENTER}
Телефон{VK_SPACE}''', pause = 0)

def msg_prolongation():
    send_keys(client_name +''',{VK_SPACE}добрый{VK_SPACE}день!{VK_SPACE}Меня{VK_SPACE}зовут{VK_SPACE},{VK_SPACE}компания{VK_SPACE}-{VK_SPACE}I2CRM,{VK_SPACE}сервис{VK_SPACE}по{VK_SPACE}интеграции{VK_SPACE}Instagram,{VK_SPACE}WhatsApp{VK_SPACE}в{VK_SPACE}CRM.{ENTER} 
Напоминаю,{VK_SPACE}что{VK_SPACE}''' + tariff_end_date + '''{VK_SPACE}оплаченный{VK_SPACE}период{VK_SPACE}использования{VK_SPACE}нашего{VK_SPACE}сервиса{VK_SPACE}заканчивается.{ENTER}
Сообщения{VK_SPACE}по{VK_SPACE}Instagram/WhatsApp{VK_SPACE}не{VK_SPACE}будут{VK_SPACE}попадать{VK_SPACE}в{VK_SPACE}Вашу{VK_SPACE}CRM.{ENTER}
Для{VK_SPACE}дальнейшей{VK_SPACE}работы{VK_SPACE}с{VK_SPACE}нашим{VK_SPACE}сервисом{VK_SPACE}Вам{VK_SPACE}нужно{VK_SPACE}оплатить{VK_SPACE}подписку.{ENTER}
Для{VK_SPACE}наиболее{VK_SPACE}выгодной{VK_SPACE}оплаты{VK_SPACE}мы{VK_SPACE}готовы{VK_SPACE}предложить{VK_SPACE}Вам{VK_SPACE}промо-код{VK_SPACE}на{VK_SPACE}оплату{VK_SPACE}нашего{VK_SPACE}сервиса.{ENTER}
Промо-код{VK_SPACE}дает{VK_SPACE}бонусные{VK_SPACE}дни{VK_SPACE}-{VK_SPACE}до{VK_SPACE}108{VK_SPACE}дней{VK_SPACE}бесплатного{VK_SPACE}использования{VK_SPACE}сервиса{VK_SPACE}{(}при{VK_SPACE}оплате{VK_SPACE}на{VK_SPACE}год{)}.{ENTER}
Промо-код{VK_SPACE}действует{VK_SPACE}при{VK_SPACE}оплате{VK_SPACE}от{VK_SPACE}3-х{VK_SPACE}месяцев.{ENTER} 
Если{VK_SPACE}готовы{VK_SPACE}воспользоваться{VK_SPACE}нашим{VK_SPACE}предложением,{VK_SPACE}то{VK_SPACE}прошу{VK_SPACE}дать{VK_SPACE}ответ{VK_SPACE}в{VK_SPACE}этой{VK_SPACE}переписке{)}{ENTER}
Хорошего{VK_SPACE}Вам{VK_SPACE}дня!{ENTER}
{ENTER}
--
{ENTER}
С{VK_SPACE}уважением,{VK_SPACE}{ENTER}
Менеджер{VK_SPACE}по{VK_SPACE}работе{VK_SPACE}с{VK_SPACE}клиентами{VK_SPACE}–{VK_SPACE}{ENTER}
Телефон{VK_SPACE}''', pause = 0)





#функция находит номер телефона, клиекает по нему и нажимает кнопку отправки сообщения в вотсапе
def send_msg_whatsapp():    
    label_number = pyautogui.locateOnScreen(path_label_number, confidence = 0.7)
    pyautogui.moveTo(label_number)
    pyautogui.move(190, 0)
    pyautogui.click()
    time.sleep(1)
    label_whatsapp = pyautogui.locateOnScreen(path_label_whatsapp, confidence = 0.7)
    button_whatsapp = label_whatsapp
    pyautogui.click(button_whatsapp)

#функция находит имейл, клиекает по нему и нажимает кнопку отправки почты из срм системы
def send_msg_email():
    label_email = pyautogui.locateOnScreen(path_label_email, confidence = 0.8)
    pyautogui.moveTo(label_email)
    pyautogui.move(190, 0)
    pyautogui.click()
    time.sleep(1)
    send_email = pyautogui.locateOnScreen(path_label_msg_email, confidence = 0.8)
    button_email = send_email
    pyautogui.click(button_email)
    label_topic_email = pyautogui.locateOnScreen(path_label_topic_email, confidence = 0.8)
    pyautogui.moveTo(label_topic_email)
    pyautogui.move(50, 0)
    pyautogui.click()
    send_keys('I2CRM', pause = 0)
    pyautogui.move(0, 190)
    pyautogui.click()

#функция нажатия кнопки отправить
def press_button_send():          
    button_send = pyautogui.locateOnScreen(path_button_send, confidence = 0.7)
    time.sleep(1)
    pyautogui.click(button_send)
   

#функция логики полного цикла отправки письма клиенту при первом касании
def first_scenario():
    global client_name
    client_name = str(input('Введите имя клиента:'))
    choice = str(input('Отправить сообщение?[y/n]'))
    if choice == 'y' or choice == 'да' or choice == 'д':
        time.sleep(3)
        send_msg_whatsapp()
        time.sleep(1)
        first_sms()
        time.sleep(1)
        press_button_send()
        time.sleep(5)
        send_msg_email()
        time.sleep(1)
        first_sms()
        time.sleep(2)
        press_button_send()
        time.sleep(1)
        formulation_task()
    else:
        selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))

#функция логики полного цикла отправки письма клиенту при уходе с тестового доступа
def second_scenario():
    global client_name
    client_name = str(input('Введите имя клиента:'))
    choice = str(input('Отправить сообщение?[y/n]'))
    if choice == 'y' or choice == 'да' or choice == 'д':
        time.sleep(3)
        send_msg_whatsapp()
        time.sleep(1)
        the_and_sms()
        time.sleep(1)
        press_button_send()
        time.sleep(5)
        send_msg_email()
        time.sleep(1)
        the_and_sms()
        time.sleep(3)
        press_button_send()
        time.sleep(1)
        formulation_task()
    else:
        selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))

#функция выбора сценариев действий бота
def event_selection():       
    global selection_of_scenarios
    selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))
    while True:       
        if selection_of_scenarios == 1:           
            first_scenario()
            selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))
        elif selection_of_scenarios == 2:
            second_scenario()
            selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))
        elif selection_of_scenarios == 3:
            third_scenario()
            selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))
        elif selection_of_scenarios == 4:
            fourth_scenario()
            selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))
        else:
            selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))

#функция отправки сообщения о продлении тарифа
def fourth_scenario():
    global client_name
    global tariff_end_date
    tariff_end_date = (input('Введите дату окончания тарифа:'))
    client_name = str(input('Введите имя клиента:'))
    choice = str(input('Отправить сообщение?[y/n]'))
    if choice == 'y' or choice == 'да' or choice == 'д':
        time.sleep(3)
        send_msg_whatsapp()
        time.sleep(1)
        msg_prolongation()
        time.sleep(1)
        press_button_send()
        time.sleep(5)
        send_msg_email()
        time.sleep(1)
        msg_prolongation()
        time.sleep(3)
        press_button_send()
        time.sleep(1)
    else:
        selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))

#функция постановки задачи
def formulation_task():
    choice = str(input('Какую задачу поставить?[1/2]'))
    if choice == '1':
        time.sleep(1)
        button_email = pyautogui.locateOnScreen(path_button_email, confidence = 0.8)
        time.sleep(1)
        pyautogui.moveTo(button_email)
        pyautogui.click()
        time.sleep(1)
        button_task = pyautogui.locateOnScreen(path_button_task, confidence = 0.8)        
        time.sleep(1)
        pyautogui.moveTo(button_task)
        pyautogui.click()
        time.sleep(1)
        label_connection = pyautogui.locateOnScreen(path_label_connection, confidence = 0.8)
        pyautogui.moveTo(label_connection)
        pyautogui.move(70, 0)
        send_keys('недозвон,{VK_SPACE}отправил{VK_SPACE}смс', pause = 0)
    elif choice == '2':
        time.sleep(1)
        button_email = pyautogui.locateOnScreen(path_button_email, confidence = 0.8)
        time.sleep(1)
        pyautogui.moveTo(button_email)
        pyautogui.click()
        time.sleep(1)
        button_task = pyautogui.locateOnScreen(path_button_task, confidence = 0.8)        
        time.sleep(1)
        pyautogui.moveTo(button_task)
        pyautogui.click()
        time.sleep(1)
        label_connection = pyautogui.locateOnScreen(path_label_connection, confidence = 0.8)
        pyautogui.moveTo(label_connection)
        pyautogui.move(70, 0)
        send_keys('недозвон,{VK_SPACE}отправил{VK_SPACE}смс,{VK_SPACE}ушли{VK_SPACE}с{VK_SPACE}теста', pause = 0)
    else:
        selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))





#функция отправки сообщения справочной информации
def third_scenario():
    global client_name
    client_name = str(input('Введите имя клиента:'))
    choice = str(input('Отправить сообщение?[y/n]'))
    if choice == 'y' or choice == 'да' or choice == 'д':
        time.sleep(3)
        send_msg_whatsapp()
        time.sleep(1)
        reference_information()
        time.sleep(1)
        press_button_send()
        time.sleep(1)        
    else:
        selection_of_scenarios = int(input('''Выберите сценарий: Первое смс[1]; Ушли с теста[2]; Отправить справку[3]; Продление[4]:'''))

#функция петли приложения для отказоустойчивости
def loop():
    while True:
        try:
            event_selection()
        except:
            continue


loop()

#функция без петли для поиска ошибок
#event_selection()          
    
