def send_email(message, recipient, sender="university.help@gmail.com"):
    domens = ['.com', '.ru', '.net']
    for i_1 in recipient:
        if i_1 == "@":
          for i_2 in sender:
             if i_2 == "@":
                for n_1 in domens:
                  if recipient[len(recipient) - len(n_1):len(recipient)] == n_1:
                       for n_2 in domens:
                          if sender[len(sender) - len(n_2):len(sender)] == n_2:
                             if sender == "university.help@gmail.com":
                                return print("Письмо успешно отправлени с адреса", sender,"на адрес",recipient)
                             elif recipient == sender:
                                return print("Невозможно отправить письмо самомму себе")
                             else:
                                return print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с", sender,"на адрес", recipient)
    return print("Невозможно отправить письмо c адреса", sender, "на адрес", recipient)
