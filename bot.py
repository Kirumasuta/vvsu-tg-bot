import telebot
import sqlite3
import psycopg2
import os
from flask import Flask, request
import logging
from telebot import types

# Database init
conn = psycopg2.connect(dbname='d39f0oqv4la9th', user='zmesqarmxotalw',
                        password='f4eb23bc9794f8c5726a727a09729197b41744262306362e56db2e76622ad5d3',
                        host='ec2-34-193-113-223.compute-1.amazonaws.com')
cursor = conn.cursor()

bot = telebot.TeleBot('5039345388:AAHMh3LdN-SbxmiGi-qSUUu_VQAVmAbjQho')
userType = ''
changeType = ''
user_Z = [
    'Игорь',
    '+8 (888) 888-88-88',
    'Владивосток',
    'Техника',
    'Проблема заключается в том, что у меня не работает морозилка, а почему я вообще хз ¯\_(ツ)_/¯'
]
search_ = ''
user_I = [
    'Игорь',
    '+8 (888) 888-88-88',
    'Владивосток',
    'Компьютеры и IT, Слесарь, Маляр',
    '3 года',
    'ОЧень скромный пацан :)'
]
input_ = [
    '',
    '',
    '',
    '',
    '',
    '',
    ''
]
input_len = 0
input_len_max = 0
I_list = [
    [
        'Игорь1',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ],
    [
        'Игорь2',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ],
    [
        'Игорь3',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ],
    [
        'Игорь4',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ],
    [
        'Игорь5',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ],
    [
        'Игорь6',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ],
    [
        'Игорь7',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ],
    [
        'Игорь8',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ],
    [
        'Игорь9',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ],
    [
        'Игорь10',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Компьютеры и IT, Слесарь, Маляр',
        '3 года',
        'ОЧень скромный пацан :)'
    ]
]
Z_list = [
    [
        'Игорь1',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Техника',
        'Проблема заключается в том, что у меня не работает морозилка, а почему я вообще хз ¯\_(ツ)_/¯'
    ],
    [
        'Игорь2',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Техника',
        'Проблема заключается в том, что у меня не работает морозилка, а почему я вообще хз ¯\_(ツ)_/¯'
    ],
    [
        'Игорь3',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Техника',
        'Проблема заключается в том, что у меня не работает морозилка, а почему я вообще хз ¯\_(ツ)_/¯'
    ],
    [
        'Игорь4',
        '+8 (888) 888-88-88',
        'Владивосток',
        'Техника',
        'Проблема заключается в том, что у меня не работает морозилка, а почему я вообще хз ¯\_(ツ)_/¯'
    ]
]
find_list = []


@bot.message_handler(commands=['start', 'старт'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    client = types.KeyboardButton('Заказчик')
    executor = types.KeyboardButton('Исполнитель')

    markup.add(client, executor)

    message = bot.send_message(
        message.chat.id,
        "Здравствуйте, вы собираетесь воспользоваться услугами {0.first_name}'а\nПожалуйста выберите Вашу роль: <b>Заказчик</b> или <b>Исполнитель</b>?\n\nПо возможности воспользуйтесь командой /info, для получения информации, как взаимодействовать с ботом"
            .format(bot.get_me()),
        parse_mode='html',
        reply_markup=markup
    )
    bot.register_next_step_handler(message, start_reply)


def start_reply(message):
    # anketa = False  # Пока в качестве переменной, потом заменим на проверку из базы данных, есть ли анкета у чела

    cursor.execute("SELECT * FROM public.users where id = '{0}';".format(message.from_user.id))
    anketa_user = cursor.fetchall()

    if len(anketa_user) == 1:
        if len(anketa_user[0]) > 1:
            print('есть запись в юзерах')
    else:
        cursor.execute("INSERT INTO public.users values({0})".format(message.from_user.id))
        cursor.execute("INSERT INTO public.isp values({0})".format(message.from_user.id))
        cursor.execute("INSERT INTO public.zak values({0})".format(message.from_user.id))
        conn.commit()

    cursor.execute("SELECT * FROM public.isp where uid = {0};".format(message.from_user.id))
    anketa_isp = cursor.fetchall()
    cursor.execute("SELECT * FROM public.zak where uid = {0};".format(message.from_user.id))
    anketa_zak = cursor.fetchall()

    global userType
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    create = types.KeyboardButton('Создать')
    change = types.KeyboardButton('Изменить')
    find = types.KeyboardButton('Поиск')

    if (message.text == 'Заказчик'):
        userType = message.text
        bot.send_message(
            message.chat.id,
            'Вы выбрали роль <b>Заказчика</b>',
            parse_mode='html'
        )
        if len([x for x in anketa_zak[0] if x is not None]) > 1:
            markup.add(create, change, find)

            message = bot.send_message(
                message.chat.id,
                'У вас уже есть созданная заявка, хотите изменить старую или сразу перейти к поиску <b>Исполнителей</b>?',
                parse_mode='html',
                reply_markup=markup
            )
            bot.register_next_step_handler(message, action_reply)
        else:
            markup.add(create, find)

            message = bot.send_message(
                message.chat.id,
                'У вас еще нет заявки, хотите её создать, или сразу перейти к поиску <b>Исполнителей</b>?',
                parse_mode='html',
                reply_markup=markup
            )
            bot.register_next_step_handler(message, action_reply)
    elif (message.text == 'Исполнитель'):
        userType = message.text
        bot.send_message(
            message.chat.id,
            'Вы выбрали роль <b>Исполнителя</b>',
            parse_mode='html'
        )
        if len([x for x in anketa_isp[0] if x is not None]) > 1:
            markup.add(change, find)

            message = bot.send_message(
                message.chat.id,
                'У вас уже есть анкета, хотите изменить старую или перейти к поиску <b>Заказчиков</b>?',
                parse_mode='html',
                reply_markup=markup
            )
            bot.register_next_step_handler(message, action_reply)
        else:
            markup.add(create, find)

            message = bot.send_message(
                message.chat.id,
                'У вас еще нет анкеты, хотите её создать, или сразу перейти к поиску <b>Исполнителей</b>?',
                parse_mode='html',
                reply_markup=markup
            )
            bot.register_next_step_handler(message, action_reply)
    elif (message.text == '/stop'):
        bot.send_message(
            message.chat.id,
            'Текущий диалог остановлен, если вам нужна дополнительная информация, напишите /help или /info',
            reply_markup=types.ReplyKeyboardRemove()
        )
    else:
        message = bot.send_message(
            message.chat.id,
            'Ошибка, вы дали неверный ответ, нажмите кнопку, либо, если вы хотите остановить текущий диалог, напишите /stop'
        )
        bot.register_next_step_handler(message, start_reply)


# ------ Перенаправление диалога в нужную команду, после ответа пользователя ------ 
def action_reply(message):
    if (message.text == 'Изменить'):
        change(message)
    elif (message.text == 'Создать'):
        create(message)
    elif (message.text == 'Поиск'):
        find(message)


# -------------- Изменение заявки/анкеты для заказчика и исполнителя -------------- 
@bot.message_handler(commands=['change', 'изменение'])
def change(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    markup.add(yes, no)

    if (userType == 'Заказчик'):

        cursor.execute("SELECT name, number, city from public.users where id = {0}".format(message.from_user.id))
        user = cursor.fetchall()

        cursor.execute("SELECT act_type, problem from public.zak where uid = {0}".format(message.from_user.id))
        form = cursor.fetchall()
        print(user)
        print(form)
        anketa = 'Имя: {0[0][0]}\nТелефон: {0[0][1]}\nГород: {0[0][2]}\nТип: {1[0][0]}\nПроблема: {1[0][1]}'.format(
            user, form)

        bot.send_message(message.chat.id, 'Ваша заявка\n\n{0}'.format(anketa))

        message = bot.send_message(
            message.chat.id,
            'Хотите что-то изменить?',
            reply_markup=markup
        )
        bot.register_next_step_handler(message, change_reply)
    elif (userType == 'Исполнитель'):

        cursor.execute("SELECT name, number, city from public.users where id = {0}".format(message.from_user.id))
        user = cursor.fetchall()

        cursor.execute("SELECT activity, exp, about from public.isp where uid = {0}".format(message.from_user.id))
        form = cursor.fetchall()
        anketa = 'Имя: {0[0][0]}\nТелефон: {0[0][1]}\nГород: {0[0][2]}\nЧем занимается: {1[0][0]}\nСтаж: {1[0][1]}\nО себе: {1[0][2]}'.format(
            user, form)
        bot.send_message(message.chat.id, 'Ваша анкета\n\n{0}'.format(anketa))

        message = bot.send_message(
            message.chat.id,
            'Хотите её изменить?',
            reply_markup=markup
        )
        bot.register_next_step_handler(message, change_reply)
    else:
        bot.send_message(message.chat.id,
                         'Вы еще не указали, либо произошла какая-ыберите что вы хотите изменить?то ошибка, воспользуйтесь командой /changeType, и затем повторно напишите /change')


def change_reply(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    name = types.KeyboardButton('Имя')
    number = types.KeyboardButton('Телефон')
    city = types.KeyboardButton('Город')
    problem = types.KeyboardButton('Проблему')
    about = types.KeyboardButton('О себе')
    type = types.KeyboardButton('Тип')
    experience = types.KeyboardButton('Стаж')
    activities = types.KeyboardButton('Тип услуги')

    if (message.text == 'Да'):
        if (userType == 'Заказчик'):
            markup.add(name, number, city, type, problem)
        elif (userType == 'Исполнитель'):
            markup.add(name, number, city, activities, experience, about)

        message = bot.send_message(
            message.chat.id,
            'Выберите что вы хотите изменить?',
            reply_markup=markup
        )

        bot.register_next_step_handler(message, change_acceptance)
    elif (message.text == 'Нет'):
        bot.send_message(
            message.chat.id,
            'В таком случае, воспользуйтесь командами /help или /info, для того чтобы найти нужную Вам функцию',
            reply_markup=types.ReplyKeyboardRemove()
        )
    elif (message.text == '/stop'):
        bot.send_message(
            message.chat.id,
            'Текущий диалог остановлен, если вам нужна дополнительная информация, напишите /help или /info',
            reply_markup=types.ReplyKeyboardRemove()
        )
    else:
        message = bot.send_message(
            message.chat.id,
            'Ошибка, вы дали неверный ответ, нажмите кнопку, либо, если вы хотите остановить текущий диалог, напишите /stop'
        )
        bot.register_next_step_handler(message, change_reply)


def change_acceptance(message):
    global changeType
    changeType = message.text
    if (changeType == 'Имя'):
        message = bot.send_message(
            message.chat.id,
            'Напишите новое имя'
        )
        bot.register_next_step_handler(message, change_text)
    elif (changeType == 'Телефон'):
        message = bot.send_message(
            message.chat.id,
            'Напишите новый телефон'
        )
        bot.register_next_step_handler(message, change_text)
    elif (changeType == 'Город'):
        message = bot.send_message(
            message.chat.id,
            'Напишите название города'
        )
        bot.register_next_step_handler(message, change_text)
    elif (changeType == 'Тип'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        tech = types.KeyboardButton("Техника")
        comp = types.KeyboardButton("Компьютеры и IT")
        mal = types.KeyboardButton("Строительство")

        markup.add(tech, comp, mal)

        message = bot.send_message(
            message.chat.id,
            'Выберите тип проблемы',
            parse_mode='html',
            reply_markup=markup
        )
        bot.register_next_step_handler(message, change_text)
    elif (changeType == 'Проблему'):
        message = bot.send_message(
            message.chat.id,
            'Опишите проблему (в одном сообщении)'
        )
        bot.register_next_step_handler(message, change_text)
    elif (changeType == 'О себе'):
        message = bot.send_message(
            message.chat.id,
            'Напишите о себе (в одном сообщении)'
        )
        bot.register_next_step_handler(message, change_text)
    elif (changeType == 'Стаж'):
        message = bot.send_message(
            message.chat.id,
            'Напишите новый телефон'
        )
        bot.register_next_step_handler(message, change_text)
    elif (changeType == 'Тип услуги'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        tech = types.KeyboardButton("Техника")
        comp = types.KeyboardButton("Компьютеры и IT")
        mal = types.KeyboardButton("Строительство")

        markup.add(tech, comp, mal)

        message = bot.send_message(
            message.chat.id,
            'Укажите услугу которыми вы занимаетесь',
            parse_mode='html',
            reply_markup=markup
        )
        # TODO Тут, как я думаю, надо добавить услуги в качестве кнопок под сообщением, хотя я пока хз как это реализовать
        # мб лучше сделать чтобы челу просто вывелся список возможных услуг и он их писал по одной в сообщении, либо одним сообщением все перечислил
        # там мы проверяем чтобы он правильно написал и обновляем базу
        # Либо вообще сделать чтобы чел просто ручками писал все услуги и забить хер, на то, что он может с ошибкой написать, а поиск анкет реализовать через поиск строки
        bot.register_next_step_handler(message, change_text)
    elif (message.text == '/stop'):
        changeType = ''
        bot.send_message(
            message.chat.id,
            'Текущий диалог остановлен, если вам нужна дополнительная информация, напишите /help или /info',
            reply_markup=types.ReplyKeyboardRemove()
        )
    else:
        changeType = ''
        message = bot.send_message(
            message.chat.id,
            'Ошибка, вы дали неверный ответ, нажмите кнопку, либо, если вы хотите остановить текущий диалог, напишите /stop'
        )
        bot.register_next_step_handler(message, change_acceptance)

    # TODO-CHANGE Сделать обновление данных в БД


def change_text(message):
    # user_Z, user_I это анкеты заказчика и исполнителя
    global user_Z, user_I

    if (changeType == 'Имя'):
        if (userType == 'Заказчик'):
            cursor.execute(
                "INSERT INTO public.users (id, name) VALUES('{1}', '{0}') "
                "ON CONFLICT (id) "
                "DO UPDATE SET name = '{0}' where users.id = '{1}'".format(
                    message.text, message.from_user.id))
            user_Z[0] = message.text
        elif (userType == 'Исполнитель'):
            cursor.execute(
                "INSERT INTO public.users (id, name) VALUES('{1}', '{0}') "
                "ON CONFLICT (id) "
                "DO UPDATE SET name = '{0}' where users.id = '{1}'".format(
                    message.text, message.from_user.id))
            user_I[0] = message.text
    elif (changeType == 'Телефон'):
        if (userType == 'Заказчик'):
            cursor.execute(
                "INSERT INTO public.users (id, number) VALUES('{1}', '{0}') "
                "ON CONFLICT (id) "
                "DO UPDATE SET number = '{0}' where users.id = '{1}'".format(
                    message.text, message.from_user.id))
            user_Z[1] = message.text
        elif (userType == 'Исполнитель'):
            cursor.execute(
                "INSERT INTO public.users (id, number) VALUES('{1}', '{0}') "
                "ON CONFLICT (id) "
                "DO UPDATE SET number = '{0}' where users.id = '{1}'".format(
                    message.text, message.from_user.id))
            user_I[1] = message.text
    elif (changeType == 'Город'):
        if (userType == 'Заказчик'):
            cursor.execute(
                "INSERT INTO public.users (id, city) VALUES('{1}', '{0}') "
                "ON CONFLICT (id) "
                "DO UPDATE SET city = '{0}' where users.id = '{1}'".format(
                    message.text, message.from_user.id))
            user_Z[2] = message.text
        elif (userType == 'Исполнитель'):
            cursor.execute(
                "INSERT INTO public.users (id, city) VALUES('{1}', '{0}') "
                "ON CONFLICT (id) "
                "DO UPDATE SET city = '{0}' where users.id = '{1}'".format(
                    message.text, message.from_user.id))
            user_I[2] = message.text
    elif (changeType == 'Проблему'):
        cursor.execute(
            "INSERT INTO public.zak (uid, problem) VALUES('{1}', '{0}') "
            "ON CONFLICT (uid) "
            "DO UPDATE SET problem = '{0}' where zak.uid = '{1}'".format(
                message.text, message.from_user.id))
        user_Z[4] = message.text
    elif (changeType == 'О себе'):
        cursor.execute(
            "INSERT INTO public.isp (uid, about) VALUES('{1}', '{0}') "
            "ON CONFLICT (uid) "
            "DO UPDATE SET about = '{0}' where isp.uid = '{1}'".format(
                message.text, message.from_user.id))
        user_I[5] = message.text
    elif (changeType == 'Стаж'):
        cursor.execute(
            "INSERT INTO public.isp (uid, exp) VALUES('{1}', '{0}') "
            "ON CONFLICT (uid) "
            "DO UPDATE SET exp = '{0}' where isp.uid = '{1}'".format(
                message.text, message.from_user.id))
        user_I[4] = message.text
    elif (changeType == 'Тип услуги'):
        cursor.execute(
            "INSERT INTO public.isp (uid, activity) VALUES('{1}', '{0}') "
            "ON CONFLICT (uid) "
            "DO UPDATE SET activity = '{0}' where isp.uid = '{1}'".format(
                message.text, message.from_user.id))
        user_I[3] = message.text
    elif (changeType == 'Тип'):
        cursor.execute(
            "INSERT INTO public.zak (uid, act_type) VALUES('{1}', '{0}') "
            "ON CONFLICT (uid) "
            "DO UPDATE SET act_type = '{0}' where zak.uid = '{1}'".format(
                message.text, message.from_user.id))
        user_Z[3] = message.text

    conn.commit()
    change(message)


@bot.message_handler(commands=['create', 'создать'])
def create(message):
    if userType == 'Заказчик':
        cursor.execute("select * from public.zak where uid = {0}".format(message.from_user.id))
        arr_len = len(cursor.fetchall())
        if arr_len > 1:
            bot.send_message(message.chat.id,
                             'У вас уже есть созданная заявка, воспользуйтесь командами:\n/form - чтобы её посмотреть\n/change - чтобы её изменить\n/clear - чтобы её удалить')
        else:
            bot.send_message(
                message.chat.id,
                'Пример заявки:\n\nИмя: Кирилл\nТелефон: +7 (777) 777-77-77\nГород: Москва\nТип: Техника\nПроблема: Не работает капучинатор, пенки нет совсем, пар идет а молоко не взбивается. машинке месяц, изначально пенка доходила до 3-4 см (Модель Philips EP1224/00)'
            )
            create_reply(message)
    elif userType == 'Исполнитель':
        cursor.execute("select * from public.isp where uid = {0}".format(message.from_user.id))
        arr_len = len(cursor.fetchall())
        if arr_len > 1:
            bot.send_message(message.chat.id,
                             'У вас уже есть созданная анкета, воспользуйтесь командами:\n/form - чтобы её посмотреть\n/change - чтобы её изменить\n/clear - чтобы её удалить')
        else:
            bot.send_message(
                message.chat.id,
                'Пример заявки:\n\nИмя: Кирилл\nТелефон: +7 (777) 777-77-77\nГород: Москва\nЧем занимается: Репетитор, Компьютеры и IT\nСтаж: 4 года\nО себе: Легко нахожу контакт с людьми'
            )
            create_reply(message)
    else:
        bot.send_message(message.chat.id,
                         'Вы еще не указали, либо произошла какая-то ошибка, воспользуйтесь командой /changeType, и затем повторно напишите /create')


def create_reply(message):
    global input_len, input_len_max, user_Z, user_I, input_

    if (input_len_max != 0):
        input_[input_len - 1] = message.text
    else:
        if userType == 'Заказчик':
            input_len_max = 4
        else:
            input_len_max = 5

            # TODO На случай если решим отменить повторный ввод имени при пересоздании заявки
        # cursor.execute("SELECT * FROM public.users where id = {0};".format(message.from_user.id))
        # anketa_user = cursor.fetchall()
        # print(len([x for x in anketa_user[0] if x is not None]))
        # if len([x for x in anketa_user[0] if x is not None]) > 1:
        #     input_len = 3

    if input_len <= input_len_max:
        if input_len == 0:
            message = bot.send_message(message.chat.id, 'Введите Ваше имя')
        elif input_len == 1:
            message = bot.send_message(message.chat.id, 'Введите Ваш телефон')
        elif input_len == 2:
            if userType == 'Заказчик':
                message = bot.send_message(message.chat.id, 'В каком городе вы находитесь?')
            else:
                message = bot.send_message(message.chat.id, 'Напишите название города, в котором Вы оказываете услуги')
        elif input_len == 3:
            if userType == 'Заказчик':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                tech = types.KeyboardButton("Техника")
                comp = types.KeyboardButton("Компьютеры и IT")
                mal = types.KeyboardButton("Строительство")

                markup.add(tech, comp, mal)

                message = bot.send_message(
                    message.chat.id,
                    'Выберите тип проблемы',
                    parse_mode='html',
                    reply_markup=markup
                )

            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                tech = types.KeyboardButton("Техника")
                comp = types.KeyboardButton("Компьютеры и IT")
                mal = types.KeyboardButton("Строительство")

                markup.add(tech, comp, mal)

                message = bot.send_message(
                    message.chat.id,
                    'Выберите один из предложенных видов деятельности',
                    parse_mode='html',
                    reply_markup=markup
                )
        elif (input_len == 4):
            if (userType == 'Заказчик'):
                message = bot.send_message(message.chat.id, 'Напишите в чем заключается проблема (в одном сообщении)')
            else:
                message = bot.send_message(message.chat.id, 'Укажите Ваш стаж')
        elif (input_len == 5):
            message = bot.send_message(message.chat.id,
                                       'Напишите небольшое предложение о себе, описывающее вашу деятельность')

        input_len += 1
        bot.register_next_step_handler(message, create_reply)

    else:
        input_len = 0
        input_len_max = 0
        # TODO-CREATE Сделать добавление новой анкеты/заявки в БД

        if (userType == 'Заказчик'):
            # В input_ хранятся внесенные данные пользователем
            user_Z = input_
            cursor.execute(
                "UPDATE public.users SET name = '{0[0]}', number = '{0[1]}', city = '{0[2]}' where id = '{1}'".format(
                    user_Z, message.from_user.id))
            cursor.execute(
                "INSERT INTO public.zak (uid, act_type,problem) VALUES('{1}','{0[3]}','{0[4]}') "
                "ON CONFLICT (uid) "
                "DO UPDATE SET act_type = '{0[3]}', problem = '{0[4]}' where zak.uid = '{1}'".format(user_Z,
                                                                                                     message.from_user.id))
            conn.commit()
        else:
            user_I = input_
            cursor.execute(
                "UPDATE public.users SET name = '{0[0]}',number = '{0[1]}', city = '{0[2]}' where id = '{1}'".format(
                    user_I, message.from_user.id))
            cursor.execute(
                "INSERT INTO public.isp (uid, activity, exp, about) VALUES('{1}','{0[3]}','{0[4]}', '{0[5]}') "
                "ON CONFLICT (uid) "
                "DO UPDATE SET activity = '{0[3]}', exp = '{0[4]}', about = '{0[5]}' where isp.uid = '{1}'".format(
                    user_I, message.from_user.id))
            conn.commit()

        change(message)


@bot.message_handler(commands=['find', 'поиск'])
def find(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    tech = types.KeyboardButton("Техника")
    comp = types.KeyboardButton("Компьютеры и IT")
    mal = types.KeyboardButton("Строительство")

    markup.add(tech, comp, mal)  # Тут по идее в переменной просто должны будут быть
    # перечислены все возможные сферы можно в принципе не делать выгрузку из бд

    if (userType == 'Заказчик'):
        message = bot.send_message(
            message.chat.id,
            'Выберете по какой сфере вы хотите искать <b>Исполнителя</b>',
            parse_mode='html',
            reply_markup=markup
        )
        bot.register_next_step_handler(message, find_reply)
    elif (userType == 'Исполнитель'):
        message = bot.send_message(
            message.chat.id,
            'Выберете по какому типу вы хотите искать <b>Заказчика</b>',
            parse_mode='html',
            reply_markup=markup
        )
        bot.register_next_step_handler(message, find_reply)
    else:
        bot.send_message(message.chat.id,
                         'Вы еще не указали, либо произошла какая-то ошибка, воспользуйтесь командой /changeType, и затем повторно напишите /find')


def find_reply(message):
    global find_list, search_
    find_list = []
    # TODO Здесь сделать выгрузку анкет/заявок по message.text и добавить их в find_list, дальше все по автомату работает
    # Тут щас работает таким образом, в list_ я храню все анкеты/заявки в зависимости от типа пользователя и потом через цикл пробегаюсь по всем элементам
    # Тебе как-то по аналогии надо будет переделать либо чтобы из базы сразу выгружались отсортированные либо выгружать всех и тут фильтровать, подумаешь как лучше

    if userType == 'Заказчик':
        cursor.execute("select id,name,number, city, activity, exp, about "
                       "from public.users "
                       "join public.isp i on users.id = i.uid")
        anketa_I = cursor.fetchall()
        for isp in anketa_I:
            if isp[4] == message.text:
                find_list.append(
                    'Имя: {0[1]}\nТелефон: {0[2]}\nГород: {0[3]}\nЧем занимается: {0[4]}\nСтаж: {0[5]}\nО себе: {0[6]}'.format(
                        isp))
    else:
        cursor.execute("select id,name,number, city, act_type, problem "
                       "from public.users "
                       "join public.zak z on users.id = z.uid")
        anketa_Z = cursor.fetchall()
        for isp in anketa_Z:
            if isp[4] == message.text:
                find_list.append(
                    'Имя: {0[1]}\nТелефон: {0[2]}\nГород: {0[3]}\nТип проблемы: {0[4]}\nПроблема: {0[5]}'.format(isp))

    find_show(message)


def find_show(message):
    global input_len, input_len_max
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    markup.add(yes, no)

    if input_len_max == 0 or message.text == 'Да':
        input_len_max = len(find_list)
        if userType == 'Заказчик':
            if len(find_list) == 0:
                bot.send_message(
                    message.chat.id,
                    'По этой сфере пока нет активных <b>Исполнителя</b>',
                    parse_mode='html',
                    reply_markup=types.ReplyKeyboardRemove()
                )
                input_len = 0
                input_len_max = 0
            else:
                while input_len < input_len_max:
                    bot.send_message(message.chat.id, '{0}'.format(find_list[input_len]))
                    input_len += 1
                    if (input_len % 3 == 0):
                        break
                if (input_len >= input_len_max):
                    bot.send_message(
                        message.chat.id,
                        'По этой сфере закончились активные <b>Исполнители</b>',
                        reply_markup=types.ReplyKeyboardRemove(),
                        parse_mode='html'
                    )
                    input_len = 0
                    input_len_max = 0
                else:
                    message = bot.send_message(
                        message.chat.id,
                        'Вывести следующих <b>Исполнителей</b>?',
                        parse_mode='html',
                        reply_markup=markup
                    )
                    bot.register_next_step_handler(message, find_show)
        else:
            if (len(find_list) == 0):
                bot.send_message(
                    message.chat.id,
                    'По этой теме пока нет активных <b>Заказчиков</b>',
                    parse_mode='html',
                    reply_markup=types.ReplyKeyboardRemove()
                )
                input_len = 0
                input_len_max = 0
            else:
                while input_len < input_len_max:
                    bot.send_message(message.chat.id, '{0}'.format(find_list[input_len]))
                    input_len += 1
                    if (input_len % 3 == 0):
                        break
                if (input_len >= input_len_max):
                    bot.send_message(
                        message.chat.id,
                        'По этой теме закончились активные <b>Заказчики</b>',
                        parse_mode='html',
                        reply_markup=types.ReplyKeyboardRemove()
                    )
                    input_len = 0
                    input_len_max = 0
                else:
                    message = bot.send_message(
                        message.chat.id,
                        'Вывести следующих <b>Заказчиков</b>?',
                        parse_mode='html',
                        reply_markup=markup
                    )
                    bot.register_next_step_handler(message, find_show)
    else:
        bot.send_message(
            message.chat.id,
            'Воспользуйтесь /info, чтобы найти нужную команду',
            parse_mode='html',
            reply_markup=types.ReplyKeyboardRemove()
        )
        input_len = 0
        input_len_max = 0
    # TODO Дописать команду хелп с выводом всех команд и их описанием


@bot.message_handler(commands=['help', 'info', 'помощь', ])
def info(message):
    bot.send_message(
        message.chat.id,
        'Для взаимодействия с ботом можно пользоваться существующими командами, на них можно нажимать и они автоматически будут продублированы в качестве Вашего сообщения в чат, либо их можно запомнить и писать их вручную\n'
        '\nКоманды:\n'
        '<b>/start /старт</b>\nДля начала взаимодействия с ботом\n'
        '<b>/type /тип</b>\nЧтобы узнать Вашу выбранную роль\n'
        '<b>/changeType /изменитьТип</b>\nДля смены роли (<b>Заказчик</b>, <b>Исполнитель</b>)\n'
        '<b>/form /анкета</b>\nДля просмотра анкеты/заявки\n'
        '<b>/create /создать</b>\nДля создания анкеты/заявки\n'
        '<b>/change /изменить</b>\nДля изменения текста анкеты/заявки\n'
        '<b>/find /поиск</b>\nДля поиска людей по анкетам/заявкам\n'
        '<b>/clear /delete /очистить /удалить</b>\nЧтобы удалить созданную заявку/анкету\n'
        '<b>/help /info /помощь</b>\nДополнительная информация по взаимодействию с ботом, а так же со списком всех возможных команд\n',
        parse_mode='html'
    )


@bot.message_handler(commands=['анкета', 'form', 'заявка', 'request'])
def anketa(message):
    # TODO Добавить вывод анкеты/заявки из БД
    if (userType == 'Исполнитель'):
        if (len(user_I) != 0):
            cursor.execute("SELECT name, number, city from public.users where id = {0}".format(message.from_user.id))
            user = cursor.fetchall()

            cursor.execute("SELECT activity, exp, about from public.isp where uid = {0}".format(message.from_user.id))
            form = cursor.fetchall()

            anketa = 'Имя: {0[0][0]}\nТелефон: {0[0][1]}\nГород: {0[0][2]}\nЧем занимается: {1[0][0]}\nСтаж: {1[0][1]}\nО себе: {1[0][2]}'.format(
                user, form)
            bot.send_message(message.chat.id, 'Ваша анкета\n\n{0}'.format(anketa))
        else:
            bot.send_message(message.chat.id, 'У вас нет активной анкеты')
    elif (userType == 'Заказчик'):
        if (len(user_Z) != 0):

            cursor.execute("SELECT name, number, city from public.users where id = {0}".format(message.from_user.id))
            user = cursor.fetchall()

            cursor.execute("SELECT act_type, problem from public.zak where uid = {0}".format(message.from_user.id))
            form = cursor.fetchall()

            anketa = 'Имя: {0[0][0]}\nТелефон: {0[0][1]}\nГород: {0[0][2]}\nТип проблемы: {1[0][0]}\nПроблема: {1[0][1]}'.format(
                user, form)
            bot.send_message(message.chat.id, 'Ваша заявка\n\n{0}'.format(anketa))
        else:
            bot.send_message(message.chat.id, 'У вас нет активной заявки')
    else:
        bot.send_message(message.chat.id, 'Вы еще не указали свою роль')


@bot.message_handler(commands=['clear', 'удалить', 'очистить', 'delete'])
def clear(message):
    global user_I, user_Z
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    markup.add(yes, no)

    if (
            message.text == '/clear' or message.text == '/delete' or message.text == '/удалить' or message.text == '/очистить'):
        anketa(message)
        message = bot.send_message(
            message.chat.id,
            'Вы точно хотите её удалить?',
            reply_markup=markup
        )
        bot.register_next_step_handler(message, clear)
    elif (message.text == 'Да'):
        if (userType == 'Заказчик'):
            cursor.execute("DELETE from public.zak where uid = '{0}'".format(message.from_user.id))
            conn.commit()
            bot.send_message(message.chat.id, 'Ваша заявка удалена')
            user_Z = []
        else:
            cursor.execute("DELETE from public.isp where uid = '{0}'".format(message.from_user.id))
            conn.commit()
            bot.send_message(message.chat.id, 'Ваша анкета удалена')
            user_I = []
    elif (message.text == 'Нет'):
        bot.send_message(
            message.chat.id,
            'Если вам нужна дополнительная информация, напишите /help или /info',
            reply_markup=types.ReplyKeyboardRemove()
        )
    else:
        message = bot.send_message(
            message.chat.id,
            'Ошибка, вы дали неверный ответ, нажмите кнопку, либо, если вы хотите остановить текущий диалог, напишите Нет'
        )
        bot.register_next_step_handler(message, clear)


@bot.message_handler(commands=['changeType', 'изменитьТип'])
def changeType_(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    client = types.KeyboardButton('Заказчик')
    executor = types.KeyboardButton('Исполнитель')
    markup.add(client, executor)

    message = bot.send_message(
        message.chat.id,
        "Выберите Вашу роль: <b>Заказчик</b> или <b>Исполнитель</b>?"
            .format(bot.get_me()),
        parse_mode='html',
        reply_markup=markup
    )
    bot.register_next_step_handler(message, changeType_reply)


def changeType_reply(message):
    global userType

    if (message.text == 'Заказчик'):
        userType = message.text
        bot.send_message(
            message.chat.id,
            'Вы выбрали роль <b>Заказчика</b>',
            parse_mode='html'
        )
    elif (message.text == 'Исполнитель'):
        userType = message.text
        bot.send_message(
            message.chat.id,
            'Вы выбрали роль <b>Исполнителя</b>',
            parse_mode='html'
        )
    elif (message.text == '/stop'):
        bot.send_message(
            message.chat.id,
            'Текущий диалог остановлен, если вам нужна дополнительная информация, напишите /help или /info',
            reply_markup=types.ReplyKeyboardRemove()
        )
    else:
        message = bot.send_message(
            message.chat.id,
            'Ошибка, вы дали неверный ответ, нажмите кнопку, либо, если вы хотите остановить текущий диалог, напишите /stop'
        )
        bot.register_next_step_handler(message, changeType_reply)


@bot.message_handler(commands=['type', 'тип'])
def type(message):
    if (len(userType) <= 0):
        bot.send_message(
            message.chat.id,
            "Вы пока не указали тип"
        )
    else:
        bot.send_message(
            message.chat.id,
            "Ваш тип: <b>{0}</b>".format(userType),
            parse_mode='html'
        )


@bot.message_handler(content_types=['text'])
def respond(message):
    if message.chat.type == 'private':
        if message.text == 'Заказчик':
            bot.send_message(message.chat.id,
                             "Если вы хотите выбрать роль заказчика, напишите /changeType, либо напишите /start")
        elif message.text == 'Исполнитель':
            bot.send_message(message.chat.id,
                             "Если вы хотите выбрать роль исполнителя, напишите /changeType, либо напишите /start")
        else:
            bot.send_message(message.chat.id, "Я не знаю как вам ответить, попробуйте написать /help либо /info")


# RUN
# bot.polling(none_stop=True)
# bot.infinity_polling(True)


bot.polling(none_stop=True)
