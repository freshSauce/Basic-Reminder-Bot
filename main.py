from flask import Flask, request, jsonify, Response
import requests as r
import datetime
import os
import uuid
import time
import threading
import re
from flask_pymongo import PyMongo
from collections import defaultdict
app = Flask(__name__)

app.config[
    "MONGO_URI"
] = f"mongodb+srv://freshSauce:{os.environ['DB_PASSWORD']}@reminders.bthpa.mongodb.net/reminders?retryWrites=true&w=majority"

#reminders = defaultdict(list)

database = PyMongo(app)

reminders = database.db.reminders


def constantCheck(user_id):
    while True:
        if reminders.find({"user_id": user_id}):
            for reminder in reminders.find({"user_id": user_id}):
                if reminder["dateReminder"] <= datetime.datetime.now():
                    reply_to_message(reminder["message_id"], reminder["chat_id"], "Reminder: " + reminder["dateReminder"].strftime('%d/%m/%Y'))
                    reminders.delete_one({"UUID": reminder["UUID"]})
                    time.sleep(5)
                    #reminders[user_id].remove(reminder)
        else:
            break
        

API_URL = f"https://api.telegram.org/bot{os.environ['API_KEY']}"
regex = r"(?<=en)(\s[\d]{1,2}\saños|\s[\d]{1,2}\saño)|(\s[\d]{1,2}\smeses|\s[\d]{1,2}\smes)|(\s[\d]{1,2}\sdías|\s[\d]{1,2}\sdía)|(\s[\d]{1,2}\shoras|\s[\d]{1,2}\shora)|(\s[\d]{1,2}\sminutos|\s[\d]{1,2}\sminuto)"



@app.route('/')
def index():
    return os.environ['API_KEY']

@app.route('/receive_info', methods = ['POST', 'GET'])
def receive_info():
    if request.method == 'POST':
        data = request.get_json()
        
        try:
            message = data['message']
            #print(message['text'])
        except KeyError:
            return Response('OK', status = 200)
        
        try:
            command = message['text'].split(' ')[0]
        except IndexError:
            reply_to_message(data['message']['message_id'], data['message']['chat']['id'], "Missing arguments")
            return Response('Ok', 200)

        match command:
            
            case '/remind' | '/remind@BasicReminder_Bot':
                if data.get('message').get('reply_to_message'):
                    try:
                        date = message['text'].split(' ')[1:]
                    except IndexError:
                        reply_to_message(data['message']['message_id'], data['message']['chat']['id'], "Missing arguments")
                        return Response('Ok', 200)
                    else:
                        createReminder(data['message']['message_id'], data['message']['chat']['id'], data['message']['from']['id'], date)
                else:
                    pass
            case '/myreminders' | '/myreminders@BasicReminder_Bot':
                myReminders(data['message']['message_id'], data['message']['chat']['id'], data['message']['from']['id'])
            case '/help' | '/help@BasicReminder_Bot':
                reply_to_message(data['message']['message_id'], data['message']['chat']['id'], "Available commands: /remind, /myreminders, /help")
            case _:
                pass



        return Response('Ok', 200)
    else:
        return Response('Method not allowed', 405)

def createReminder(message_id, chat_id, user_id, date):
    date = ' '.join(date)

    timedelta = datetime.timedelta()
    if re.search(regex, date):
        timeList = [time for itemList in re.findall(regex, date) for time in itemList if time]
        for time in timeList:
            time = [time for time in time.replace('í', 'i').split(' ') if time]
            #print(time)
            if any(isThere in time for isThere in ('año', 'años')):
                timedelta += datetime.timedelta(days = 365 * int(time[0]))
            elif any(isThere in time for isThere in ('mes', 'meses')):
                timedelta += datetime.timedelta(days = 30 * int(time[0]))
            elif any(isThere in time for isThere in ('dia', 'dias')):
                timedelta += datetime.timedelta(days = int(time[0]))
            elif any(isThere in time for isThere in ('hora', 'horas')):
                timedelta += datetime.timedelta(hours = int(time[0]))
            elif any(isThere in time for isThere in ('minuto', 'minutos')):
                timedelta += datetime.timedelta(minutes = int(time[0]))
            else:
                reply_to_message(message_id, chat_id, "Reminder couldn't be created\. Reason: No time specified")
                return False

        reminders.insert_one({
            "UUID": str(uuid.uuid4()),
            "message_id": message_id,
            "chat_id": chat_id,
            "user_id": user_id,
            "dateReminder": datetime.datetime.now() + timedelta
        })
        """ reminders[user_id].append(
                                    {"message_id": message_id, 
                                    "chat_id": chat_id, 
                                    "dateInitiated": datetime.datetime.now(), 
                                    "dateReminder": datetime.datetime.now() + timedelta}
                                    ) """

        reply_to_message(message_id, chat_id, "Reminder created")
        if reminders.find({"user_id": user_id}):
            p = threading.Thread(
                        target=constantCheck,
                        args=(user_id,),
                        daemon=True
                        )
            p.start()
        return True
    else:
            reply_to_message(message_id, chat_id, "Reminder couldn't be created\. Reason: No time specified")
            return False

def myReminders(message_id, chat_id, user_id):
    userReminders = reminders[user_id]

    if not userReminders:
        reply_to_message(message_id, chat_id, "No reminders")
    else:
        localReminders = []
        for reminder in userReminders:
            if reminder["chat_id"] == chat_id:
                localReminders.append(f"{reminder['dateReminder'].strftime('%d/%m/%Y')} \- [View message](https://t.me/c/{str(chat_id)[4:]}/{reminder['message_id']})")
        reply_to_message(message_id, chat_id, "Your reminders:\n" + '\n'.join(localReminders))

def reply_to_message(message_id, chat_id, text, parse_mode = 'MarkdownV2'):
    result = r.post(f"{API_URL}/sendMessage", data = {"chat_id": chat_id, "text": text, "reply_to_message_id": message_id, "parse_mode": parse_mode})
    if result.status_code != 200:
        print(result.json())
        return False
    return True




