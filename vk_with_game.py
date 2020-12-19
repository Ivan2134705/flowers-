import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard  
key = "acaed12d0f40be3d4a52212a7704fe6418e8413ec3b471378f1aa528c08ecbf7712062027ec1657290113"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message, keyboard = None):  
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,
                           'keyboard':keyboard.get_keyboard() if keyboard else None,}  
                          )

start_keyboard = VkKeyboard(one_time = True)  
start_keyboard.add_button('START')
start_keyboard.add_line()
start_keyboard.add_button('NOT START')

main_keyboard = VkKeyboard(one_time = True)  
main_keyboard.add_button('Об авторе')
main_keyboard.add_button('Сделать пожертвование')
main_keyboard.add_line()
main_keyboard.add_button('Сыграть в игру')

main_keyboard.add_button('узнать погоду')

back_keyboard = VkKeyboard(one_time = True)
back_keyboard.add_button('Назад')


game_over_keyboard = VkKeyboard(one_time = True)    #<1=====
game_over_keyboard.add_button('Выйти')
game_over_keyboard.add_line()
game_over_keyboard.add_button('Продолжить(просто введи число)')

drugaya_klava  = VkKeyboard(one_time = True) 
drugaya_klava.add_button('Выйти')
drugaya_klava.add_line()
drugaya_klava.add_button('купить шавуху афтору')
drugaya_klava  = VkKeyboard(one_time = True) 
drugaya_klava.add_button('Выйти')
drugaya_klava.add_line()
drugaya_klava.add_button('Помолиться')


gamers={}
# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            print(text)
            if user_id in gamers:
                try:
                    otvet = int(text)
                except:
                    if text == 'выйти':
                        del gamers[user_id]
                        send_message(user_id,"ну ладно :с",main_keyboard)    #<1=====
                    else:
                        send_message(user_id,"те чо игра надоела?",game_over_keyboard)
                    
                    continue
                if otvet > gamers[user_id]:
                    send_message(user_id,"mnoga")
                elif otvet < gamers[user_id]:
                    send_message(user_id,"malo")
                else:
                    send_message(user_id,"Победил", main_keyboard)
                    del gamers[user_id]
            else:
                if text == 'START'.lower():   
                    send_message(user_id,"Добро пожаловать",main_keyboard)  
                    
                elif text == 'Об авторе'.lower():   
                    send_message(user_id,"Damir",back_keyboard)
                elif text == 'Сделать пожертвование'.lower():   
                    send_message(user_id,"выбери",drugaya_klava)
                elif text == 'Сыграть в игру'.lower():
                    from random import randint
                    gamers[user_id] = randint(1,9000)
                    send_message(user_id,"угадывай")
                elif text == 'узнать погоду'.lower():   
                    send_message(user_id,"ясно",back_keyboard)
                    #купить шавуху афтору
                elif text == 'купить шавуху афтору'.lower():   
                    send_message(user_id,"купи",main_keyboard)
                else:
                    send_message(user_id,"Продолжайте",main_keyboard)
