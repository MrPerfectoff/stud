def send_mail(message, recipient,*, sender = "university.help@gmail.com"):
    domains = (".com", '.ru', '.net')
    if ('@' not in recipient or not recipient.endswith(domains)) or ('@' not in sender or not sender.endswith(domains)):
        print(f"He возможно отправить писмо с адреса с {sender} на адрес {recipient}")
        return
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == "university.help@gmail.com" :
        print('Письмо успошно отправлено с адреса ' + sender + ' на адрес ' + recipient)
    else:
        print(f'не стандартный отправитель! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_mail('a', 'test@mail.com')

