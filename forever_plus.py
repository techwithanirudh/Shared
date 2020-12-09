# import os
# from time import strftime
# from reminder_json_helper import read_reminder_json, write_reminder_json
# from plyer import notification

# os.chdir(os.path.dirname(__file__))

# def timeFormat(reminder):
#     reminder = reminder.upper()
#     reminder = reminder.replace(' ', '')
#     return reminder

# def find_reminders_due():
#     reminders = read_reminder_json()
#     hr = list(strftime('%I'))
#     if hr[0] == '0':
#         hr = hr[1]
#     else:
#         hr = hr[0] + hr[1]

#     for rem in reminders:
#         print(timeFormat(rem['due_date']), strftime(f'%Y-%m-%d,{hr}:%M%p'))
#     reminders_due = [
#         reminder for reminder in reminders
#         if timeFormat(reminder['due_date']) == strftime(f'%Y-%m-%d,{hr}:%M%p')
#     ]
#     if len(reminders_due) > 0:
#         send_sms_reminder(reminders_due)

# def send_sms_reminder(reminders):
#     import time
#     for reminder in reminders:
#         print(reminder)
#         wait = int(reminder['interval'])
#         notification.notify(title='Reminder', message=reminder['message'], timeout=wait, app_icon='calendar.ico')
#         time.sleep(wait + 1)
#         delete_reminder(reminder)

# def delete_reminder(reminder):
#     reminders = read_reminder_json()
#     reminder_id = reminder['id']
#     reminder = [
#         reminder for reminder in reminders if reminder['id'] == reminder_id
#     ]
#     reminders.remove(reminder[0])
#     data = {}
#     data['reminders'] = reminders
#     write_reminder_json(data)

# if __name__ == '__main__':
#     while True:
#         try:
#             find_reminders_due()
#         except:
#             pass


import os
from time import strftime
from reminder_json_helper import read_reminder_json, write_reminder_json
from plyer import notification

os.chdir(os.path.dirname(__file__))

def timeFormat(reminder):
    reminder = reminder.upper()
    reminder = reminder.replace(' ', '')
    return reminder

def find_reminders_due():
    reminders = read_reminder_json()
    hr = list(strftime('%I'))
    if hr[0] == '0':
        hr = hr[1]
    else:
        hr = hr[0] + hr[1]
    for rem in reminders:
        print(timeFormat(rem['due_date']), strftime(f'%Y-%m-%d,{hr}:%M%p'))
        print(timeFormat(rem['due_date']).split(',')[0] == 'FOREVER')
    reminders_due = []
    for reminder in reminders:
        if not timeFormat(reminder['due_date']).split(',')[0] == 'FOREVER':
            if timeFormat(reminder['due_date']) == strftime(f'%Y-%m-%d,{hr}:%M%p'):
                reminders_due.append(reminder)
        else:
            if timeFormat(reminder['due_date']) == strftime(f'FOREVER,{hr}:%M%p'):
                reminders_due.append(reminder)
    print(reminders_due)
    if len(reminders_due) > 0:
        send_sms_reminder(reminders_due)

def send_sms_reminder(reminders):
    import time
    for reminder in reminders:
        print(reminder)
        wait = int(reminder['interval'])
        print('DATA: ', timeFormat(reminder['due_date']).split(',')[0].upper())
        notification.notify(title='Reminder', message=reminder['message'], timeout=wait, app_icon='calendar.ico')
        time.sleep(wait + 1)
        delete_reminder(reminder)
        if timeFormat(reminder['due_date']).split(',')[0].upper() == 'FOREVER':
            delete_reminder(reminder, update=True)

def delete_reminder(reminder, update=False):
    if not update:
        reminders = read_reminder_json()
        reminder_id = reminder['id']
        reminder = [
            reminder for reminder in reminders if reminder['id'] == reminder_id
        ]
        reminders.remove(reminder[0])
        data = {}
        data['reminders'] = reminders
        write_reminder_json(data)
    if update:
        while True:
            print('ERROR')

if __name__ == '__main__':
    while True:
        try:
            find_reminders_due()
        except:
            pass
