from EmailNotification import EmailNotification
from SMSNotification import SMSNotification


def send_bulk(notifiers, message):    
    for notifier in notifiers:
        notifier.send(message)


notifiers = [
    EmailNotification(),
    SMSNotification(),
    EmailNotification()
]

send_bulk(notifiers, "Your order has been shipped!")
